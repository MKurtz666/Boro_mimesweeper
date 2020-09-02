from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import resources
from random import randint


class Tile(QPushButton):

    def __init__(self, window):
        QPushButton.__init__(self)

        # creating the game field by iterating and creating tiles
        self.setCheckable(True)
        self.content = ''
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        window.tile_list.append(self)


