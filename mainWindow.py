from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader
from config import *
from Parser import Parser
from button import button
from feedback import feedback
from plotter import Plotter
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
        # labels fonts
        self.findChild(QLabel, "title").setFont(QFont(FONT_AV, 32))
        self.findChild(QLabel, "label1").setFont(QFont("Consolas", 14))
        self.findChild(QLabel, "label2").setFont(QFont("Consolas", 14))
        self.findChild(QLabel, "label3").setFont(QFont("Consolas", 14))
        
        
        # line edits fonts
        # expression
        self.function = self.findChild(QLineEdit, "function")
        self.function.setFont(QFont("Consolas", 18))
        # minimum x
        self.min = self.findChild(QLineEdit, "min")
        self.min.setFont(QFont("Consolas", 16))
        # maximum x
        self.max = self.findChild(QLineEdit, "max")
        self.max.setFont(QFont("Consolas", 16))
        
        # evaluate button
        self.eval_button = button(self.findChild(QPushButton, "eval"))
        self.eval_button.button.setFont(QFont("Consolas", 16))
        self.eval_button.button.clicked.connect(self.handle_eval)
        
        # feedback label
        self.feedback  = self.findChild(QLabel, "feedback")
        self.feedback.setFont(QFont("Consolas", 16))
        self.feedback = feedback(self.feedback)
        
        # plotter
        self.plotter = Plotter()
        plotter = self.findChild(QWidget, "Plotter")
        plotter.setLayout(QVBoxLayout())
        plotter.layout().addWidget(self.plotter)
                
        self.show()
        

    # a function that is called when the evalualte button is clicked
    def handle_eval(self):
        # parse the expression
        try:
            expression = self.Parser.parse_expression(self.function.text())
            # print(expression)
        except Exception as e:
            self.plotter.hide()
            self.feedback.show("Invalid expression, only * / + - ^ are allowed")
            return 
        
        # parse the minimum x value    
        try:
            min_x = self.Parser.parse_value(self.min.text())
            # print(min_x)
        except Exception as e:
            self.plotter.hide()
            self.feedback.show("Invalid Minimum x value")
            return
        
        # parse the maximum x value
        try:
            max_x = self.Parser.parse_value(self.max.text())
            # print(max_x)
        except Exception as e:
            self.plotter.hide()
            self.feedback.show("Invalid Maximum x value")
            return

        # check if the maximum x value is greater than the minimum x value
        if max_x <= min_x:
            self.feedback.show("Maximum x value must be greater than minimum x value")
            return 
        
        # if everything is valid, hide the feedback label
        self.feedback.hide()
        
        #plor the graph usinh the plotter
        self.plotter.make_graph(expression, min_x, max_x)