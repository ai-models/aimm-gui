import os

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
from logic import JsonHandler
from widgets.models_table_widget import ModelsTableWidget
from widgets.top_bar import TopBar

basedir = os.path.dirname(__file__)

basedir_icons = os.path.dirname(__file__) + "\..\icons\\"

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

    ## Window
    self.setContentsMargins(0, 0, 0, 0)
    self.setStyleSheet("""
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
    self.setCentralWidget(central_widget)

    self.top_bar = TopBar()
    self.main_layout.addWidget(self.top_bar)

    self.models_widget = ModelsTableWidget(self)
    self.models_widget.add_models(self.json_handler.get_models())
    self.main_layout.addWidget(self.models_widget)

    ## Icons
    self.setWindowIcon(QIcon(os.path.join(basedir_icons, 'icon.png')))



