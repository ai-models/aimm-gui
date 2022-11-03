from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView

from widgets.widget_table_model_row import ModelRow
from widgets.widget_table import TableWidget


class LibraryTableWidget(TableWidget):
    def __init__(self, main_window):
        super().__init__(main_window, 7)
        self.name = "LibraryTableWidget"

        self.setColumnCount(7)
        self.setHorizontalHeaderLabels(["", 'Category', 'Name', 'Version', 'Size', 'Path', ''])

        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)
        self.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive)
        self.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)

        self.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        self.horizontalHeaderItem(3).setTextAlignment(Qt.AlignRight)
        self.horizontalHeaderItem(4).setTextAlignment(Qt.AlignRight)
        self.horizontalHeaderItem(5).setTextAlignment(Qt.AlignLeft)

    def add_model(self, model: "ModelRow"):
        if not model.model_info["installed"]:
            return

        self.models.append(model)
        index = self.rowCount()
        # detailed text is not visible yet for the model
        self.detailedTextVisible[str(index)] = False
        self.insertRow(index)
        for i, widget in enumerate(model.library_widgets):
            self.setCellWidget(index, i, widget)

        self.insertRow(index + 1)
        # Set row span
        self.setSpan(index + 1, 0, 1, self.columnCount())
        # Add the model info to the row
        self.setCellWidget(index + 1, 0, model.detailed_widget)
        # Hide the row
        self.hideRow(index + 1)
        self.resizeRowToContents(index + 1)

    def install_model(self, model: ModelRow):
        model.model_info["installed"] = True
        new_model = ModelRow(self.main_window, self, model.model_info)
        self.add_model(new_model)

    def __repr__(self):
        return "LibraryTableWidget"
