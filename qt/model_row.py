from PyQt6 import QtWidgets, QtCore, QtGui
from qt.reusable_items import H_Holder


class Model_Info(QtWidgets.QLabel):
    """A custom QLabel

    Args:
        text (str): The displayed text
        width (int): The minimum width
        alignment (AlignmentFlag): The alignment 
    """

    def __init__(self, text: str, width: int, alignment) -> None:
        super().__init__(text=text)
        self.setMinimumWidth(width)
        self.setAlignment(alignment)


class Fixed_Part(H_Holder):
    def __init__(self, row, children=None, alignment=QtCore.Qt.AlignmentFlag.AlignLeft) -> None:
        super().__init__(children, alignment)
        self.row = row
        self.init_ui()

    def init_ui(self):
        self.lay.setSpacing(5)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.arrow_button = QtWidgets.QToolButton()
        self.arrow_button.setArrowType(QtCore.Qt.ArrowType.RightArrow)
        self.arrow_button.setStyleSheet("QToolButton { border: none; }")
        self.arrow_button.clicked.connect(self.row.handle_click)
        self.arrow_button.setFixedHeight(15)
        self.arrow_button.setFixedWidth(15)

        category = Model_Info(
            self.row.model_info["category"], 168, QtCore.Qt.AlignmentFlag.AlignLeft)

        name = Model_Info(
            self.row.model_info["name"], 168, QtCore.Qt.AlignmentFlag.AlignLeft)
        name.setWordWrap(True)

        version = Model_Info(
            self.row.model_info["version"], 83, QtCore.Qt.AlignmentFlag.AlignRight)

        size = Model_Info(
            self.row.model_info["size"], 83, QtCore.Qt.AlignmentFlag.AlignRight)

        displayed_link = f'<a href={self.row.model_info["github_url"]}>Github</a>'
        link = Model_Info(displayed_link, 170,
                          QtCore.Qt.AlignmentFlag.AlignLeft)
        link.linkActivated.connect(self.row.open_link)

        install_button = QtWidgets.QPushButton("Install")
        install_button.clicked.connect(
            lambda: self.row.open_link(self.row.model_info["download_url"]))
        color = self.palette().button().color().name()
        install_button.setStyleSheet(f'background:{color}')

        install_holder = H_Holder(
            install_button, QtCore.Qt.AlignmentFlag.AlignRight)
        install_holder.lay.setContentsMargins(0, 0, 0, 0)

        install_holder.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.addWidget(
            (self.arrow_button, category, name, version, size, link, install_holder))


class Extended_Part(H_Holder):
    def __init__(self, row, children=None, alignment=QtCore.Qt.AlignmentFlag.AlignLeft) -> None:
        super().__init__(children, alignment)
        self.row = row
        self.init_ui()

    def init_ui(self):
        self.lay.setContentsMargins(0, 0, 0, 0)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        description = Model_Info(
            self.row.model_info["description"], 400, QtCore.Qt.AlignmentFlag.AlignLeft)
        description.setWordWrap(True)

        space = QtWidgets.QWidget()
        space.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                            QtWidgets.QSizePolicy.Policy.Minimum)

        checksum_zone = H_Holder(alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        checksum = Model_Info(
            f'Checksum: {self.row.model_info["md5"]}', 200, QtCore.Qt.AlignmentFlag.AlignLeft)
        copy_button = QtWidgets.QPushButton("🗊")
        copy_button.setFixedSize(20, 20)
        color = self.palette().button().color().name()
        copy_button.setStyleSheet(f'background:{color}')
        checksum_zone.addWidget((checksum, copy_button))

        self.addWidget((description, space, checksum_zone))


class Model_Row(QtWidgets.QLabel):
    """A custom QWidget representing a 'category' with its own appearance and logic.

    Args:
        main_window (QMainWindow): The main window.
        scroll_area (Scroll_area): The scroll area of the main window.
        title (str): A string representing the title of this category.
    """

    def __init__(self, scroll_area, model_info: dict) -> None:
        super().__init__()
        self.scroll_area = scroll_area
        self.model_info = model_info
        self.is_expanded = False
        self.current_height = 60
        self.init_ui()

    def init_ui(self):
        """Init the UI of the object
        """
        self.setFixedHeight(self.current_height)
        lay = QtWidgets.QGridLayout()
        lay.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        lay.setContentsMargins(0, 0, 0, 0)

        self.fixed_area = Fixed_Part(self)
        self.extended_area = Extended_Part(self)
        # At the start, this part is hidden because is maximum height is set to 0
        self.extended_area.setMaximumHeight(0)

        lay.addWidget(self.fixed_area, 0, 0, 1, 1)
        lay.addWidget(self.extended_area, 1, 0, 1, 1)

        self.setLayout(lay)

    def open_link(self, linkStr):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(linkStr))

    def handle_height(self):
        """Adjust the size of the object based on the 'is_expanded' variable
        """
        # We assume that the task_area is not expanded
        task_area_height = 0
        # If it is, we need its height
        if self.is_expanded:
            task_area_height = 34

        # We adjust the height of the task_area
        self.extended_area.setMaximumHeight(task_area_height)
        # We update the current height (used in the scroll_area)
        self.current_height = task_area_height+60
        # We make the scroll_area adjust its height accordingly
        self.scroll_area.update_height()
        self.setFixedHeight(self.current_height)

    def handle_click(self):
        """Handle the click of the button/row
        """
        self.is_expanded = not self.is_expanded
        if self.is_expanded:
            self.fixed_area.arrow_button.setArrowType(
                QtCore.Qt.ArrowType.DownArrow)
            color = self.palette().highlight().color().name()
            self.setStyleSheet(f'background:{color}')

        else:
            self.fixed_area.arrow_button.setArrowType(
                QtCore.Qt.ArrowType.RightArrow)
            self.setStyleSheet("background:transparent")
        self.handle_height()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """A modification of the built in mousePressEvent
        """
        self.handle_click()
        return super().mousePressEvent(event)
