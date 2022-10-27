import os
import sys
from pathlib import Path
from typing import Union

from PySide6 import QtCore
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, QEvent
from PySide6.QtWidgets import QTableWidget, QStyledItemDelegate, QStyleOptionViewItem
from PySide6.QtGui import Qt, QPixmap, QMouseEvent, QColor
from widgets.model_row import ModelRow


bundle_dir = Path(getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__))))


class HoverDelegate(QStyledItemDelegate):
    def initStyleOption(self, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]):
        super().initStyleOption(option, index)
        option.backgroundBrush = QColor("#e7e7e7")


class SelectionDelegate(QStyledItemDelegate):
    def initStyleOption(self, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]):
        super().initStyleOption(option, index)
        # Light blue
        option.backgroundBrush = QColor("#c5f5fe")


class TableWidget(QTableWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.models = []

        # dict to store the status of the detailed text for each model
        self.detailedTextVisible = {}
        self.setSelectionMode(QTableWidget.NoSelection)

        self.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.horizontalHeader().setHighlightSections(False)

        self.verticalHeader().setVisible(False)
        self.setFocusPolicy(Qt.NoFocus)
        self.setShowGrid(False)

        self.setMouseTracking(True)
        self.hovering_row = None
        self.selected_row = None

        self.hover_delegate = HoverDelegate()
        self.selection_delegate = SelectionDelegate()

    def show_model(self, model: ModelRow):
        index = self.models.index(model) * 2 + 1
        self.showRow(index)
        # detailed text is visible for the model with the idx "index-1"
        self.detailedTextVisible[str(index - 1)] = True

    def hide_model(self, model: ModelRow):
        index = self.models.index(model) * 2 + 1
        self.hideRow(index)
        # detailed text is not visible for the model with the idx "index-1"
        self.detailedTextVisible[str(index - 1)] = False

    def mouseDoubleClickEvent(self, event):
        # index for the current clicked model
        index = self.indexAt(event.pos())
        # row which has to be made visible
        row = index.row() + 1
        # index of the model stored in the self.models list
        idxModel = int(index.row() / 2)

        # check if the correct row was clicked
        if str(row - 1) not in self.detailedTextVisible:
            return

        # if text is visible --> hide text
        if self.detailedTextVisible[str(row - 1)]:
            self.clearSelection()
            self.models[idxModel].collapse_button.setIcon(QPixmap("icons/right_arrow.png"))
            self.hideRow(row)
            self.detailedTextVisible[str(row - 1)] = False

        # if text is not visible --> show text
        else:
            self.models[idxModel].collapse_button.setIcon(QPixmap("icons/down_arrow.png"))
            self.showRow(row)
            self.detailedTextVisible[str(row - 1)] = True

    def mousePressEvent(self, event: QMouseEvent):
        row = self.indexAt(event.pos()).row()
        if row == -1:
            return

        if row % 2 == 1 and row - 1 == self.selected_row:
            return

        if row % 2 == 0 and row + 1 == self.selected_row:
            return

        self.select_row(row)

    def select_row(self, row: int):
        self.unselect_row()
        self.selected_row = row

        if row % 2 == 0 and row + 1 == self.selected_row:
            return

        if row % 2 == 1 and row - 1 == self.selected_row:
            return

        # Select both rows
        self.setItemDelegateForRow(row, self.selection_delegate)
        if row % 2 == 0:
            self.setItemDelegateForRow(row + 1, self.selection_delegate)
        else:
            self.setItemDelegateForRow(row - 1, self.selection_delegate)

    def unselect_row(self):
        if self.selected_row is None:
            return
        if self.selected_row % 2 == 0:
            self.setItemDelegateForRow(self.selected_row + 1, None)
        else:
            self.setItemDelegateForRow(self.selected_row - 1, None)
        self.setItemDelegateForRow(self.selected_row, None)

    def mouseMoveEvent(self, event: QMouseEvent):
        row = self.indexAt(event.pos()).row()
        if row == -1:
            return

        if row % 2 == 1 and row - 1 == self.selected_row:
            return

        if row % 2 == 0 and row + 1 == self.selected_row:
            return

        self.hover_row(row)

    def leaveEvent(self, event: QEvent):
        self.clear_hover()

    def hover_row(self, row: int):
        self.clear_hover()
        self.hovering_row = row

        if self.hovering_row == self.selected_row:
            return

        if self.hovering_row % 2 == 0 and self.hovering_row + 1 == self.selected_row:
            return
        if self.hovering_row % 2 == 1 and self.hovering_row - 1 == self.selected_row:
            return

        # Hover the rows
        self.setItemDelegateForRow(row, self.hover_delegate)
        if row % 2 == 0:
            self.setItemDelegateForRow(row + 1, self.hover_delegate)
        else:
            self.setItemDelegateForRow(row - 1, self.hover_delegate)

    def clear_hover(self):
        if self.hovering_row is None:
            return

        if self.hovering_row == self.selected_row:
            return

        self.setItemDelegateForRow(self.hovering_row, None)
        if self.hovering_row % 2 == 0:
            self.setItemDelegateForRow(self.hovering_row + 1, None)
        else:
            self.setItemDelegateForRow(self.hovering_row - 1, None)
        self.hovering_row = None
