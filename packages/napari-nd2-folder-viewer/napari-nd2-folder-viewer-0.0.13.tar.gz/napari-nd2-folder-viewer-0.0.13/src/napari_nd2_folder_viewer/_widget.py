"""
This module provides a widget to open a folder of nd2 files and show them continuously.
"""
from typing import TYPE_CHECKING

import os
import pandas as pd
import numpy as np
import dask.array as da
from dask.cache import Cache

import nd2
import napari
from sklearn.metrics import pairwise_distances
from napari_animation import Animation

from magicgui.widgets import FileEdit, Slider, Label
from qtpy.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
    QVBoxLayout,
)

from .exp_info import (
    get_exp_info,
    print_time_diff,
    antibiotic_exposure,
    calc_times,
    TimeDiff,
    to_datetime,
)

cache = Cache(2e10)  # Leverage twenty gigabytes of memory
cache.register()  # Turn cache on globally


def test_nd2_timestamps(times, nd2_file):
    if times.shape[0] != 1 and np.all(np.diff(times, axis=0) == 0.0):
        print(nd2_file)
        print("made adjustment")
        parameters = nd2_file.experiment[0].parameters
        try:
            period_ms = parameters.periodMs
        except AttributeError:
            period_ms = parameters.periods[0].periodMs
        period_time = period_ms / 1000
        in_julian = period_time / (24 * 3600)

        add_time = np.arange(times.shape[0]) * in_julian

        return times + add_time[:, np.newaxis, np.newaxis]
    return times


def get_position_names(nd2_file):
    for exp in nd2_file.experiment:
        if exp.type == "XYPosLoop":
            return [p.name for p in exp.parameters.points]
    return []


def get_zstack_size(coord_info):
    for ci in coord_info:
        if ci[1] == "ZStackLoop":
            return ci[2]
    return 0


def get_tstack_size(coord_info):
    for ci in coord_info:
        if ci[1] == "NETimeLoop" or ci[1] == "TimeLoop":
            return ci[2]
    return 0


def get_xy_size(coord_info):
    for ci in coord_info:
        if ci[1] == "XYPosLoop":
            return ci[2]
    return 0


def get_nd2_files_in_folder(folder):
    zstack_sizes = []
    channel_names_list = []
    nd2_files = []
    for f in sorted(os.listdir(folder)):
        if f.endswith(".nd2"):
            print(f)
            nd2_file = nd2.ND2File(os.path.join(folder, f))
            zstack_sizes.append(get_zstack_size(nd2_file._rdr._coord_info()))
            channel_names_list.append(nd2_file._rdr.channel_names())

            nd2_files.append(nd2_file)

    zlen = max(zstack_sizes)

    channel_names_len = [len(cn) for cn in channel_names_list]
    ind = np.argmax(channel_names_len)
    channel_names = channel_names_list[ind]

    xylen = nd2_files[ind].shape[-1]
    mlen = get_xy_size(nd2_files[ind]._rdr._coord_info())

    return nd2_files, xylen, mlen, zlen, channel_names


def insert_nd2_file_channels(img_, channel_names, channel_names_):
    imgs = []
    for i, cn in enumerate(channel_names):
        try:
            j = channel_names_.index(cn)
            imgs.append(img_[..., j, :, :])
        except ValueError:
            imgs.append(da.zeros_like(img_[..., 0, :, :]))
    img = da.stack(imgs, axis=-3)
    return img


def get_stage_positions(nd2_file):
    for exp in nd2_file.experiment:
        if exp.type == "XYPosLoop":
            return np.array([p.stagePositionUm for p in exp.parameters.points])
    return []


def get_position_names_and_inds(nd2_file, invert_x, invert_y):
    pos = get_stage_positions(nd2_file)
    if invert_x:
        pos[:, 0] *= -1

    dists = pairwise_distances(pos[:, 0][:, np.newaxis]).flatten()

    # beware hardcoded assumption of the distances
    nearest_neighbors_inds = np.logical_and(dists > 2000, dists < 6000)
    nearest_neighbors = dists[nearest_neighbors_inds]

    mean_diff = nearest_neighbors.mean()

    inds = []
    total_sort = []

    channel_names = np.empty(pos.shape[0], dtype=object)

    x_pos = pos[:, 0]

    min_x = x_pos.min()
    std_diff = mean_diff / 3

    nums = np.arange(pos.shape[0])

    for i in range(10):
        mid_ = min_x + i * mean_diff
        min_ = mid_ - std_diff
        max_ = mid_ + std_diff

        tmp_inds = np.logical_and(min_ < x_pos, x_pos < max_)
        inds.append(tmp_inds)

        y_pos = pos[tmp_inds, 1]
        sort_inds = np.argsort(y_pos)
        if invert_y:
            sort_inds = sort_inds[::-1]

        tmp_channel_names = np.empty(len(y_pos), dtype=object)
        tmp_channel_names[sort_inds] = [
            f"ch{i+1}-{j}" for j in range(1, len(y_pos) + 1)
        ]

        channel_names[tmp_inds] = tmp_channel_names

        total_sort.append(nums[tmp_inds][sort_inds])

    return inds, pos, channel_names, np.concatenate(total_sort)


def nd2_file_to_dask(nd2_file, zlen, channel_names, mlen, xylen):
    coord_info = nd2_file._rdr._coord_info()

    tlen_ = get_tstack_size(coord_info)
    if tlen_ == 0:
        tlen = 1
    else:
        tlen = tlen_

    zlen_ = get_zstack_size(coord_info)

    tmp_times = np.zeros((tlen, mlen, zlen))

    channel_names_ = nd2_file._rdr.channel_names()
    img = insert_nd2_file_channels(
        nd2_file.to_dask(), channel_names, channel_names_
    )

    if (
        tlen_ == 0
        or (tlen_ == 1 and zlen_ == 0 and img.ndim == 4)
        or (tlen_ == 1 and zlen_ != 0 and img.ndim == 5)
    ):
        img = da.expand_dims(img, axis=0)

    if zlen_ == 0:
        img = da.expand_dims(img, axis=2)

        first_img = da.zeros_like(img)
        shape = list(img.shape)
        shape[2] = zlen - 2
        last_imgs = da.zeros(
            tuple(shape),
            chunks=(1, 1, 1, 1, shape[4], shape[5]),
            dtype=np.uint16,
        )

        img = da.concatenate([first_img, img, last_imgs], axis=2)

    if tlen_ == 0 and zlen_ == 0:
        for i in range(nd2_file.metadata.contents.frameCount):
            k = nd2_file._rdr._coords_from_seq_index(i)
            tmp_times[:, k, :] = (
                nd2_file._rdr.frame_metadata(i)
                .channels[0]
                .time.absoluteJulianDayNumber
            )

    elif tlen_ == 0:
        print(nd2_file)
        print(img.shape)
        for i in range(nd2_file.metadata.contents.frameCount):
            k, l = nd2_file._rdr._coords_from_seq_index(i)
            tmp_times[:, k, l] = (
                nd2_file._rdr.frame_metadata(i)
                .channels[0]
                .time.absoluteJulianDayNumber
            )

    elif zlen_ == 0:
        for i in range(nd2_file.metadata.contents.frameCount):
            j, k = nd2_file._rdr._coords_from_seq_index(i)
            tmp_times[j, k, :] = (
                nd2_file._rdr.frame_metadata(i)
                .channels[0]
                .time.absoluteJulianDayNumber
            )

    else:
        for i in range(nd2_file.metadata.contents.frameCount):
            j, k, l = nd2_file._rdr._coords_from_seq_index(i)
            tmp_times[j, k, l] = (
                nd2_file._rdr.frame_metadata(i)
                .channels[0]
                .time.absoluteJulianDayNumber
            )

    return img, tmp_times


def nd2_file_to_time(nd2_file, zlen, channel_names, mlen, xylen):
    coord_info = nd2_file._rdr._coord_info()

    tlen_ = get_tstack_size(coord_info)
    if tlen_ == 0:
        tlen = 1
    else:
        tlen = tlen_

    zlen_ = get_zstack_size(coord_info)

    tmp_times = np.zeros((tlen, mlen, zlen))

    # channel_names_ = nd2_file._rdr.channel_names()
    # img = insert_nd2_file_channels(
    #     nd2_file.to_dask(), channel_names, channel_names_
    # )

    # if (
    #     tlen_ == 0
    #     or (tlen_ == 1 and zlen_ == 0 and img.ndim == 4)
    #     or (tlen_ == 1 and zlen_ != 0 and img.ndim == 5)
    # ):
    #     img = da.expand_dims(img, axis=0)

    # if zlen_ == 0:
    #     img = da.expand_dims(img, axis=2)

    #     first_img = da.zeros_like(img)
    #     shape = list(img.shape)
    #     shape[2] = zlen - 2
    #     last_imgs = da.zeros(
    #         tuple(shape),
    #         chunks=(1, 1, 1, 1, shape[4], shape[5]),
    #         dtype=np.uint16,
    #     )

    #     img = da.concatenate([first_img, img, last_imgs], axis=2)

    if tlen_ == 0 and zlen_ == 0:
        for i in range(nd2_file.metadata.contents.frameCount):
            k = nd2_file._rdr._coords_from_seq_index(i)
            tmp_times[:, k, :] = (
                nd2_file._rdr.frame_metadata(i)
                .channels[0]
                .time.absoluteJulianDayNumber
            )

    elif tlen_ == 0:
        print(nd2_file)
        # print(img.shape)
        for i in range(nd2_file.metadata.contents.frameCount):
            k, l = nd2_file._rdr._coords_from_seq_index(i)
            tmp_times[:, k, l] = (
                nd2_file._rdr.frame_metadata(i)
                .channels[0]
                .time.absoluteJulianDayNumber
            )

    elif zlen_ == 0:
        for i in range(nd2_file.metadata.contents.frameCount):
            j, k = nd2_file._rdr._coords_from_seq_index(i)
            tmp_times[j, k, :] = (
                nd2_file._rdr.frame_metadata(i)
                .channels[0]
                .time.absoluteJulianDayNumber
            )

    else:
        for i in range(nd2_file.metadata.contents.frameCount):
            j, k, l = nd2_file._rdr._coords_from_seq_index(i)
            tmp_times[j, k, l] = (
                nd2_file._rdr.frame_metadata(i)
                .channels[0]
                .time.absoluteJulianDayNumber
            )

    return tmp_times


def color_from_name(name):
    if "GFP" in name or "epi" in name:
        return "green"
    elif "mRuby" in name:
        return "red"
    elif "brightfield" in name or "Brightfield" in name:
        return "gray"
    else:
        return "blue"


class LoadWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        label1 = Label(value="<b>Open and save</b>")
        self.file_edit = FileEdit(label="Folder: ", mode="d")
        btn = QPushButton("Click me!")
        btn.clicked.connect(self._on_click)

        save_btn = QPushButton("Save analysis!")
        save_btn.clicked.connect(self._on_save_click)

        # self.anim_fps_slider = Slider(value=5, min=1, max=50, step=1)
        # anim_btn = QPushButton("Animate position!")
        # anim_btn.clicked.connect(self._animate_position)

        label2 = Label(value="<b>Navigate through position and time</b>")

        pos_btn = QPushButton("Play position!")
        pos_btn.clicked.connect(self._play_position)

        label_survival = Label(value="<b>Surviving</b>")

        next_btn = QPushButton("Next annotated surviving biofilm!")
        next_btn.clicked.connect(self.next_biofilm)

        prev_btn = QPushButton("Previous annotated surviving biofilm!")
        prev_btn.clicked.connect(self.prev_biofilm)

        label_single_cell = Label(value="<b>Surviving single cells</b>")

        single_next_btn = QPushButton("Next annotated single cells surviving!")
        single_next_btn.clicked.connect(self.next_biofilm_single_cell)

        single_prev_btn = QPushButton(
            "Previous annotated single cells surviving!"
        )
        single_prev_btn.clicked.connect(self.prev_biofilm_single_cell)

        label_dead = Label(value="<b>Non-surviving</b>")

        next_btn_dead = QPushButton("Next annotated non-surviving biofilm!")
        next_btn_dead.clicked.connect(self.next_biofilm_dead)

        prev_btn_dead = QPushButton(
            "Previous annotated non-surviving biofilm!"
        )
        prev_btn_dead.clicked.connect(self.prev_biofilm_dead)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(label1.native)
        self.layout().addWidget(self.file_edit.native)
        self.layout().addWidget(btn)
        self.layout().addWidget(save_btn)
        # self.layout().addWidget(self.anim_fps_slider.native)
        # self.layout().addWidget(anim_btn)
        self.layout().addWidget(label2.native)
        self.layout().addWidget(pos_btn)

        self.layout().addWidget(label_survival.native)
        self.layout().addWidget(next_btn)
        self.layout().addWidget(prev_btn)

        self.layout().addWidget(label_single_cell.native)
        self.layout().addWidget(single_next_btn)
        self.layout().addWidget(single_prev_btn)

        self.layout().addWidget(label_dead.native)
        self.layout().addWidget(next_btn_dead)
        self.layout().addWidget(prev_btn_dead)

        # varibales to be defined later
        self.times = None
        self.stack = None
        self.exp_info = None
        self.chip_channel_names = None
        self.channel_names = None
        self.colors = None
        self.opacities = None

        self.shape_layers = None
        self._shape_layer_info = [
            (
                "survival.csv",
                dict(
                    edge_color="white",
                    name="population survival",
                    ndim=4,
                ),
            ),
            (
                "single-cell-survival.csv",
                dict(
                    edge_color="#55ffffff",
                    edge_width=4,
                    name="single cells survive",
                    ndim=4,
                ),
            ),
            (
                "dead_biofilms_new.csv",
                dict(
                    edge_color="#2ae3ffff",
                    name="dead_biofilms",
                    ndim=3,
                ),
            ),
        ]

    def _animate_position(self):
        animation = Animation(self.viewer)
        self.viewer.update_console({"animation": animation})

        self.viewer.reset_view()

        current_step = list(self.viewer.dims.current_step)

        current_step[0] = 0
        self.viewer.dims.current_step = tuple(current_step)
        animation.capture_keyframe()

        timelen = self.stack.shape[0] - 1
        current_step[0] = timelen

        self.viewer.dims.current_step = tuple(current_step)
        animation.capture_keyframe(steps=timelen)

        pos = self.viewer.dims.current_step[1]
        pos_name = self.chip_channel_names[pos]
        z = self.viewer.dims.current_step[2]
        fps = self.anim_fps_slider.value
        animation.animate(
            os.path.join(
                self.file_edit.value, f"{pos_name}_pos{pos}_z{z}_fps{fps}.mov"
            ),
            fps=self.anim_fps_slider.value,
            quality=9,
        )

    def _play_position(self):
        new_viewer = napari.Viewer()
        position = self.viewer.dims.current_step[1]
        z = self.viewer.dims.current_step[2]

        for i in range(len(self.channel_names)):
            image_layer = new_viewer.add_image(
                self.stack[:, position, z, i, :, :].compute(),
                colormap=self.colors[i],
                opacity=self.opacities[i],
                name=self.channel_names[i],
            )
            image_layer._keep_auto_contrast = True

        def tmp_write_info(event):
            current_step = (new_viewer.dims.current_step[0], position, z)

            pos_name = self.chip_channel_names[position]
            channel_name = pos_name.split("-")[0]
            ch = self.exp_info.channel_infos[channel_name]

            texts = [
                pos_name
                + " had "
                + print_time_diff(antibiotic_exposure(ch))
                + " hours of abx duration"
            ]

            if ch.antibiotic:
                abx = ch.antibiotic
                texts.append(
                    f"{abx.name} ({abx.concentration:2.0f} {abx.concentration_unit})"
                )

            timefmt = "%Y-%m-%d %H-%M"

            durations = calc_times(
                current_step,
                self.chip_channel_names,
                self.exp_info,
                self.times,
            )

            if type(durations[0]) == TimeDiff:
                texts.append(
                    f"Current abx time:           {print_time_diff(durations[0])}"
                )
            else:
                texts.append("abx not started yet")

            if type(durations[1]) == TimeDiff:
                texts.append(
                    f"Current regrowth time: {print_time_diff(durations[1])}"
                )
            else:
                texts.append("regrowth not started yet")

            current_time = to_datetime(self.times[current_step])
            current_time = current_time.strftime(timefmt)
            texts.append(f"Current time: {current_time}")

            texts.append(
                f"Start time:      {ch.antibiotic_start.strftime(timefmt)}"
            )

            texts.append(
                f"End time:        {ch.antibiotic_end.strftime(timefmt)}"
            )

            text = "\n".join(texts)
            new_viewer.text_overlay.text = text

        new_viewer.text_overlay.visible = True
        new_viewer.text_overlay.font_size = 20
        new_viewer.text_overlay.color = "red"

        new_viewer.dims.events.current_step.connect(tmp_write_info)

    def _on_click(self):
        self.root = self.file_edit.value
        (
            nd2_files,
            xylen,
            mlen,
            zlen,
            self.channel_names,
        ) = get_nd2_files_in_folder(self.root)
        self.exp_info = get_exp_info(os.path.join(self.root, "exp-info.yaml"))

        imgs, times = [], []
        channel_names = []
        for nd2_file in nd2_files:
            img_, tmp_times_ = nd2_file_to_dask(
                nd2_file, zlen, self.channel_names, mlen, xylen
            )
            _, _, tmp_channel_names, sort_inds = get_position_names_and_inds(
                nd2_file,
                self.exp_info.general_info.invert_stage_x,
                self.exp_info.general_info.invert_stage_y,
            )
            img = img_[:, sort_inds, ...]
            # print(tmp_times_.shape)
            tmp_times = tmp_times_[:, sort_inds, ...]
            tested_tmp_times = test_nd2_timestamps(tmp_times, nd2_file)
            imgs.append(img)
            times.append(tested_tmp_times)
            channel_names.append(tmp_channel_names[sort_inds])

        self.times = np.concatenate(times, axis=0)
        # print(self.times.shape)
        stack = da.concatenate(imgs)
        print(stack.shape)
        self.stack = da.transpose(stack, (2, 0, 1, 3, 4, 5))

        self.colors = [color_from_name(cn) for cn in self.channel_names]
        self.opacities = [1,] + [
            0.6,
        ] * (len(self.colors) - 1)

        self.chip_channel_names = channel_names[0]

        self.viewer.text_overlay.visible = True
        self.viewer.text_overlay.font_size = 20
        self.viewer.text_overlay.color = "red"

        self.viewer.dims.events.current_step.connect(self.write_info)

        for i in range(len(self.channel_names)):
            image_layer = self.viewer.add_image(
                self.stack[..., i, :, :],
                colormap=self.colors[i],
                # opacity does not matter so much when using additive blending
                # opacity=self.opacities[i],
                blending="additive",
                name=self.channel_names[i],
            )
            # TODO: once https://github.com/napari/napari/issues/5402 is resolved
            # image_layer._keep_auto_contrast = True

        self.shape_layers = []
        for file_name, tmp_kwargs in self._shape_layer_info:
            kwargs = dict(
                opacity=0.7,
                edge_width=1.0,
                face_color="#ffffff00",
                # color and name are now in tmp_kwargs
                # edge_color=color,
                # name=name,
                # ndim is different for different layers
                # ndim=4,
            )
            kwargs.update(tmp_kwargs)

            try:
                layer = self.viewer.open(
                    os.path.join(self.root, file_name),
                    layer_type="shapes",
                    **kwargs,
                )[0]
            except FileNotFoundError:
                print(
                    f"no annotation present for {tmp_kwargs['name']}, creating empty shapes layer"
                )
                layer = self.viewer.add_shapes(None, **kwargs)
            self.shape_layers.append(layer)

        self.viewer.dims.axis_labels = ["z", "time", "position", "y", "x"]
        self.viewer.dims.set_current_step(0, 1)
        self.viewer.dims.set_current_step(1, 0)
        self.viewer.dims.set_current_step(2, 0)

    def _on_save_click(self):
        print(self.shape_layers)
        for layer, (file_name, _) in zip(
            self.shape_layers, self._shape_layer_info
        ):
            layer.save(os.path.join(self.root, file_name))

    def write_info(self, event):
        current_step = self.swap_axes_ztp_to_tpz(
            tuple(self.viewer.dims.current_step[:3])
        )
        position = current_step[1]
        # print(current_step)

        pos_name = self.chip_channel_names[position]
        channel_name = pos_name.split("-")[0]
        ch = self.exp_info.channel_infos[channel_name]

        texts = [
            pos_name
            + " had "
            + print_time_diff(antibiotic_exposure(ch))
            + " hours of abx duration"
        ]

        if ch.antibiotic:
            abx = ch.antibiotic
            texts.append(
                f"{abx.name} ({abx.concentration:2.0f} {abx.concentration_unit})"
            )

        timefmt = "%Y-%m-%d %H-%M"

        # print(self.times[:, current_step[1], 1])

        durations = calc_times(
            current_step,
            self.chip_channel_names,
            self.exp_info,
            self.times,
        )
        # print(durations)

        if type(durations[0]) == TimeDiff:
            texts.append(
                f"Current abx time:           {print_time_diff(durations[0])}"
            )
        else:
            texts.append("abx not started yet")

        if type(durations[1]) == TimeDiff:
            texts.append(
                f"Current regrowth time: {print_time_diff(durations[1])}"
            )
        else:
            texts.append("regrowth not started yet")

        current_time = to_datetime(self.times[current_step])
        current_time = current_time.strftime(timefmt)
        texts.append(f"Current time: {current_time}")

        texts.append(
            f"Start time:      {ch.antibiotic_start.strftime(timefmt)}"
        )

        texts.append(f"End time:        {ch.antibiotic_end.strftime(timefmt)}")

        text = "\n".join(texts)
        self.viewer.text_overlay.text = text

    def change_current_view_dead_biofilm(self, offset):
        # swap step axes: (z, time, pos) -> (pos, time, z)
        current_view = int(self.viewer.dims.current_step[2])
        shape_data = [int(pos[0, 0]) for pos in self.shape_layers[2].data]

        sorted_steps = sorted(list(set(shape_data + [current_view])))
        current_index = sorted_steps.index(current_view)
        new_index = (current_index + offset) % len(sorted_steps)
        # swap step axes back: (pos, time, z) -> (time, pos, z)
        print(current_view)
        new_view = sorted_steps[new_index]
        print(new_view)

        self.viewer.dims.set_current_step(2, new_view)

    def change_current_view(self, offset, layer=0):
        # swap step axes: (z, time, pos) -> (pos, time, z)
        current_view = (
            self.viewer.dims.current_step[2],
            self.viewer.dims.current_step[1],
        )
        shape_data = [
            (int(pos[0, 1]), int(pos[0, 0]))
            for pos in self.shape_layers[layer].data
        ]
        sorted_steps = sorted(list(set(shape_data + [current_view])))
        current_index = sorted_steps.index(current_view)
        new_index = (current_index + offset) % len(sorted_steps)
        # swap step axes back: (pos, time, z) -> (time, pos, z)
        print(current_view)
        new_view = sorted_steps[new_index][::-1]
        print(new_view)

        for i in range(2):
            self.viewer.dims.set_current_step(i + 1, new_view[i])

    def next_biofilm(self):
        self.change_current_view(1)

    def prev_biofilm(self):
        self.change_current_view(-1)

    def next_biofilm_single_cell(self):
        self.change_current_view(1, 1)

    def prev_biofilm_single_cell(self):
        self.change_current_view(-1, 1)

    def next_biofilm_dead(self):
        self.change_current_view_dead_biofilm(1)

    def prev_biofilm_dead(self):
        self.change_current_view_dead_biofilm(-1)

    def swap_axes_ztp_to_tpz(self, axes):
        return tuple(axes[i] for i in [1, 2, 0])

    def swap_axes_tpz_to_ztp(self, axes):
        return tuple(axes[i] for i in [2, 0, 1])
