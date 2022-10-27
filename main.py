import asyncio
import os
from asyncio.subprocess import Process
from pathlib import Path

from PySide6.QtWidgets import QApplication
import sys

from widgets.main_window import MainWindow
from widgets.trayicon import run

if getattr(sys, "frozen", False):
    bundle_dir = Path(getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__))))
else:
    bundle_dir = Path().parent


if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    app.setStyle("Fusion")
    app.setStyleSheet((bundle_dir / "stylesheet.qss").read_text())
    window = MainWindow()
    window.show()
    window.resize(1000, 600)

    app.run = run(window)

    # async def apistart():
    #   # process: Process = await asyncio.create_subprocess_exec('python','api/main.py')
    #   process: Process = await asyncio.create_subprocess_exec('.\dist\\api\\api.exe')
    #   print(f'Process pid is: {process.pid}')

    # asyncio.run(apistart())
    sys.exit(app.exec())
