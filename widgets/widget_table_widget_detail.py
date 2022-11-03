from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QSizePolicy, QHBoxLayout, QToolButton, QApplication


class DetailedWidget(QWidget):
    def __init__(self, row, show_links=False):
        super().__init__()
        self.row = row
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self.main_layout)

        description = QLabel(self.row.model_info["description"])
        description.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        description.setWordWrap(True)
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(description, stretch=1)

        self.lower_right_layout = QHBoxLayout()
        self.lower_right_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addLayout(self.lower_right_layout)
        self.lower_right_layout.addStretch()

        if show_links:
            github_url_label = QLabel(f'<a href={self.row.model_info["github_url"]}>Github</a>')
            github_url_label.setOpenExternalLinks(True)
            github_url_label.linkActivated.connect(lambda: QDesktopServices.openUrl(QUrl(self.row.model_info["github_url"])))
            self.lower_right_layout.addWidget(github_url_label)

        checksum = QLabel(f'Checksum (md5): {self.row.model_info["md5"][:8]}...')
        checksum.setObjectName("checksum")
        self.lower_right_layout.addWidget(checksum, alignment=Qt.AlignRight)

        self.copy_checksum_button = QToolButton()
        self.copy_checksum_button.setIcon(QPixmap("icons/copy.png"))
        self.copy_checksum_button.clicked.connect(
            lambda: QApplication.clipboard().setText(self.row.model_info["md5"])
        )
        self.lower_right_layout.addWidget(self.copy_checksum_button, alignment=Qt.AlignRight)
        self.setMouseTracking(True)
