import asyncio
from asyncio.subprocess import Process
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
import sys, os


from widgets.main_window import MainWindow
from widgets.trayicon import run

if __name__ == "__main__":
  if not QApplication.instance():
    app = QApplication(sys.argv)
  else:
    app = QApplication.instance()
  app.setStyle("Fusion")
  window = MainWindow()
  window.show()
  window.resize(1000, 600)

  app.run = run(window)

  async def apistart():
    # process: Process = await asyncio.create_subprocess_exec('python','api/main.py')
    process: Process = await asyncio.create_subprocess_exec('.\dist\\api\\api.exe')
    print(f'Process pid is: {process.pid}')

  asyncio.run(apistart())
  sys.exit(app.exec())
