from PySide6.QtWidgets import QTableWidget, QHeaderView
from widgets.model_row import ModelRow

from PySide6.QtGui import Qt


class ModelsTableWidget(QTableWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.models = []

        # dict to store the status of the detailed text for each model
        self.detailedTextVisible = {}
        self.setColumnCount(7)
        self.setHorizontalHeaderLabels(["", 'Category', 'Name', 'Version', 'Size', 'Links', ''])
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        self.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)

        self.verticalHeader().setVisible(False)

        self.setShowGrid(False)
        
        self.setStyleSheet("""
                           QTableWidget::item:selected{
                               color: #ffffff;
                               background-color: #red;
                               }""")

    def add_model(self, model: "ModelRow"):
        self.models.append(model)
        index = self.rowCount()
        # detailed text is not visible yet for the model
        self.detailedTextVisible[str(index)] = False
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
        # detailed text is visible for the model with the idx "index-1"
        self.detailedTextVisible[str(index - 1)] = True

    def deselect_model(self, model: ModelRow):
        index = self.models.index(model) * 2 + 1
        self.hideRow(index)
        # detailed text is not visible for the model with the idx "index-1"
        self.detailedTextVisible[str(index - 1)] = False

    def mouseDoubleClickEvent(self, event):
        # index for the current clicked model
        index       = self.indexAt(event.pos())
        # row which has to be made visible
        row         = index.row() + 1
        # index of the model stored in the self.models list
        idxModel    = int(index.row() / 2)
        
        # check if the correct row was clicked
        if str(row - 1) in self.detailedTextVisible:
            # if text is visible --> hide text
            if self.detailedTextVisible[str(row - 1)]:
                self.clearSelection()
                self.models[idxModel].collapse_button.setArrowType(Qt.ArrowType.RightArrow)
                self.hideRow(row)
                self.detailedTextVisible[str(row - 1)] = False
                
            # if text is not visible --> show text
            else:
                self.models[idxModel].collapse_button.setArrowType(Qt.ArrowType.DownArrow)
                self.showRow(row)
                self.detailedTextVisible[str(row - 1)] = True
