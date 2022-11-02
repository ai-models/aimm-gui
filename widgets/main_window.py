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
        self.setWindowTitle("AI Model Manager")
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

        self.models = self.json_handler.get_models()
        self.categories = set(m["category"] for m in self.models)
        self.top_bar.update_categories(self.categories)

        self.add_model_table_widget = AddModelTableWidget(self)
        self.library_table_widget = LibraryTableWidget(self)

        self.library_table_widget.add_models(self.models)
        self.add_model_table_widget.add_models(self.models)

        self.table_layout.addWidget(self.library_table_widget)
        self.table_layout.addWidget(self.add_model_table_widget)

        self.library_table_widget.resizeColumnToContents(4)
        self.library_table_widget.resizeColumnToContents(5)
        self.library_table_widget.resizeColumnToContents(6)
        self.add_model_table_widget.resizeColumnToContents(2)
        self.add_model_table_widget.resizeColumnToContents(6)

        self.top_bar.search.textChanged.connect(self.update_filter)
        self.top_bar.categories.currentTextChanged.connect(self.update_filter)

        self.placeholder_widget = QLabel("TO DO")
        self.table_layout.addWidget(self.placeholder_widget)

    def update_filter(self):
        category = self.top_bar.categories.currentText().lower()
        search = self.top_bar.search.text().lower()
        self.add_model_table_widget.filter(category, search)
        self.library_table_widget.filter(category, search)
