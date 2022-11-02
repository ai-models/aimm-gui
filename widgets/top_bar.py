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

        # self.add_custom_button = QPushButton("Add Custom")
        # self.add_custom_button.setObjectName("green_button")
        # self.add_custom_button.clicked.connect(lambda: self.go_to_tab(2))
        # self.main_layout.addWidget(self.add_custom_button)
        # self.add_custom_button.hide()

        self.main_layout.addStretch()

        self.categories = QComboBox()
        self.categories.setFixedWidth(160)
        self.categories.setObjectName("categories")
        self.main_layout.addWidget(self.categories)

        self.search = QLineEdit()
        self.search.setFixedWidth(160)
        self.search.setPlaceholderText("Search")
        self.search.setObjectName("search")
        self.main_layout.addWidget(self.search)

    def go_to_tab(self, tab: int):
        self.main_window.table_layout.setCurrentIndex(tab)
        # if tab in (1, 2):
        #     self.add_custom_button.show()
        # else:
        #     self.add_custom_button.hide()

    def update_categories(self, categories: set):
        self.categories.clear()
        self.categories.addItem("")
        self.categories.addItems(sorted(categories))
