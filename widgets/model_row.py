from PySide6 import QtCore
from PySide6.QtCore import QUrl, Slot
from PySide6.QtGui import QDesktopServices, QPixmap, Qt
from PySide6.QtWidgets import QLabel, QPushButton, QWidget, QHBoxLayout, QApplication, QToolButton, QSizePolicy

from widgets.detailed_widget import DetailedWidget


class ModelRow:
    def __init__(self, main_window, table, model_info: dict):
        super().__init__()
        self.main_window = main_window
        self.table = table
        self.model_info = model_info

        self.category = model_info['category']
        self.name = model_info['name']
        self.description = model_info['description']

        self.add_model_widgets = []
        self.library_widgets = []

        self.collapse_button = QPushButton()
        self.collapse_button.setObjectName("collapse_button")
        self.collapse_button.setFlat(True)
        self.collapse_button.setIcon(QPixmap("icons/right_arrow.png"))
        self.collapse_button.clicked.connect(self.toggle_collapsed)
        self.collapse_button.mousePressEvent = self.handle_mouse_press
        self.add_model_widgets.append(self.collapse_button)
        self.library_widgets.append(self.collapse_button)

        category_label = QLabel(self.model_info["category"])
        category_label.setWordWrap(False)
        category_label.setToolTip("This is the category")
        self.add_model_widgets.append(category_label)
        self.library_widgets.append(category_label)

        name_label = QLabel(self.model_info["name"])
        name_label.setWordWrap(False)
        name_label.setToolTip(f"This is the name: {self.model_info['name']}")
        self.add_model_widgets.append(name_label)
        self.library_widgets.append(name_label)

        version_label = QLabel(self.model_info["version"])
        version_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.add_model_widgets.append(version_label)
        self.library_widgets.append(version_label)

        size_label = QLabel(self.model_info["size"])
        size_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.add_model_widgets.append(size_label)
        self.library_widgets.append(size_label)

        self.url_widget = QWidget()
        self.url_layout = QHBoxLayout()
        self.url_layout.setContentsMargins(0, 0, 0, 0)
        self.url_widget.setLayout(self.url_layout)

        self.github_url_label = QLabel('Github')
        self.github_url_label.setObjectName("url_label")
        self.github_url_label.mousePressEvent = self.handle_github_url_mouse_press
        self.url_layout.addWidget(self.github_url_label)
        self.url_layout.addStretch()
        self.add_model_widgets.append(self.url_widget)

        self.path_widget = QWidget()
        path_layout = QHBoxLayout()
        path_layout.setContentsMargins(8, 0, 0, 0)
        path_layout.setSpacing(0)
        path_layout.setAlignment(Qt.AlignLeft)
        self.path_widget.setLayout(path_layout)

        path_copy_button = QToolButton()
        path_copy_button.setObjectName("path_copy_button")
        path_copy_button.setIcon(QPixmap("icons/copy.png"))
        path_copy_button.clicked.connect(lambda: QApplication.clipboard().setText(self.model_info["path"]))
        path_copy_button.setMouseTracking(True)
        path_layout.addWidget(path_copy_button, 0)

        path_label = QLabel(f'...{self.model_info["path"]}')
        path_label.setOpenExternalLinks(True)
        path_label.linkActivated.connect(self.open_link)
        path_label.setMouseTracking(True)
        path_layout.addWidget(path_label)

        self.library_widgets.append(self.path_widget)

        self.install_button = QPushButton()

        if not self.model_info["installed"]:
            self.install_button.setText("Install")
        else:
            self.install_button.setText("Installed")
            self.install_button.setDisabled(True)

        self.install_button.clicked.connect(self.install_model)
        self.install_button.setObjectName("table_button")
        self.add_model_widgets.append(self.install_button)

        delete_button = QPushButton()
        delete_button.setText("Delete")
        delete_button.clicked.connect(self.delete_model)
        delete_button.setObjectName("table_button")
        self.library_widgets.append(delete_button)

        for widget in self.add_model_widgets:
            widget.setMouseTracking(True)
        for widget in self.library_widgets:
            widget.setMouseTracking(True)

        self.detailed_widget = DetailedWidget(self, show_links=table.name == "LibraryTableWidget")
    
    def handle_github_url_mouse_press(self, event):
        QLabel.mousePressEvent(self.github_url_label, event)
        self.table.unselect_row()
        self.table.select_row(self.table.models.index(self) * 2)
        QDesktopServices.openUrl(QUrl(self.model_info["github_url"]))

    def handle_mouse_press(self, event):
        QPushButton.mousePressEvent(self.collapse_button, event)
        self.table.unselect_row()
        self.table.select_row(self.table.models.index(self) * 2)

    @staticmethod
    @Slot(str)
    def open_link(link: str):
        QDesktopServices.openUrl(QUrl(link))

    def install_model(self):
        self.main_window.library_table_widget.install_model(self)
        self.install_button.setText("Installed")
        self.install_button.setDisabled(True)
        self.main_window.add_model_table_widget.selectRow(self.table.models.index(self) * 2)

    def delete_model(self):
        self.table.delete_model(self)
        model = self.main_window.add_model_table_widget.find_correspondent_model(self)
        model.install_button.setEnabled(True)
        model.install_button.setText("Install")

    def toggle_collapsed(self):
        self.table.unselect_row()
        self.table.select_row(self.table.models.index(self) * 2)

        if self.detailed_widget.isVisible():
            # Hide
            self.table.clearSelection()
            self.collapse_button.setIcon(QPixmap("icons/right_arrow.png"))
            self.table.hide_model(self)
        else:
            # Show
            self.collapse_button.setIcon(QPixmap("icons/down_arrow.png"))
            self.table.show_model(self)

    def __repr__(self):
        return f"ModelRow('{self.model_info['name']}')"

