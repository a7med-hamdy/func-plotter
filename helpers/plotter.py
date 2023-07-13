import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sympy as sp
from helpers.thread import computeThread

class Plotter(QWidget):
    
    def __init__(self, width=50, height=4, dpi=100, stop_gif : callable = None):
        super().__init__()
        
        # embed the matplotlib figure
        self.canvas = FigureCanvas(Figure(figsize = (width, height), dpi = dpi))
        vertical_layout = QVBoxLayout() # create a vertical layout
        toolbar = NavigationToolbar(self.canvas, self) # create a toolbar
        vertical_layout.addWidget(toolbar) # add the toolbar to the layout
        vertical_layout.addWidget(self.canvas)  # add the canvas to the layout
        self.canvas.axes = self.canvas.figure.add_subplot(111) # add a subplot to the figure
        self.setLayout(vertical_layout) # set the layout
        self.stop_gif = stop_gif # a function to stop the gif
        self.thread = None # a thread to compute the points in the background
    
    # a function to plot the graph of the expression    
    def make_graph(self, expression : sp.Expr, min_x : float, max_x : float) -> None:
        if self.thread is not None and self.thread.isRunning(): # if the thread is running return
            return
        self.thread : QThread= computeThread() # create a thread to compute the points in the background without freezing the ui
        self.thread.set_expression(expression) # set the expression
        self.thread.set_min_max_x(min_x, max_x) # set the min and max x
        self.thread.finished.connect(self.__plot) # connect the finished signal to the plot function
        self.thread.finished.connect(lambda x,y : self.stop_gif()) # connect the finished signal to the stop gif function
        self.thread.start()     # start the thread
    
    
        
    # a helper function to plot the graph
    def __plot(self, x : list, y : list) -> None:
        self.canvas.axes.clear() # clear the axes
        self.canvas.axes.set_title("Plot") # set the title
        self.canvas.axes.set_xlim(min(x), max(x)) # set the x limits
        self.canvas.axes.grid() # show the grid
        self.canvas.axes.plot(x, y) 
        self.canvas.draw()
        self.__show_plot()
        
    # a helper function to show the plot with animation
    def __show_plot(self) -> None:
        self.show()
        # create an opacity effect
        self.effect = QGraphicsOpacityEffect()
        self.canvas.setGraphicsEffect(self.effect)
        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
        
        