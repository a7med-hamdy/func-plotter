from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class feedback():
    def __init__(self, label : QLabel) -> None:
        self.label = label
        self.label.hide()
       
    # handle the animation of the feedback label 
    def show(self, text : str) -> None:
        self.label.setText(text)
        self.label.show()
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(2000) 
        self.animation.setEasingCurve(QEasingCurve.OutElastic)
        self.animation.setStartValue(self.label.pos() - QPoint(0, 50))
        self.animation.setEndValue(self.label.pos())
        self.animation.start()
        
    def hide(self) -> None:
        self.label.hide()
    