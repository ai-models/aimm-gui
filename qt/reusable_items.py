from PyQt6 import QtWidgets, QtCore, QtGui


class H_Holder(QtWidgets.QWidget):
    def __init__(self, children=None, alignment=QtCore.Qt.AlignmentFlag.AlignLeft) -> None:
        super().__init__()
        self.lay = QtWidgets.QHBoxLayout()
        self.lay.setAlignment(alignment)
        self.setLayout(self.lay)
        self.addWidget(children)

    def addWidget(self, children):
        if children is None:
            return
        if isinstance(children, list) or isinstance(children, tuple):
            for child in children:
                self.lay.addWidget(child)
        else:
            self.lay.addWidget(children)


class Vertical_Rule(QtWidgets.QLabel):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedWidth(1)
        border_color = self.palette().dark().color().name()
        self.setStyleSheet(f'background:{border_color}')


class Button(QtWidgets.QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedHeight(30)
