from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QComboBox, QLineEdit


class TopBar(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        library_button = QPushButton("Library")
        library_button.clicked.connect(lambda: self.go_to_tab(0))
        self.main_layout.addWidget(library_button)

        add_model_button = QPushButton("Add Model")
        add_model_button.clicked.connect(lambda: self.go_to_tab(1))
        self.main_layout.addWidget(add_model_button)

        self.add_custom_button = QPushButton("Add Custom")
        self.add_custom_button.setObjectName("green_button")
        self.add_custom_button.clicked.connect(lambda: self.go_to_tab(2))
        self.main_layout.addWidget(self.add_custom_button)
        self.add_custom_button.hide()

        self.main_layout.addStretch()

        dropdown = QComboBox()
        dropdown.setFixedWidth(160)
        dropdown.setEditable(True)
        dropdown.lineEdit().setPlaceholderText("Categories")
        dropdown.setStyleSheet(f"border:0px solid transparent;border-bottom:1px solid #a0a0a0;background:transparent")
        self.main_layout.addWidget(dropdown)

        search_bar = QLineEdit()
        search_bar.setFixedWidth(160)
        search_bar.setPlaceholderText("Search")
        search_bar.setStyleSheet(f"border:0px solid transparent;border-bottom:1px solid #a0a0a0;background:transparent")
        self.main_layout.addWidget(search_bar)

    def go_to_tab(self, tab: int):
        self.main_window.table_layout.setCurrentIndex(tab)
        if tab in (1, 2):
            self.add_custom_button.show()
        else:
            self.add_custom_button.hide()
