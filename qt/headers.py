from PyQt6 import QtWidgets, QtCore, QtGui

from qt.reusable_items import Vertical_Rule


class Header(QtWidgets.QLabel):
    def __init__(self, text: str, width: int, alignment) -> None:
        super().__init__(text=text)
        self.setMinimumWidth(width)
        font = QtGui.QFont()
        font.setWeight(700)
        self.setFont(font)
        self.setAlignment(alignment)


class Headers_Display(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QtWidgets.QHBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        main_layout.setContentsMargins(0, 0, 0, 0)

        space = QtWidgets.QWidget()
        space.setFixedWidth(25)

        category = Header("Category", 160, QtCore.Qt.AlignmentFlag.AlignLeft)
        rule1 = Vertical_Rule()
        name = Header("Name", 160, QtCore.Qt.AlignmentFlag.AlignLeft)
        rule2 = Vertical_Rule()
        version = Header("Version", 80, QtCore.Qt.AlignmentFlag.AlignRight)
        rule3 = Vertical_Rule()
        size = Header("Size", 70, QtCore.Qt.AlignmentFlag.AlignRight)
        rule4 = Vertical_Rule()

        links = Header("Links", 100, QtCore.Qt.AlignmentFlag.AlignLeft)

        main_layout.addWidget(space)
        main_layout.addWidget(category)
        main_layout.addWidget(rule1)
        main_layout.addWidget(name)
        main_layout.addWidget(rule2)
        main_layout.addWidget(version)
        main_layout.addWidget(rule3)
        main_layout.addWidget(size)
        main_layout.addWidget(rule4)
        main_layout.addWidget(links)

        self.setLayout(main_layout)
