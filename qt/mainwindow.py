from PyQt6 import QtWidgets, QtCore

from qt.scroll_area import Scroll_area
from qt.headers import Headers_Display
from qt.top_bar import Top_Bar


class Window(QtWidgets.QMainWindow):
    def __init__(self, json_handler):
        super().__init__()
        self.json_handler = json_handler
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Pons AI Model Manager")
        self.setMinimumSize(QtCore.QSize(1000, 600))

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        top_bar = Top_Bar()

        bottom_part = QtWidgets.QWidget()
        bottom_part_layout = QtWidgets.QVBoxLayout()
        bottom_part_layout.setSpacing(0)
        bottom_part.setLayout(bottom_part_layout)
        headers = Headers_Display()
        scroll = Scroll_area(self)

        models = self.json_handler.get_models()
        scroll.add_models(models)

        bottom_part_layout.addWidget(headers)
        bottom_part_layout.addWidget(scroll)
        self.main_layout.addWidget(top_bar)
        self.main_layout.addWidget(bottom_part)

        self.show()
