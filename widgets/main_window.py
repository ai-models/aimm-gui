from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDockWidget, QFrame
from PySide6.QtGui import QIcon, QFont
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
    self.setMinimumSize(QSize(600, 300))
    self.setWindowIcon(QIcon('icon/icon.png'))
    self.setContentsMargins(0, 0, 0, 0)
    self.setStyleSheet("""
            QTableView::item:selected {
                background-color: #c5f5fe;
                border: 0;
                }
            QTableView::item:focus {
                background-color: #c5f5fe;
                border: 0;
                }
            QTableView::row:hover {
                background-color: #d0d0d0;
                border: 0;
                }
            QTableView {background-color: white; border: 0;}
            QTableView QHeaderView {border: 0 solid #f0f0f0; background: #f0f0f0;}
            QTableView QToolButton {border: 0px}
            QTableView QPushButton {margin: 3px; background-color: #ffffff;}
            QTableWidget {
                qproperty-showGrid: "false";
            }
        """)

    central_widget = QWidget()
    self.main_layout = QVBoxLayout()
    central_widget.setLayout(self.main_layout)
    font = QFont('Serif', 11, QFont.Weight.Light)
    central_widget.setFont(font)
    self.setCentralWidget(central_widget)

    self.top_bar = TopBar()
    self.main_layout.addWidget(self.top_bar)

    self.models_widget = ModelsTableWidget(self)
    self.models_widget.add_models(self.json_handler.get_models())
    self.main_layout.addWidget(self.models_widget)
