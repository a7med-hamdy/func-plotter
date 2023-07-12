import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np
import sympy as sp
from config import *

class Plotter(QWidget):
    
    def __init__(self, parent = None, width=50, height=4, dpi=100):

        QWidget.__init__ ( self ,  parent )
        
        self.canvas = FigureCanvas(Figure(figsize = (width, height), dpi = dpi))
        vertical_layout = QVBoxLayout()
        toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout.addWidget(toolbar)
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
    
    # a function to plot the graph of the expression    
    def make_graph(self, expression : sp.Expr, min_x : float, max_x : float) -> None:
        x,y = self.create_points(expression, min_x, max_x)
        self.__plot(x, y)
    
    # a function to create points from the expression
    def create_points(self, expression : sp.Expr, min_x: float, max_x : float) -> tuple:
        # use the sympy expression to create list of points from min_x to max_x
        x = sp.Symbol("x")
        x_vals = np.linspace(min_x, max_x, num_points)
        # ecaluate the expression at each point
        y_vals = np.array([sp.lambdify(x, expression)(i) for i in x_vals])
        return x_vals, y_vals
        
    # a helper function to plot the graph
    def __plot(self, x : list, y : list) -> None:
        self.canvas.axes.clear()
        self.canvas.axes.set_title("Plot")
        self.canvas.axes.set_xlim(min(x), max(x))
        self.canvas.axes.set_ylim(min(y), max(y))
        self.canvas.axes.grid()
        self.canvas.axes.plot(x, y)
        self.canvas.draw()
        self.__show_plot()
        
    # a helper function to show the plot with animation
    def __show_plot(self) -> None:
        self.show()
        self.effect = QGraphicsOpacityEffect()
        self.canvas.setGraphicsEffect(self.effect)
        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
        
        