from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os

class LoadingGif():
    def __init__(self, lb: QLabel):

        # Label Create
        self.label = lb
        # Loading the GIF
        # the icon "Ellipsis" is provided by loading.io
        self.movie = QMovie(os.path.join("assets", "loading.gif"))
        self.movie.setScaledSize(QSize(50, 50))
        self.label.setMovie(self.movie)
        self.label.hide()

    # Start Animation
    def startAnimation(self):
        self.label.show()
        self.movie.start()

    # Stop Animation
    def stopAnimation(self):
        self.movie.stop()
        self.label.hide()