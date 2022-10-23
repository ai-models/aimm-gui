from PySide6.QtWidgets import QApplication
import sys

from widgets.main_window import MainWindow

if __name__ == "__main__":
  app = QApplication(sys.argv)
  app.setStyle("Fusion")
  window = MainWindow()
  window.show()
  window.resize(1000, 600)
  # app.setQuitOnLastWindowClosed(False)

sys.exit(app.exec())
