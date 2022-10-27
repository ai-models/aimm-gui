from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView
from widgets.table_widget import TableWidget


class LibraryTableWidget(TableWidget):
    def __init__(self, main_window):
        super().__init__(main_window)

        self.setColumnCount(7)
        self.setHorizontalHeaderLabels(["", 'Category', 'Name', 'Version', 'Size', 'Path', 'Delete'])

        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        self.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.horizontalHeaderItem(4).setTextAlignment(Qt.AlignHCenter)
        self.horizontalHeaderItem(5).setTextAlignment(Qt.AlignHCenter)
        self.horizontalHeaderItem(6).setTextAlignment(Qt.AlignHCenter)
