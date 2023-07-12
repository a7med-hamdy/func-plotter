import sys
sys.path.insert(0, './') # for the future to setupt github actions

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pytest
from mainWindow import MainWindow

# test points creation
@pytest.fixture
def app(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window


def test_dummy(app, qtbot):
    assert True