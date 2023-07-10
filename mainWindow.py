from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader
from config import *
from Parser import Parser
from button import button
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 700)
        self.setWindowTitle("App")
        
        self.animations = []
        self.Parser = Parser()
        # load the ui file
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
        
        
        self.eval_button = button(self.findChild(QPushButton, "eval"))
        self.eval_button.button.setFont(QFont("Consolas", 16))
        self.eval_button.button.clicked.connect(self.handle_eval)
        self.animations.append(self.eval_button._animation)
        
    
        
        
        # self.feedback  = self.findChild(QLabel, "feedback")
        # self.feedback.setFont(QFont("Consolas", 16))
        
        
        # self.animation = QPropertyAnimation(self.feedback, b"font")
        # self.animation.setDuration(2000)  # 1000 milliseconds = 1 second
        # #self.animation.setEasingCurve(QEasingCurve.OutElastic)
        # self.animation.setStartValue(QFont("Consolas", 16))
        # self.animation.setEndValue(QFont("Consolas", 50))
        # self.animation.start()
        self.show()
        

    # a function that is called when the evalualte button is clicked
    def handle_eval(self):
        expression = self.Parser.parse_expression(self.function.text())
        print(expression)
        min_x = self.Parser.parse_value(self.min.text())
        print(min_x)
        max_x = self.Parser.parse_value(self.max.text())
        print(max_x)