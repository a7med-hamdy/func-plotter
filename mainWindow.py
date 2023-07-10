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


        # set appropriate fonts
        self.findChild(QLabel, "title").setFont(QFont(FONT_AV, 32))
        self.findChild(QLabel, "label1").setFont(QFont("Consolas", 14))
        self.findChild(QLabel, "label2").setFont(QFont("Consolas", 14))
        self.findChild(QLabel, "label3").setFont(QFont("Consolas", 14))
        
        
        
        self.function = self.findChild(QLineEdit, "function")
        self.function.setFont(QFont("Consolas", 18))
        
        self.min = self.findChild(QLineEdit, "min")
        self.min.setFont(QFont("Consolas", 16))
        
        self.max = self.findChild(QLineEdit, "max")
        self.max.setFont(QFont("Consolas", 16))
        
        
        self.eval_button = self.findChild(QPushButton, "eval")
        self.eval_button.setFont(QFont("Consolas", 16))
        self.eval_button.clicked.connect(self.handle_eval)
        
        self.show()
    
    def handle_eval(self):
        print("eval")
        print(self.function.text())
        print(self.min.text())
        print(self.max.text())