from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.classes.Tile import Tile
from random import choice


def mimesweeper_main_create_gui(window):
    pass


def create_tiles(window):
    for x in range(10):
        for y in range(10):
            tile = Tile(window)
            window.central_layout.addWidget(tile, x, y, 1, 1)


def generate_mimes(window):
    for x in range(window.mime_number):
        chosen_tile = choice(window.tile_list)
        chosen_tile.content = 'MIME'
        chosen_tile.clicked.connect(chosen_tile.reveal_tile)
        window.mime_list.append(chosen_tile)


def generate_clean_tiles(window):
    matrix = [[tile for tile in window.tile_list[window.tile_list.index(tile):window.tile_list.index(tile) + 10]]
              for tile in window.tile_list[::10]]
    for row in matrix:
        for tile in row:
            if tile.content != 'MIME':
                try:
                    if row[row.index(tile) + 1] in window.mime_list:
                        tile.neighbouring_mimes += 1
                except IndexError:
                    pass
                try:
                    if row is not matrix[0]:
                        if matrix[matrix.index(row) - 1][row.index(tile)] in window.mime_list:
                            tile.neighbouring_mimes += 1
                except IndexError:
                    pass
                try:
                    if matrix[matrix.index(row) + 1][row.index(tile)] in window.mime_list:
                        tile.neighbouring_mimes += 1
                except IndexError:
                    pass
                try:
                    if tile is not row[0]:
                        if row[row.index(tile) - 1] in window.mime_list:
                            tile.neighbouring_mimes += 1
                except IndexError:
                    pass

                tile.content = str(tile.neighbouring_mimes)
                tile.clicked.connect(tile.reveal_tile)

