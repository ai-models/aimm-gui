from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView

from widgets.model_row import ModelRow
from widgets.table_widget import TableWidget


class AddModelTableWidget(TableWidget):
    def __init__(self, main_window):
        super().__init__(main_window, 7)
        self.name = "AddModelTableWidget"

        self.setColumnCount(7)
        self.setHorizontalHeaderLabels(['', 'Category', 'Name', 'Version', 'Size', 'Links', ''])

        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(4, QHeaderView.Interactive)
        self.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(6, QHeaderView.Fixed)

        self.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        self.horizontalHeaderItem(3).setTextAlignment(Qt.AlignRight)
        self.horizontalHeaderItem(4).setTextAlignment(Qt.AlignRight)
        self.horizontalHeaderItem(5).setTextAlignment(Qt.AlignLeft)

    def add_model(self, model: ModelRow):
        self.models.append(model)
        index = self.rowCount()
        # detailed text is not visible yet for the model
        self.detailedTextVisible[str(index)] = False
        self.insertRow(index)
        for i, widget in enumerate(model.add_model_widgets):
            self.setCellWidget(index, i, widget)

        self.insertRow(index + 1)
        # Set row span
        self.setSpan(index + 1, 0, 1, self.columnCount())
        # Add the model info to the row
        self.setCellWidget(index + 1, 0, model.detailed_widget)
        # Hide the row
        self.hideRow(index + 1)
        self.resizeRowToContents(index + 1)

    def __repr__(self):
        return "AddModelTableWidget"
