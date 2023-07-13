import sys
sys.path.insert(0, './') # for the future to setupt github actions

from helpers.plotter import Plotter
from helpers.thread import computeThread
from config import num_points
import pytest
import sympy as sp
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# test points creation
@pytest.fixture
def app(qtbot):
    plotter = Plotter()
    qtbot.addWidget(plotter)

    return plotter

@pytest.fixture
def thread(qtbot):
    thread = computeThread()
    return thread

def helper(x, y):
    assert len(x) == num_points
    assert len(y) == num_points
    assert x[0] == -10
    assert x[-1] == 10
    assert y[0] == 99
    assert y[-1] == 99

def test_create_points(thread, qtbot):
    thread.set_expression(sp.sympify("x^2-1"))
    thread.set_min_max_x(-10, 10)
    thread.finished.connect(helper)
    thread.start()
    with qtbot.waitSignal(thread.finished):
        pass
    
        
#test the whole plotting process
def test_make_graph(app, qtbot):
    app.make_graph(sp.sympify("x^2-1"), -10, 10)
    with qtbot.waitSignal(app.thread.finished):
        pass
    assert app.canvas.axes.get_title() == "Plot"
    assert app.canvas.axes.get_xbound() == (-10, 10)
    
# test animation
def test_animation(app, qtbot):
    app.make_graph(sp.sympify("x^2-1"), -10, 10)
    with qtbot.waitSignal(app.thread.finished):
        pass
    assert not app.isHidden()
    assert app.animation.finished
    
    