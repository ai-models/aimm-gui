from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QComboBox, QLineEdit


class TopBar(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        library_button = QPushButton("Library")
        main_layout.addWidget(library_button)

        add_model_button = QPushButton("Add Model")
        main_layout.addWidget(add_model_button)

        add_custom_button = QPushButton("Add Custom")
        main_layout.addWidget(add_custom_button)

        main_layout.addStretch()

        dropdown = QComboBox()
        dropdown.setFixedWidth(160)
        dropdown.setEditable(True)
        dropdown.lineEdit().setPlaceholderText("Categories")
        dropdown.setStyleSheet(
            f"border:0px solid transparent;border-bottom:1px solid #a0a0a0;background:transparent"
        )
        main_layout.addWidget(dropdown)

        search_bar = QLineEdit()
        search_bar.setFixedWidth(160)
        search_bar.setPlaceholderText("Search")
        search_bar.setStyleSheet(
            f"border:0px solid transparent;border-bottom:1px solid #a0a0a0;background:transparent"
        )
        main_layout.addWidget(search_bar)
