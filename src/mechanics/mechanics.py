from src.classes.Tile import Tile
from random import choice
from time import sleep
from datetime import datetime, timedelta


def generate_mimes(window):
    # when the tiles are created the function assigns random tiles with 'MIME' content rendering them
    # deadly when stepped on. The number of times the function does that is dependent on how many mimes
    # there are to be generated according top the parent window class attrib
    while window.mimes_to_be_deployed > 0:
        chosen_tile = choice(window.tile_list)
        if chosen_tile.content != 'MIME':
            chosen_tile.content = 'MIME'
            # adding the MIME tiles to mime_list for later use in logic
            window.mime_list.append(chosen_tile)
            window.mimes_to_be_deployed -= 1


def create_matrix(window):
    # creating a 2d matrix of tiles for later use in logic based on the parent window tile_list
    window.matrix = [[tile for tile in window.tile_list[window.tile_list.index(tile):window.tile_list.index(tile) +
                                                                                     window.map_width]] for tile in
                     window.tile_list[::window.map_width]]


def check_if_tile_in_range(matrix, row_index, tile_index_to_be_ckecked):
    # checking if given tile index is in range to avoid indexError
    if tile_index_to_be_ckecked <= len(matrix[row_index]) - 1:
        return True
    return False


def check_if_row_in_range(matrix, row_index_to_be_ckecked):
    # checking if given row index is in range to avoid indexError
    if row_index_to_be_ckecked <= len(matrix) - 1:
        return True
    return False


def generate_clean_tiles(window):
    # assigning appropriate content - that is the number of neighbouring mimes - to tiles that are not MIME tiles
    matrix = window.matrix
    # enumerating rows in matrix
    for row_index, row in enumerate(matrix):
        # enumerating tiles in row
        for tile_index, tile in enumerate(row):
            # executing if tile is not already a MIME tile
            if tile.content != 'MIME':
                # checking if tile 'to the right' is in row range
                if check_if_tile_in_range(matrix, row_index, tile_index + 1):
                    # if tile 'to the right' in range adding to the count of neighbouring mimes
                    if row[tile_index + 1] in window.mime_list:
                        tile.neighbouring_mimes += 1
                # checking if tile 'up' is in matrix range
                if check_if_row_in_range(matrix, row_index - 1):
                    if row_index != 0:
                        if matrix[row_index - 1][tile_index] in window.mime_list:
                            tile.neighbouring_mimes += 1
                # checking if tile 'down' in range of matrix
                if check_if_row_in_range(matrix, row_index + 1):
                    if matrix[row_index + 1][tile_index] in window.mime_list:
                        tile.neighbouring_mimes += 1
                # checking if tile 'to the left' is in row range
                if check_if_tile_in_range(matrix, row_index, tile_index - 1):
                    if tile_index != 0:
                        if row[tile_index - 1] in window.mime_list:
                            tile.neighbouring_mimes += 1
                # checking if tile 'up and to the left' is in matrix range
                if check_if_row_in_range(matrix, row_index - 1) and \
                        check_if_tile_in_range(matrix, row_index - 1, tile_index - 1):
                    if row_index != 0 and tile_index != 0:
                        if matrix[row_index - 1][tile_index - 1] in window.mime_list:
                            tile.neighbouring_mimes += 1
                # checking if tile 'up and to the right' is in matrix range
                if check_if_row_in_range(matrix, row_index - 1) and \
                        check_if_tile_in_range(matrix, row_index - 1, tile_index + 1):
                    if row_index != 0:
                        if matrix[row_index - 1][tile_index + 1] in window.mime_list:
                            tile.neighbouring_mimes += 1
                # checking if tile 'down and to the right' is in matrix range
                if check_if_row_in_range(matrix, row_index + 1) and \
                        check_if_tile_in_range(matrix, row_index + 1, tile_index + 1):
                    if matrix[row_index + 1][tile_index + 1] in window.mime_list:
                        tile.neighbouring_mimes += 1
                # checking if tile 'down and to the left' is in matrix range
                if check_if_row_in_range(matrix, row_index + 1) and \
                        check_if_tile_in_range(matrix, row_index + 1, tile_index - 1):
                    if tile_index != 0:
                        if matrix[row_index + 1][tile_index - 1] in window.mime_list:
                            tile.neighbouring_mimes += 1

                # setting the (yet invisible) tile content to reflect number of neighbor mimes
                tile.content = str(tile.neighbouring_mimes)
