from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtUiTools import QUiLoader
from config import *
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 700)
        self.setWindowTitle("App")

        loader = QUiLoader()
        self.setCentralWidget(loader.load(os.path.join("assets","gui.ui"), self))

        self.title = self.findChild(QLabel, "title")
        self.title.setFont(QFont(FONT_AV, 32))
        
        self.show()