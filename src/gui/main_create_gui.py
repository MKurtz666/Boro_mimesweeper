from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.classes.Tile import Tile
from random import choice


def mimesweeper_main_create_gui(window):
    window.setGeometry(320, 320, 430, 450)
    window.setWindowIcon(QIcon('://main_icon.png'))
    menu_bar = QMenuBar(window)
    window.setMenuBar(menu_bar)
    file_menu = menu_bar.addMenu('File')
    window.central_widget = QFrame(window)
    window.central_layout = QGridLayout()
    window.central_layout.setContentsMargins(0, 0, 0, 0)
    window.central_layout.setSpacing(0)
    window.tile_list = []
    window.mime_list = []
    window.mimes_to_be_deployed = 20
    window.central_widget.setLayout(window.central_layout)
    window.setCentralWidget(window.central_widget)
    window.setFixedSize(window.size())


def create_tiles(window):
    for x in range(10):
        for y in range(10):
            tile = Tile(window)
            window.central_layout.addWidget(tile, x, y, 1, 1)


def generate_mimes(window):
    while window.mimes_to_be_deployed > 0:
        chosen_tile = choice(window.tile_list)
        if chosen_tile.content != 'MIME':
            chosen_tile.content = 'MIME'
            chosen_tile.clicked.connect(chosen_tile.reveal_tile)
            window.mime_list.append(chosen_tile)
            window.mimes_to_be_deployed -= 1


def create_matrix(window):
    window.matrix = [[tile for tile in window.tile_list[window.tile_list.index(tile):window.tile_list.index(tile) + 10]]
                     for tile in window.tile_list[::10]]


def check_if_tile_in_range(matrix, row_index, tile_index_to_be_ckecked):
    if tile_index_to_be_ckecked <= len(matrix[row_index]) - 1:
        return True
    return False


def check_if_row_in_range(matrix, row_index_to_be_ckecked):
    if row_index_to_be_ckecked <= len(matrix) - 1:
        return True
    return False


def generate_clean_tiles(window):
    matrix = window.matrix
    # iterating through every row in matrix
    for row in matrix:
        # iterating through every tile in row
        for tile in row:
            # executing if tile is not already a MIME tile
            if tile.content != 'MIME':
                # pinning down tile position in matrix
                row_index = matrix.index(row)
                tile_index = row.index(tile)
                # checking if tile 'to the right' is in row range
                if check_if_tile_in_range(matrix, row_index, tile_index + 1):
                    # if tile 'to the right' in range adding to the count of neighbouring mimes
                    if row[tile_index + 1] in window.mime_list:
                        tile.neighbouring_mimes += 1
                # checking if tile 'up' is in matrix range
                if check_if_row_in_range(matrix, row_index - 1):
                    # if tile 'up' in range and tile not in first row adding to count of neighboring mimes
                    if row_index != 0:
                        if matrix[row_index - 1][tile_index] in window.mime_list:
                            tile.neighbouring_mimes += 1
                # checking if tile 'down' in range of matrix
                if check_if_row_in_range(matrix, row_index + 1):
                    # if tile 'down' in range of matrix adding to the count of neighbouring mimes
                    if matrix[row_index + 1][tile_index] in window.mime_list:
                        tile.neighbouring_mimes += 1
                # checking if tile 'to the left' is in row range
                if check_if_tile_in_range(matrix, row_index, tile_index - 1):
                    # if tile 'to the left' is in row range adding to the count of neighbouring mimes
                    if tile_index != 0:
                        if row[tile_index - 1] in window.mime_list:
                            tile.neighbouring_mimes += 1
                # setting the (yet invisible) tile content to reflect number of neighbor mimes
                tile.content = str(tile.neighbouring_mimes)




