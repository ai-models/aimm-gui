from PySide6.QtCore import QUrl, Slot
from PySide6.QtGui import QDesktopServices, Qt
from PySide6.QtWidgets import QLabel, QPushButton, QToolButton

from widgets.detailed_model import DetailedModel


class ModelRow:
    def __init__(self, models_table_widget: "ModelsTableWidget", model_info: dict):
        super().__init__()
        self.models_table_widget = models_table_widget
        self.models_table_widget.setStyleSheet("""
                                               QTableWidget{
                                                   background-color: #ffffff;
                                                   }
                                               
                                               QTableWidget::item:selected{
                                                   color: #ffffff;
                                                   background-color: blue;
                                                   }""")
        self.model_info = model_info

        self.detailed_model = DetailedModel(self)
        self.widgets = []

        self.collapse_button = QToolButton()
        self.collapse_button.setArrowType(Qt.ArrowType.RightArrow)
        self.collapse_button.clicked.connect(self.toggle_selected)
        self.widgets.append(self.collapse_button)

        category = QLabel(self.model_info['category'])
        category.setWordWrap(False)
        # hover status
        category.setToolTip("This is the category")
        self.widgets.append(category)

        name = QLabel(self.model_info['name'])
        name.setWordWrap(False)
        # hover status
        name.setToolTip(f"This is the name: {self.model_info['name']}")
        self.widgets.append(name)

        version = QLabel(self.model_info['version'])
        self.widgets.append(version)

        size_label = QLabel(self.model_info['size'])
        self.widgets.append(size_label)

        github_url = QLabel(f'<a href={self.model_info["github_url"]}>Github</a>')
        github_url.setOpenExternalLinks(True)
        github_url.linkActivated.connect(self.open_link)
        self.widgets.append(github_url)

        install_button = QPushButton('Install')
        install_button.clicked.connect(self.install_model)
        self.widgets.append(install_button)

    @staticmethod
    @Slot(str)
    def open_link(link: str):
        QDesktopServices.openUrl(QUrl(link))

    def install_model(self):
        ...  # TODO

    def toggle_selected(self):
        if self.collapse_button.arrowType() == Qt.ArrowType.DownArrow:
            # Hide
            self.models_table_widget.clearSelection()
            self.collapse_button.setArrowType(Qt.ArrowType.RightArrow)
            self.models_table_widget.deselect_model(self)
        else:
            # Select
            self.collapse_button.setArrowType(Qt.ArrowType.DownArrow)
            self.models_table_widget.select_model(self)

    def __repr__(self):
        return f"ModelRow('{self.model_info['name']}')"