from PyQt6 import QtWidgets, QtCore, QtGui
import sys


import qt.mainwindow
import logic.json_backend

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    json_handler = logic.json_backend.Json_Handler()
    window = qt.mainwindow.Window(json_handler)
    sys.exit(app.exec())
