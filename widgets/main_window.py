from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDockWidget, QFrame

from logic import JsonHandler
from widgets.model_row import ModelRow
from widgets.models_table_widget import ModelsTableWidget
from widgets.top_bar import TopBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.json_handler = JsonHandler()

        self.setWindowTitle("Pons AI Model Manager")
        self.setMinimumSize(QSize(800, 400))

        central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.top_bar = TopBar()
        self.main_layout.addWidget(self.top_bar)

        self.models_widget = ModelsTableWidget(self)
        self.models_widget.add_models(self.json_handler.get_models())
        self.main_layout.addWidget(self.models_widget)
