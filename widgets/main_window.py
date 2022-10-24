from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDockWidget, QFrame
from PySide6.QtGui import QIcon
from logic import JsonHandler
from widgets.model_row import ModelRow
from widgets.models_table_widget import ModelsTableWidget
from widgets.top_bar import TopBar

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'pons.aimodelmanager.subproduct.001'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.json_handler = JsonHandler()
        self.setWindowTitle("Pons AI Model Manager")
        self.setMinimumSize(QSize(800, 400))
        self.setWindowIcon(QIcon('icon/icon.png'))
        self.setStyleSheet("""
            QWidget {background-color: white;}
            QTableView {background-color: gray}
            QTableView {border-top: 0px; border-left: 0px; border-right: 0px;}
            QToolButton {border: 0px}
        """)

        central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.top_bar = TopBar()
        self.main_layout.addWidget(self.top_bar)

        self.models_widget = ModelsTableWidget(self)
        self.models_widget.add_models(self.json_handler.get_models())
        self.main_layout.addWidget(self.models_widget)
