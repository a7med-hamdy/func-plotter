from PySide2.QtCore import *
import PySide2.QtCore
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sympy as sp
import numpy as np
from config import num_points, ERROR_EVLAUATE

class computeThread(QThread):
    finished = Signal(list, list)
    error = Signal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
    
    def set_expression(self, expression : sp.Expr) -> None:
        self.expression = expression
    
    def set_min_max_x(self, min_x : float, max_x : float) -> None:
        self.min_x = min_x
        self.max_x = max_x
    
    # main thread function
    def run(self) -> None:
        # create points from the expression
        try:
            x, y = self.create_points(self.expression, self.min_x, self.max_x)
            self.finished.emit(x, y)
        except TypeError: # if an error occured while evaluating the expression
            self.error.emit(ERROR_EVLAUATE)
        self.stop()
    
    # a function to create points from the expression
    def create_points(self, expression : sp.Expr, min_x: float, max_x : float) -> tuple:
        # use the sympy expression to create list of points from min_x to max_x
        x = sp.Symbol("x")
        x_vals = np.linspace(min_x, max_x, num_points)
        # ecaluate the expression at each point
        y_vals = np.array([sp.lambdify(x, expression)(i) for i in x_vals])
        return x_vals, y_vals
    
    def stop(self):
        self.quit()