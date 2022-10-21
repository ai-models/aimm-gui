from PySide6.QtWidgets import QTableWidget, QHeaderView
from widgets.model_row import ModelRow


class ModelsTableWidget(QTableWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.models = []
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["", 'Name', 'Description', 'Version', 'Size', 'Github', 'Install'])
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        self.verticalHeader().setVisible(False)

        self.setShowGrid(False)

    def add_model(self, model: "ModelRow"):
        self.models.append(model)
        index = self.rowCount()
        self.insertRow(index)
        for i, widget in enumerate(model.widgets):
            self.setCellWidget(index, i, widget)

        self.insertRow(index + 1)
        # Set row span
        self.setSpan(index + 1, 0, 1, 7)
        # Add the model info to the row
        self.setCellWidget(index + 1, 0, model.detailed_model)
        # Hide the row
        self.hideRow(index + 1)
        self.resizeRowToContents(index + 1)

    def add_models(self, models: list[dict]):
        for model_info in models:
            model = ModelRow(self, model_info)
            self.add_model(model)

        self.resizeColumnsToContents()

    def select_model(self, model: ModelRow):
        index = self.models.index(model) * 2 + 1
        self.showRow(index)

    def deselect_model(self, model: ModelRow):
        index = self.models.index(model) * 2 + 1
        self.hideRow(index)
