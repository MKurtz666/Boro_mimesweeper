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







