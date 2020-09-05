from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.classes.Tile import Tile
from random import choice


def mimesweeper_main_create_gui(window):
    window.setWindowIcon(QIcon('://main_icon.png'))
    window.width = 430
    window.height = 450
    window.setGeometry(320, 320, window.width, window.height)
    menu_bar = QMenuBar(window)
    window.setMenuBar(menu_bar)
    file_menu = menu_bar.addMenu('File')
    window.central_widget = QFrame(window)
    window.central_layout = QGridLayout()
    window.central_layout.setContentsMargins(0, 0, 0, 0)
    window.central_layout.setSpacing(0)
    window.tile_list = []
    window.mime_list = []
    window.map_width = 10
    window.map_height = 10
    window.mimes_to_be_deployed = 20
    window.central_widget.setLayout(window.central_layout)
    window.setCentralWidget(window.central_widget)
    window.setFixedSize(window.size())


def create_tiles(window):
    for x in range(window.map_width):
        for y in range(window.map_height):
            tile = Tile(window)
            window.central_layout.addWidget(tile, x, y, 1, 1)







