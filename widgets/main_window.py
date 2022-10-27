from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedLayout, QLabel, QSizePolicy
from PySide6.QtGui import QIcon
from logic import JsonHandler
from widgets.library_table_widget import LibraryTableWidget
from widgets.add_model_table_widget import AddModelTableWidget
from widgets.top_bar import TopBar

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "pons.aimodelmanager.subproduct.001"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.json_handler = JsonHandler()
        self.setWindowTitle("Pons AI Model Manager")
        self.setWindowIcon(QIcon("icons/icon.png"))

        central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.top_bar = TopBar(self)
        self.main_layout.addWidget(self.top_bar)

        self.table_layout = QStackedLayout()
        self.main_layout.addLayout(self.table_layout)

        self.models_widget = LibraryTableWidget(self)
        self.table_layout.addWidget(self.models_widget)

        self.add_model_table_widget = AddModelTableWidget(self)
        self.add_model_table_widget.add_models(self.json_handler.get_models())
        self.table_layout.addWidget(self.add_model_table_widget)


        self.add_model_table_widget.setColumnWidth(2, 140)
        self.add_model_table_widget.resizeColumnToContents(3)
        self.add_model_table_widget.resizeColumnToContents(4)

        self.placeholder_widget = QLabel("TO DO")
        self.table_layout.addWidget(self.placeholder_widget)
