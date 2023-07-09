# main file
from mainWindow import MainWindow
import sys
import os
from PySide2.QtWidgets import QApplication
from PySide2 import QtGui
from PySide2.QtUiTools import QUiLoader
from assets.my_resources_rc import *
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    id = QtGui.QFontDatabase.addApplicationFont(os.path.join("assets","Chopsic.otf"))
    id = QtGui.QFontDatabase.addApplicationFont(os.path.join("assets","AVENGEANCE.ttf"))
    # if id != -1:
    #     print("Font loaded successfully")
    # else:
    #     print("Failed to load font")
    window = MainWindow()
    sys.exit(app.exec_())

    
    