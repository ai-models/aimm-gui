import os
import sys
from abc import abstractmethod
from pathlib import Path
from typing import Union

from PySide6 import QtCore
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, QEvent, QRect
from PySide6.QtWidgets import QTableWidget, QStyledItemDelegate, QStyleOptionViewItem, QHeaderView
from PySide6.QtGui import Qt, QPixmap, QMouseEvent, QColor, QPainter
from widgets.model_row import ModelRow


bundle_dir = Path(getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__))))


class HoverDelegate(QStyledItemDelegate):
    def initStyleOption(self, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]):
        super().initStyleOption(option, index)
        # Dark gray
        option.backgroundBrush = QColor("#e7e7e7")


class SelectionDelegate(QStyledItemDelegate):
    def initStyleOption(self, option: QStyleOptionViewItem, index: Union[QModelIndex, QPersistentModelIndex]):
        super().initStyleOption(option, index)
        # Light blue
        option.backgroundBrush = QColor("#c5f5fe")


class Header(QHeaderView):
    def __init__(self, columns: int):
        super().__init__(Qt.Horizontal)
        self.columns = columns
        self.setDefaultAlignment(Qt.AlignLeft)
        self.setHighlightSections(False)

    def paintSection(self, painter: QPainter, rect: QRect, logical_index: int):

        self.draw_text(painter, logical_index, rect)

        # Draw vertical line
        painter.setPen(QColor("darkgray"))
        if logical_index not in (0, self.columns - 2):
            adjusted_rect = self.adjusted_rect(rect, self.get_alignment(logical_index))
            painter.drawLine(rect.right(), adjusted_rect.top(), rect.right(), adjusted_rect.bottom())
        # Draw bottom line
        painter.drawLine(rect.left(), rect.bottom(), rect.right(), rect.bottom())

    def get_alignment(self, index: int):
        align = self.model().headerData(index, Qt.Horizontal, Qt.TextAlignmentRole)
        if align is None:
            align = self.defaultAlignment()
        return align

    def draw_text(self, painter: QPainter, index: int, rect):
        align = self.get_alignment(index)
        text = self.model().headerData(index, Qt.Horizontal)
        adjusted_rect = self.adjusted_rect(rect, align)
        painter.drawText(adjusted_rect, align, text)

    @staticmethod
    def adjusted_rect(rect: QRect, align: Qt.Alignment):
        if align == Qt.AlignLeft:
            return rect.adjusted(8, 2, 0, 0)
        elif align == Qt.AlignRight:
            return rect.adjusted(-8, 2, -8, 0)
        elif align == Qt.AlignCenter:
            return rect.adjusted(8, 2, 8, 0)


class TableWidget(QTableWidget):
    def __init__(self, main_window, columns: int):
        super().__init__()
        self.main_window = main_window
        self.models: list[ModelRow] = []

        # dict to store the status of the detailed text for each model
        self.detailedTextVisible = {}
        self.setSelectionMode(QTableWidget.NoSelection)

        self.setHorizontalHeader(Header(columns))

        self.verticalHeader().setVisible(False)

        self.setFocusPolicy(Qt.NoFocus)
        self.setShowGrid(False)

        self.setMouseTracking(True)
        self.hovering_row = None
        self.selected_row = None

        self.hover_delegate = HoverDelegate()
        self.selection_delegate = SelectionDelegate()

    def filter(self, category: str, search_string: str):
        self.clearSelection()
        self.unselect_row()
        self.clear_hover()

        assert self.rowCount() % 2 == 0

        for i in range(self.rowCount()):
            self.hideRow(i)
            self.hideRow(i + 1)

        for i in range(self.rowCount() // 2):
            self.models[i].collapse_button.setIcon(QPixmap("icons/right_arrow.png"))
            self.detailedTextVisible[str(i)] = False

        for row in range(self.rowCount() // 2):
            model = self.models[row]

            if not (category in model.category.lower() or not category):
                continue

            if not (
                search_string in model.name.lower() or search_string in model.description.lower() or not search_string
            ):
                continue

            self.showRow(row * 2)

    def add_models(self, models: list[dict]):
        for model_info in models:
            model = ModelRow(self.main_window, self, model_info)
            self.add_model(model)

    @abstractmethod
    def add_model(self, model: "ModelRow"):
        pass

    def delete_model(self, model: ModelRow):
        for i, m in enumerate(self.models):
            if m.model_info["name"] == model.model_info["name"]:
                index = i
                self.models.pop(index)
                break
        else:
            raise RuntimeError("Model not found")
        self.removeRow(index * 2 + 1)
        self.removeRow(index * 2)

    def find_correspondent_model(self, model: ModelRow):
        for i, m in enumerate(self.models):
            if m.model_info["name"] == model.model_info["name"]:
                return m
        raise RuntimeError("Model not found")

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
        self.selected_row = None

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
