import sys
sys.path.insert(0, './') # for the future to setupt github actions

from helpers.plotter import Plotter
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

def test_create_points(app, qtbot):
    x, y = app.create_points(sp.sympify("x^2-1"), -10, 10)
    assert len(x) == num_points
    assert len(y) == num_points
    assert x[0] == -10
    assert x[-1] == 10
    assert y[0] == 99
    assert y[-1] == 99
    
# test variable names other than x

def test_create_points_other_var(app, qtbot):
    plotter = Plotter()
    with pytest.raises(Exception):
        x, y = plotter.create_points("a^2-1", -10, 10)
        
# test the whole plotting process
def test_make_graph(app, qtbot):
    app.make_graph(sp.sympify("x^2-1"), -10, 10)
    assert app.canvas.axes.get_title() == "Plot"
    assert app.canvas.axes.get_xbound() == (-10, 10)
    
# test animation
def test_animation(app, qtbot):
    app.make_graph(sp.sympify("x^2-1"), -10, 10)
    assert not app.isHidden()
    assert app.animation.finished
    
    