from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import resources
from random import randint


class Tile(QPushButton):

    def __init__(self, window):
        QPushButton.__init__(self)
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
        elif self.content == '0':
            for row in self.parent.matrix:
                for tile in row:
                    if tile is self:
                        row_index = self.parent.matrix.index(row)
                        tile_index = row.index(tile)
            self.setText(self.content)
            self.setChecked(True)
            self.reveal_neighbouring_zeros(row_index, tile_index)
        else:
            self.setText(self.content)
            self.setChecked(True)

    def reveal_neighbouring_zeros(self, row_index, tile_index):
        # checking for tiles containing a number further down the row
        try:
            if self.parent.matrix[row_index][tile_index + 1].content != 'MIME' and not \
                    self.parent.matrix[row_index][tile_index + 1].isChecked():
                self.parent.matrix[row_index][tile_index + 1].reveal_tile()
        except IndexError:
            pass
        # checking for numbers in previous row, same tile index under the condition
        # that this is not the first row
        try:
            if row_index != 0:
                if self.parent.matrix[row_index - 1][tile_index].content != 'MIME' and not \
                        self.parent.matrix[row_index - 1][tile_index].isChecked():
                    self.parent.matrix[row_index - 1][tile_index].reveal_tile()
        except IndexError:
            pass
        # checking for numbers in the next row. No condition as index error handled
        try:
            if self.parent.matrix[row_index + 1][tile_index].content != 'MIME' and not \
                    self.parent.matrix[row_index + 1][tile_index].isChecked():
                self.parent.matrix[row_index + 1][tile_index].reveal_tile()
        except IndexError:
            pass
        # checking for numbers on the previous index in the row under the condition that
        # index of current tile not 0
        try:
            if tile_index != 0:
                if self.parent.matrix[row_index][tile_index - 1].content != 'MIME' and not \
                        self.parent.matrix[row_index][tile_index - 1].isChecked():
                    self.parent.matrix[row_index][tile_index - 1].reveal_tile()
        except IndexError:
            pass

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.setIcon(QIcon('://caution_icon.png'))
            self.setIconSize(QSize(20, 20))
        else:
            self.reveal_tile()




