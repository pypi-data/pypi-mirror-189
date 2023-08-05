import numpy as np
from PIL import ImageQt
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, Qt, QSize, pyqtSlot
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from primawera.HighlightScrollArea import HighlightScrollArea


class Visualiser(QWidget):
    signal_position = pyqtSignal(int, int, int, list)
    value_change_emitter_vertical = pyqtSignal(int)
    value_change_emitter_horizontal = pyqtSignal(int)

    def __init__(self, data, axes_orientation, mode, maximum_height,
                 maximum_width, main_window, *args,
                 **kwargs):
        super(Visualiser, self).__init__(*args, **kwargs)
        self.axes_orientation = None
        self.data = None
        self.mode = None
        self.height = 0
        self.width = 0
        self.frames = 0
        self.frame = 0
        self.pixmaps = None
        self.main_window = main_window

        self.MAXIMUM_HEIGHT = maximum_height
        self.MAXIMUM_WIDTH = maximum_width
        self.ZOOMED_MAX_SIZE = 32000

        self.zoom_level = 1
        self.update_data(data, axes_orientation, mode)

        # Set up label
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignLeft)
        self.setContentsMargins(0, 0, 0, 0)

        # Set up scroll area
        self.scroll_area = HighlightScrollArea()
        self.scroll_area.setBackgroundRole(QPalette.Dark)
        self.scroll_area.setWidget(self.label)
        self.scroll_area.setAlignment(Qt.AlignLeft)

        # Set up layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll_area)
        self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)

        # Set up event handling
        self.label.mousePressEvent = self.get_position
        self.connect_horizontal_bar()
        self.connect_vertical_bar()

        # Set up focus in/out border change
        # self.focusChanged.connect(self.focus_changed)

    def connect_vertical_bar(self):
        self.get_vertical_bar().valueChanged.connect(
            self._value_change_wrapper_vertical)

    def connect_horizontal_bar(self):
        self.get_horizontal_bar().valueChanged.connect(
            self._value_change_wrapper_horizontal)

    def update_data(self, data, axes_orientation, mode):
        # Prepare the data
        # NOTE: Without copy() the program may receive SIGSEV.
        self.axes_orientation = axes_orientation
        self.mode = mode
        if self.mode == "rgb":
            axes_orientation = axes_orientation[0], axes_orientation[1], \
                axes_orientation[2], 3
        self.data = np.transpose(data, axes_orientation).copy()
        self.frames, self.height, self.width = self.data.shape[0], \
            self.data.shape[1], \
            self.data.shape[2]
        self.frame = 0
        self.pixmaps = []

    def generate(self):
        self._generate()

    def redraw(self):
        self.choose_frame(self.frame)

    def get_position(self, event):
        event_x = event.pos().x()
        event_y = event.pos().y()
        pixmap_height = self.label.pixmap().size().height()
        pixmap_width = self.label.pixmap().size().width()
        if event_x >= pixmap_width or event_y > pixmap_height:
            # User clicked outside of the QPixmap (but inside the QLabel
            # container)
            return

        if self.mode in {"grayscale", "1", "F", "C"}:
            _, data_rows, data_cols = self.data.shape
        else:
            _, data_rows, data_cols, _ = self.data.shape
        position_x = int((event_x / pixmap_width) * data_cols)
        position_y = int((event_y / pixmap_height) * data_rows)

        # Now take into account the transposition of the data
        transposed_coords = [self.frame, position_y, position_x]
        real_frame = transposed_coords[self.axes_orientation.index(0)]
        real_x = transposed_coords[self.axes_orientation.index(1)]
        real_y = transposed_coords[self.axes_orientation.index(2)]

        # Note: numpy is row-centric, that's why y and x are switched
        mapped_value = [self.data[self.frame, position_y, position_x]]
        self.signal_position.emit(real_frame, real_x, real_y, mapped_value)

    def _generate(self):
        for i in range(self.frames):
            if self.mode in {"grayscale", "1", "F", "C"}:
                qimage = ImageQt.QImage(self.data[i, :, :], self.width,
                                        self.height,
                                        self.width, QImage.Format_Grayscale8)
            elif self.mode == "rgb":
                qimage = ImageQt.QImage(self.data[i, :, :], self.width,
                                        self.height,
                                        3 * self.width, QImage.Format_RGB888)
            else:
                raise RuntimeError(
                    f"Combination of mode='{self.mode}' not supported.")
            self.pixmaps.append(QPixmap.fromImage(qimage))

    def choose_frame(self, frame: int) -> None:
        if frame < 0 or frame >= self.frames:
            return
        self.frame = frame

        # Calculate the right size of the image label
        zoomed_width = self.width * self.zoom_level
        zoomed_height = self.height * self.zoom_level
        resized_pixmap = self.pixmaps[self.frame].scaled(
            QSize(zoomed_width, zoomed_height),
            Qt.KeepAspectRatio)

        # Calculate the size of the container QLabel.
        label_width = min(zoomed_width, self.MAXIMUM_WIDTH)
        label_height = min(zoomed_height, self.MAXIMUM_HEIGHT)

        # Update the container's size
        self.label.setMinimumSize(zoomed_width, zoomed_height)
        self.label.setMaximumSize(zoomed_width, zoomed_height)

        height, width = label_height + 20, label_width + 20

        # Hide the scrollbars
        self.scroll_area.horizontalScrollBar().setStyleSheet(
            "QScrollBar {height:0px;}")
        self.scroll_area.verticalScrollBar().setStyleSheet(
            "QScrollBar {width:0px;}")

        # If the image is too big, show the scrollbars only in the main wind.
        if label_width >= self.MAXIMUM_WIDTH:
            if self.main_window:
                # This is to accomodate the size of the scrollbars
                self.scroll_area.horizontalScrollBar().setStyleSheet(
                    "QScrollBar {height:10px;}")
                height += 10
        if label_height >= self.MAXIMUM_HEIGHT:
            if self.main_window:
                self.scroll_area.verticalScrollBar().setStyleSheet(
                    "QScrollBar {width:10px;}")
                width += 10

        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)

        # Update the pixmap
        self.label.setPixmap(resized_pixmap)

    def next_frame(self) -> None:
        self.choose_frame(self.frame + 1)

    def previous_frame(self) -> None:
        self.choose_frame(self.frame - 1)

    def resizeEvent(self, event) -> None:
        self.choose_frame(self.frame)

    def decrease_zoom_level(self) -> None:
        self.zoom_level = max(self.zoom_level // 2, 1)
        self.choose_frame(self.frame)

    def increase_zoom_level(self) -> None:
        size = max(self.width, self.height) * self.zoom_level
        if size * 2 <= self.ZOOMED_MAX_SIZE:
            self.zoom_level = self.zoom_level * 2
            self.choose_frame(self.frame)

    def get_horizontal_bar(self):
        return self.scroll_area.horizontalScrollBar()

    def get_vertical_bar(self):
        return self.scroll_area.verticalScrollBar()

    def get_scroll_area(self):
        return self.scroll_area

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_N:
            self.next_frame()
        elif event.key() == QtCore.Qt.Key_P:
            self.previous_frame()
        else:
            event.ignore()

    @pyqtSlot(int)
    def _value_change_wrapper_horizontal(self, value: int):
        if self.scroll_area.in_focus():
            self.value_change_emitter_horizontal.emit(value)

    @pyqtSlot(int)
    def _value_change_wrapper_vertical(self, value: int):
        if self.scroll_area.in_focus():
            self.value_change_emitter_vertical.emit(value)
