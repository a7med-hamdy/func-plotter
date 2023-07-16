from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader
from config import *
from helpers.Parser import Parser
from ui.button import button
from ui.feedback import feedback
from ui.gif import LoadingGif
from helpers.plotter import Plotter
import sympy as sp
import os

class MainWindow(QMainWindow):
    def __init__(self, test : bool = False):
        super().__init__()
        self.setFixedSize(1000, 700)
        self.setWindowTitle("App")
        self.Parser = Parser()
        self.center()
        self.isTest = test
        # load the ui file
        loader = QUiLoader()
        self.setCentralWidget(loader.load(os.path.join("assets","gui.ui"), self))
        
        self.setup_ui()
        self.setup_plotter()
        
    # center the window
    def center(self):
        # Get the available geometry of the primary screen
        screen = QGuiApplication.primaryScreen().availableGeometry()
        
        # Calculate the center point of the screen
        center = screen.center()

        # Calculate the top-left point of the window
        top_left = center - self.rect().center()

        # Set the position of the window
        self.move(top_left)
        
    def setup_plotter(self) -> None:
        # plotter
        self.plotter = Plotter(stop_gif= self.gif.stopAnimation, error_handler = self.report_error)
        plotter = self.findChild(QWidget, "Plotter")
        plotter.setLayout(QVBoxLayout())
        plotter.layout().addWidget(self.plotter)

    # setup the ui
    def setup_ui(self) -> None:
        self.setup_line_edits()
        self.setup_buttons()
        self.setup_labels()
        
        
    
    def setup_line_edits(self) -> None:
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
    
    def setup_buttons(self) -> None:
        # evaluate button
        self.eval_button = button(self.findChild(QPushButton, "eval"), self.isTest)
        self.eval_button.button.setFont(QFont("Consolas", 16))
        self.eval_button.button.clicked.connect(self.handle_eval)
        
    def setup_labels(self) -> None:
        
        # feedback label
        self.feedback  = self.findChild(QLabel, "feedback")
        self.feedback.setFont(QFont("Consolas", 16))
        self.feedback = feedback(self.feedback)
        
        # gif label
        gif = self.findChild(QLabel, "gif")
        self.gif = LoadingGif(gif)
        
        # set appropriate fonts
        # labels fonts
        self.findChild(QLabel, "title").setFont(QFont(FONT_AV, 32))
        self.findChild(QLabel, "label1").setFont(QFont("Consolas", 14))
        self.findChild(QLabel, "label2").setFont(QFont("Consolas", 14))
        self.findChild(QLabel, "label3").setFont(QFont("Consolas", 14))
    
    # a function that is called when the evalualte button is clicked
    def handle_eval(self)->None:
        args = self.parse_input()
        if args is None:
            return
        # if everything is valid, hide the feedback label
        self.feedback.hide()
        
        #plor the graph using the plotter
        self.gif.startAnimation()
        self.plotter.make_graph(args[0], args[1], args[2])
        try:
            pass
        except TypeError:
            self.report_error(ERROR_WRONG_VARIABLE)
            
    def parse_input(self)->tuple:
        # parse the expression
        try:
            expression = self.Parser.parse_expression(self.function.text())
        except sp.SympifyError:
            self.report_error(ERROR_WRONG_EXPRESSION)
            return None
        except RuntimeError:
            self.report_error(ERROR_WRONG_VARIABLE)
            return
        
        # parse the minimum x value    
        try:
            min_x = self.Parser.parse_value(self.min.text())
        except ValueError:
            self.report_error(ERROR_WRONG_MIN)
            return None
        except RuntimeError:
            self.report_error(ERROR_INFINITE_MIN)
            return None
        
        # parse the maximum x value
        
        try:
            max_x = self.Parser.parse_value(self.max.text())
        except ValueError:
            self.report_error(ERROR_WRONG_MAX)
            return None
        except RuntimeError:
            self.report_error(ERROR_INFINITE_MAX)
            return None

        # check if the maximum x value is greater than the minimum x value
        if max_x <= min_x:
            self.report_error(ERROR_WRONG_BOUNDS)
            return None
        return expression, min_x, max_x
    
    # a function to report errors
    def report_error(self, error : str) -> None:
        self.plotter.hide()
        self.feedback.show(str(error))