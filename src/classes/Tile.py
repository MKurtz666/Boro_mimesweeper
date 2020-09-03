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
        self.setFixedHeight(45)
        self.setFixedWidth(45)
        self.parent = window
        self.content = ''
        self.neighbouring_mimes = 0
        window.tile_list.append(self)

    def reveal_tile(self):
        if self.content == 'MIME':
            for mime in self.parent.mime_list:
                mime.setIcon(QIcon('://mime_face.png'))
                mime.setIconSize(QSize(20, 20))
                mime.setChecked(True)
        else:
            self.setText(self.content)
            self.setChecked(True)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.setIcon(QIcon('://caution_icon.png'))
            self.setIconSize(QSize(20, 20))
        else:
            self.reveal_tile()




