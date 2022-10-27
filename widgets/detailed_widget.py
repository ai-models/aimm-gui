from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QSizePolicy, QHBoxLayout, QToolButton, QApplication


class DetailedWidget(QWidget):
    def __init__(self, row):
        super().__init__()
        self.model_row = row
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self.main_layout)

        description = QLabel(self.model_row.model_info["description"])
        description.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        description.setWordWrap(True)
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(description, stretch=1)

        self.checksum_layout = QHBoxLayout()
        self.checksum_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addLayout(self.checksum_layout)
        self.checksum_layout.addStretch()

        checksum = QLabel(f'Checksum (md5): {self.model_row.model_info["md5"][:8]}...')
        checksum.setObjectName("checksum")
        self.checksum_layout.addWidget(checksum, alignment=Qt.AlignRight)

        self.copy_checksum_button = QToolButton()
        self.copy_checksum_button.setIcon(QPixmap("icons/copy.png"))
        self.copy_checksum_button.clicked.connect(
            lambda: QApplication.clipboard().setText(self.model_row.model_info["md5"])
        )
        self.checksum_layout.addWidget(self.copy_checksum_button, alignment=Qt.AlignRight)
        self.setMouseTracking(True)
