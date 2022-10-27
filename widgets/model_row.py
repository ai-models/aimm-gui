from PySide6 import QtCore
from PySide6.QtCore import QUrl, Slot
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton

from widgets.detailed_widget import DetailedWidget


class ModelRow:
    def __init__(self, models_table_widget: "ModelsTableWidget", model_info: dict):
        super().__init__()
        self.models_table_widget = models_table_widget
        self.model_info = model_info

        self.detailed_widget = DetailedWidget(self)
        self.widgets = []

        self.collapse_button = QPushButton()
        self.collapse_button.setFlat(True)
        self.collapse_button.setIcon(QPixmap("icons/right_arrow.png"))
        self.collapse_button.clicked.connect(self.toggle_collapsed)
        self.widgets.append(self.collapse_button)

        category = QLabel(self.model_info["category"])
        category.setWordWrap(False)
        # hover status
        category.setToolTip("This is the category")
        self.widgets.append(category)

        name = QLabel(self.model_info["name"])
        name.setWordWrap(False)
        name.setToolTip(f"This is the name: {self.model_info['name']}")
        self.widgets.append(name)

        version = QLabel(self.model_info["version"])
        version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.widgets.append(version)

        size_label = QLabel(self.model_info["size"])
        size_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.widgets.append(size_label)

        github_url = QLabel(f'<a href={self.model_info["github_url"]}>Github</a>')
        github_url.setOpenExternalLinks(True)
        github_url.linkActivated.connect(self.open_link)
        self.widgets.append(github_url)

        install_button = QPushButton("Install")
        install_button.clicked.connect(self.install_model)
        install_button.setObjectName("install_button")
        install_button.setMinimumWidth(60)
        self.widgets.append(install_button)

        for widget in self.widgets:
            widget.setMouseTracking(True)

    @staticmethod
    @Slot(str)
    def open_link(link: str):
        QDesktopServices.openUrl(QUrl(link))

    def install_model(self):
        ...  # TODO

    def toggle_collapsed(self):
        self.models_table_widget.unselect_row()
        self.models_table_widget.select_row(self.models_table_widget.models.index(self) * 2)

        if self.detailed_widget.isVisible():
            # Hide
            self.models_table_widget.clearSelection()
            self.collapse_button.setIcon(QPixmap("icons/right_arrow.png"))
            self.models_table_widget.hide_model(self)
        else:
            # Show
            self.collapse_button.setIcon(QPixmap("icons/down_arrow.png"))
            self.models_table_widget.show_model(self)


    def __repr__(self):
        return f"ModelRow('{self.model_info['name']}')"

    # def hover_row(self):
    #     self.models_table_widget.clear_hover()
    #     self.models_table_widget.hover_model(self)

    # def set_stylesheet(self, stylesheet: str):
    #     for widget in self.widgets:
    #         widget.setStyleSheet(stylesheet)
    #     self.detailed_widget.setStyleSheet(stylesheet)
