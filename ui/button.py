from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class button():
    def __init__(self, button: QPushButton, test: bool = False):
        self.button = button
        # 2 color to interpolate between them
        self.color1 = (255, 85, 0)
        self.color2 = (255, 255, 255)
        
        
        self._animation = QVariantAnimation(
            self.button,
            startValue=0.0,
            endValue=1.0,
            duration=1000
        )
        if not test:
            self.timer = QTimer() # timer to animate the button
            self._animation.valueChanged.connect(self._animate) 
            self.timer.timeout.connect(self.timer_animate)
            self._animate(0.0)# set the initial color of the button
            self.timer.start(1000) # start the timer every 1.5 seconds
            self.flag = True # flag to change the direction of animation and reverse it
    
    # a function that is called when the animation updates
    def _animate(self, value : float) -> None:
        # linear interpolation between color1 and color2
        interpolated_color = (int(self.color1[0] + value * (self.color2[0] - self.color1[0])),
                      int(self.color1[1] + value * (self.color2[1] - self.color1[1])),
                      int(self.color1[2] + value * (self.color2[2] - self.color1[2])))
        
        # convert the interpolated color to a QColor object
        color = QColor(interpolated_color[0], interpolated_color[1], interpolated_color[2])
        # create new style sheet for the button
        var = f"QPushButton{{border: 1px solid {color.name()};border-radius: 20px;color: rgb(247, 255, 217);}}"
        # fixed style sheet
        fixed = '''
        QPushButton:hover{
            color:rgb(255,85,0);
            background-color:  rgb(247, 255, 217);
        }

        QPushButton:pressed{
            border: 3px solid rgb(255,85,0);
        }
        '''
        # set the style sheet
        self.button.setStyleSheet(fixed+var)

    # a function that is called when the timer times out
    def timer_animate(self) -> None:
        if self.flag:
            self._animation.setDirection(QAbstractAnimation.Forward)
        else:
            self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        self.flag = not self.flag # reverse the direction of animation
