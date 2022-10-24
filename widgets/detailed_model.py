from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget


class DetailedModel(QWidget):
    def __init__(self, row):
        super().__init__()
        self.model_row = row
        self.setStyleSheet("background-color: #ffffff;")
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        description = QLabel(f"Description: {self.model_row.model_info['description']}")
        description.setWordWrap(True)
        self.main_layout.addWidget(description)

        checksum = QLabel(f'Checksum (md5): {self.model_row.model_info["md5"]}')
        self.main_layout.addWidget(checksum)
