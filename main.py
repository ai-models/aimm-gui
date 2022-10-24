from PySide6.QtWidgets import QApplication
import sys

from widgets.main_window import MainWindow


if __name__ == "__main__":
    # fixed an error after try to restart the application
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    window.resize(1000, 600)
    sys.exit(app.exec())