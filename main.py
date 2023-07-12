# main file
from mainWindow import MainWindow
import sys
import os
from PySide2.QtWidgets import QApplication, QSplashScreen
from PySide2.QtCore import QTimer
from PySide2 import QtGui
from assets.my_resources_rc import *
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    id = QtGui.QFontDatabase.addApplicationFont(os.path.join("assets","Chopsic.otf"))
    id = QtGui.QFontDatabase.addApplicationFont(os.path.join("assets","AVENGEANCE.ttf"))
    # if id != -1:
    #     print("Font loaded successfully")
    # else:
    #     print("Failed to load font")
    splash = QSplashScreen(QtGui.QPixmap(os.path.join("assets","splash.png")))
    window = MainWindow()
    splash.show()
    QTimer.singleShot(2000, splash.close)
    QTimer.singleShot(2000, window.show)
    sys.exit(app.exec_())

    
    