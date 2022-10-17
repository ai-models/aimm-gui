from PyQt6 import QtWidgets


class Top_Bar(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self):
        palette = self.palette()
        main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(main_layout)

        library_button = QtWidgets.QPushButton("Library")
        add_model_button = QtWidgets.QPushButton("Add Model")
        add_custom_button = QtWidgets.QPushButton("Add Custom")

        spacer = QtWidgets.QLabel()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                             QtWidgets.QSizePolicy.Policy.Preferred)
        dropdown = QtWidgets.QComboBox()
        dropdown.setMinimumWidth(160)
        # comboBox.addItems([])
        # dropdown.activated.connect()
        dropdown.setEditable(True)
        dropdown.lineEdit().setPlaceholderText("Categories")
        border_color = palette.dark().color().name()
        dropdown.setStyleSheet(
            f'border:0px solid transparent;border-bottom:1px solid {border_color};background:transparent')
        dropdown.setFixedHeight(24)

        search_bar = QtWidgets.QLineEdit()
        search_bar.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum,
                                 QtWidgets.QSizePolicy.Policy.Fixed)
        search_bar.setMinimumWidth(160)
        search_bar.setPlaceholderText("Search")

        search_bar.setStyleSheet(
            f'border:0px solid transparent;border-bottom:1px solid {border_color};background:transparent')
        search_bar.setFixedHeight(24)

        main_layout.addWidget(library_button)
        main_layout.addWidget(add_model_button)
        main_layout.addWidget(add_custom_button)
        main_layout.addWidget(spacer)
        main_layout.addWidget(dropdown)
        main_layout.addWidget(search_bar)
