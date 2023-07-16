import sys
sys.path.insert(0, './') # for the future to setupt github actions

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pytest
from config import *
from mainWindow import MainWindow

# test points creation
@pytest.fixture
def app(qtbot):
    window = MainWindow(True)
    qtbot.addWidget(window)
    return window

#test no input case
def test_no_input(app, qtbot):
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    assert app.feedback.label.text() == ERROR_WRONG_EXPRESSION
    assert app.plotter.isHidden()
    
# test true testcase
def test_constant_function(app, qtbot):
    qtbot.keyClicks(app.function, "2")
    qtbot.keyClicks(app.min, "-10")
    qtbot.keyClicks(app.max, "10")
    assert app.feedback.label.isHidden()
    assert app.gif.label.isHidden()
    assert not app.plotter.isHidden()

# test invallid fucntion
def test_wrong_expression(app, qtbot):
    qtbot.keyClicks(app.function, "x^2-")
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    assert app.feedback.label.text() == ERROR_WRONG_EXPRESSION
    assert app.plotter.isHidden()
# test invalid minimum value
def test_wrong_min_value(app, qtbot):
    qtbot.keyClicks(app.function, "x^2")
    qtbot.keyClicks(app.min, "1*2")
    qtbot.keyClicks(app.max, "10")
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    assert app.feedback.label.text() == ERROR_WRONG_MIN
    assert app.plotter.isHidden()
    
# test invalid maximum value
def test_wrong_max_value(app, qtbot):
    qtbot.keyClicks(app.function, "x^2")
    qtbot.keyClicks(app.min, "-10") 
    qtbot.keyClicks(app.max, "10/7")
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    assert app.feedback.label.text() == ERROR_WRONG_MAX
    assert app.plotter.isHidden()
# test invalid bounds
def test_greater_min(app, qtbot):
    qtbot.keyClicks(app.function, "x^2")
    qtbot.keyClicks(app.min, "10")
    qtbot.keyClicks(app.max, "1")
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    assert app.feedback.label.text() == ERROR_WRONG_BOUNDS
    assert app.plotter.isHidden()
# test infinite minimum
def test_infinite_min(app, qtbot):
    qtbot.keyClicks(app.function, "x^2")
    qtbot.keyClicks(app.min, "inf")
    qtbot.keyClicks(app.max, "10")
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    assert app.feedback.label.text() == ERROR_INFINITE_MIN
    assert app.plotter.isHidden()
# test infinite maximum
def test_infinite_max(app, qtbot):
    qtbot.keyClicks(app.function, "x^2")
    qtbot.keyClicks(app.min, "-10")
    qtbot.keyClicks(app.max, "inf")
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    assert app.feedback.label.text() == ERROR_INFINITE_MAX
    assert app.plotter.isHidden()

# test invalid variable
def test_invalid_variable(app, qtbot):
    qtbot.keyClicks(app.function, "y^2")
    qtbot.keyClicks(app.min, "-10")
    qtbot.keyClicks(app.max, "10")
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    assert app.feedback.label.text() == ERROR_WRONG_VARIABLE
    assert app.plotter.isHidden()
    
def test_undefined_function(app,qtbot):
    qtbot.keyClicks(app.function, "f(x)")
    qtbot.keyClicks(app.min, "7")
    qtbot.keyClicks(app.max, "15")
    qtbot.mouseClick(app.eval_button.button, Qt.LeftButton)
    qtbot.waitUntil(lambda: app.feedback.label.text() == ERROR_EVLAUATE + "name 'f' is not defined")
    assert app.plotter.isHidden()