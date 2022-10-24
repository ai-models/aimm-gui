import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu

class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, win, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        # self.setToolTip("Test SystemTray")
        self.win = win  # <----- name it whatever you want ie self.abc will also work
        menu = QMenu(parent)
        # exit_ = menu.addAction("Exit")
        # exit_.triggered.connect(lambda: sys.exit())
        #
        self.setContextMenu(menu)
        # self.activated.connect(self.trayiconclicked)



def run(win):
    basedir_icons = os.path.dirname(__file__) + "\..\icons\\"
    print(os.path.join(basedir_icons, 'icon.png'))
    # app.setQuitOnLastWindowClosed(False)
    # Create the icon
    icon = QIcon(os.path.join(basedir_icons, 'icon.png'))

    # Create the tray
    tray = QSystemTrayIcon(icon, win)
    tray.setVisible(True)
    tray.activated.connect(trayiconclicked)

def trayiconclicked(reason):
    print(reason)
    if str(reason) == 'ActivationReason.Trigger':
        print('ay')
        # print("SysTrayIcon left clicked")
