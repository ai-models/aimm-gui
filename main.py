import asyncio
from asyncio.subprocess import Process
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
import sys, os

from widgets.main_window import MainWindow
basedir_icons = os.path.dirname(__file__) + "\icons\\"

if __name__ == "__main__":
  app = QApplication(sys.argv)
  app.setStyle("Fusion")
  window = MainWindow()
  window.show()
  window.resize(1000, 600)

  ## Tray Icon
  app.setQuitOnLastWindowClosed(False)
  # Create the icon
  icon = QIcon(os.path.join(basedir_icons, 'icon.png'))

  # Create the tray
  tray = QSystemTrayIcon()
  tray.setIcon(icon)
  tray.setVisible(True)

  # Create the menu
  menu = QMenu()

  # Add a Quit option to the menu.
  quit = QAction("Quit")
  quit.triggered.connect(app.quit)
  menu.addAction(quit)

  # Add the menu to the tray
  tray.setContextMenu(menu)


  async def apistart():
    # process: Process = await asyncio.create_subprocess_exec('python','api/main.py')
    process: Process = await asyncio.create_subprocess_exec('.\dist\\api\\api.exe')
    print(f'Process pid is: {process.pid}')

asyncio.run(apistart())

sys.exit(app.exec())
