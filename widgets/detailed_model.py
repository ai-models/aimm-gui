from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget


class DetailedModel(QWidget):
    def __init__(self, row):
        super().__init__()
        self.model_row = row
        self.setStyleSheet("background-color: #ffffff;")
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        name = QLabel(f"Name: {self.model_row.model_info['name']}")
        name.setWordWrap(True)
        self.main_layout.addWidget(name)

        github_link = self.model_row.model_info.get("github_url")
        if github_link is not None:
            github_label = QLabel(f'<a href={github_link}>{github_link}</a>')
        else:
            github_label = QLabel("No github link")
        github_label.setOpenExternalLinks(True)
        github_label.linkActivated.connect(self.model_row.open_link)
        self.main_layout.addWidget(github_label)

        hugging_face_link = self.model_row.model_info.get("huggingface_url")
        if hugging_face_link is not None:
            hugging_face_label = QLabel(f'<a href={hugging_face_link}>{hugging_face_link}</a>')
        else:
            hugging_face_label = QLabel("Hugging Face: Not available")
        hugging_face_label.setOpenExternalLinks(True)
        hugging_face_label.linkActivated.connect(self.model_row.open_link)
        self.main_layout.addWidget(hugging_face_label)

        description = QLabel(f"Description: {self.model_row.model_info['description']}")
        description.setWordWrap(True)
        self.main_layout.addWidget(description)

        checksum = QLabel(f'Checksum (md5): {self.model_row.model_info["md5"]}')
        self.main_layout.addWidget(checksum)
