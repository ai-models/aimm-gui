from PyQt6 import QtWidgets, QtCore
from qt.model_row import Model_Row


class Scroll_area(QtWidgets.QScrollArea):
    """A QScrollArea object representing a 'scroll area' with its own appearance and logic.

    Args:
        main_object (QMainWindow): A QMainWindow object. Use to acces method of the main window.
    """

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self) -> None:
        """Init the UI of the object.
        """
        self.setWidgetResizable(True)
        self.content_holder = QtWidgets.QWidget()
        self.content_holder.setFixedHeight(0)

        self.content_holder_layout = QtWidgets.QVBoxLayout()
        self.content_holder_layout.setContentsMargins(0, 0, 0, 0)
        self.content_holder_layout.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTop)
        self.content_holder_layout.setSpacing(10)

        self.content_holder.setLayout(self.content_holder_layout)

        self.setWidget(self.content_holder)

    def add_row(self, row: Model_Row, update: bool = True):
        """Add a category to the layout.

        Args:
            category (Model_Row): The row that need to be added to the layout.
            update (bool): Does the height need to be updated or not.
        """
        self.content_holder_layout.addWidget(row)
        if update:
            self.update_height()

    def update_height(self):
        """Adjust the size of the object based on it's children
        """
        children_count = self.content_holder_layout.count()
        height = 10
        for index in range(children_count):
            child = self.content_holder_layout.itemAt(index).widget()
            # The +10 is for the spacing
            child_height = child.current_height+10
            height += child_height

        self.content_holder.setFixedHeight(height)

    def add_models(self, models: list[dict]):
        """Add rows based on a list of nodels.

        Args:
            models (list[dict]): The list of models
        """
        for model_info in models:
            row = Model_Row(self, model_info)
            self.add_row(row, False)
        self.update_height()
