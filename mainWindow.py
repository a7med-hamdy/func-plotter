from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from config import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        # make the font bold
        label.setFont(QFont(FONT_AV, 16))

        self.setCentralWidget(label)
        
        self.show()