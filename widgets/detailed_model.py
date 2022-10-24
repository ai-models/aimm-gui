from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget


class DetailedModel(QWidget):
    def __init__(self, row):
        super().__init__()
        self.model_row = row
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        description = QLabel(f"Description: {self.model_row.model_info['description']}")
        description.setWordWrap(True)
        description.setStyleSheet("""              
            background-color: #c5f5fe;
        """)
        self.main_layout.addWidget(description)

        checksum = QLabel(f'Checksum (md5): {self.model_row.model_info["md5"]}')
        checksum.setStyleSheet("""              
            background-color: #c5f5fe;
        """)
        self.main_layout.addWidget(checksum)
