from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from src.stylesheets.stylesheets import mime_tile_checked, zero_tile_checked, number_tile_checked
import resources


class Tile(QPushButton):

    def __init__(self, window):
        QPushButton.__init__(self)
        self.setCheckable(True)
        # setting button size
        self.setFixedSize(QSize(45, 45))
        self.parent = window
        # button content left empty for now
        self.content = ''
        # no neighbouring mimes added yet
        self.neighbouring_mimes = 0
        # tile not flagged so this attr is False by default
        self.caution_flag = False
        # adding tile to the parent tile_list for use in logic
        window.tile_list.append(self)

    @staticmethod
    def check_if_tile_in_range(matrix, row_index, tile_index_to_be_ckecked):
        # checking if tile with a given position in the matrix is available to avoid index error
        if tile_index_to_be_ckecked <= len(matrix[row_index]) - 1:
            return True
        return False

    @staticmethod
    def check_if_row_in_range(matrix, row_index_to_be_ckecked):
        # checking if row with a given index in the matrix is available to avoid index error
        if row_index_to_be_ckecked <= len(matrix) - 1:
            return True
        return False

    def mousePressEvent(self, QMouseEvent):
        # overriding mousePressEvent to be able to set/remove caution flags with righ click...
        if QMouseEvent.button() == Qt.RightButton:
            if not self.isChecked():
                if self.caution_flag is False:
                    self.setIcon(QIcon('://caution_icon.png'))
                    self.setIconSize(QSize(20, 20))
                    self.caution_flag = True
                else:
                    self.setIcon(QIcon())
                    self.caution_flag = False
        # and reveal tiles with left click
        else:
            self.reveal_tile()

    def reveal_tile(self):
        # depending on the content of the tile, revealing it and taking action
        if self.content == 'MIME':
            # if the content of a tile is 'MIME' all MIME tiles are revealed and a game over message box is triggered
            for mime in self.parent.mime_list:
                mime.setStyleSheet(mime_tile_checked)
                mime.setIcon(QIcon('://mime_face.png'))
                mime.setIconSize(QSize(20, 20))
                mime.setChecked(True)
            self.parent.stepped_on_a_mime()
        elif self.content == '0':
            # if the content is '0' (so no MIMES to the left, right, up, down and diagonally) reveal and trigger same
            # method for neighbouring tiles
            for r_index, row in enumerate(self.parent.matrix):
                for t_index, tile in enumerate(row):
                    if tile is self:
                        row_index = r_index
                        tile_index = t_index
            self.setText(self.content)
            self.setChecked(True)
            self.setIcon(QIcon())
            self.setStyleSheet(zero_tile_checked)
            self.reveal_neighbouring_zeros(row_index, tile_index)
        else:
            # if content is neither 'MIME' nor '0' (some MIMEs in the neighbourhood) reveal tile
            self.setText(self.content)
            self.setChecked(True)
            self.setIcon(QIcon())
            self.setStyleSheet(number_tile_checked)

    def reveal_neighbouring_zeros(self, row_index, tile_index):
        # checking for tiles containing a number further down the row
        if self.check_if_tile_in_range(self.parent.matrix, row_index, tile_index + 1):
            if self.parent.matrix[row_index][tile_index + 1].content != 'MIME' and not \
                    self.parent.matrix[row_index][tile_index + 1].isChecked():
                self.parent.matrix[row_index][tile_index + 1].reveal_tile()
        # checking for numbers in previous row, same tile index under the condition
        # that this is not the first row
        if self.check_if_row_in_range(self.parent.matrix, row_index - 1):
            if row_index != 0:
                if self.parent.matrix[row_index - 1][tile_index].content != 'MIME' and not \
                        self.parent.matrix[row_index - 1][tile_index].isChecked():
                    self.parent.matrix[row_index - 1][tile_index].reveal_tile()
        # checking for numbers in the next row. No condition as index error handled
        if self.check_if_row_in_range(self.parent.matrix, row_index + 1):
            if self.parent.matrix[row_index + 1][tile_index].content != 'MIME' and not \
                    self.parent.matrix[row_index + 1][tile_index].isChecked():
                self.parent.matrix[row_index + 1][tile_index].reveal_tile()
        # checking for numbers on the previous index in the row under the condition that
        # index of current tile not 0
        if self.check_if_tile_in_range(self.parent.matrix, row_index, tile_index - 1):
            if tile_index != 0:
                if self.parent.matrix[row_index][tile_index - 1].content != 'MIME' and not \
                        self.parent.matrix[row_index][tile_index - 1].isChecked():
                    self.parent.matrix[row_index][tile_index - 1].reveal_tile()







