from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFrame, QMenuBar, QDesktopWidget, QLayout, QGridLayout
from PyQt5.QtGui import QIcon
from src.classes.Tile import Tile
from src.stylesheets.stylesheets import dark_grey
from random import choice


def mimesweeper_main_create_gui(window):
    window.setWindowIcon(QIcon('://mime_face.png'))
    # setting height and width as class attribs with the intent of later introducing functionality of changing them
    # by the player via additional dialog
    window.width = 430
    window.height = 450
    window.setFixedSize(QSize(window.width, window.height))
    # retrieving the geometry of the main window
    qt_rectangle = window.frameGeometry()
    # retrieving the center point of the desktop (will depend on desktop resolution)
    center_point = QDesktopWidget().availableGeometry().center()
    # moving the center of window to the center of the desktop
    qt_rectangle.moveCenter(center_point)
    window.move(qt_rectangle.topLeft())
    # creating menu bar - later possibly to be moved to separate file
    menu_bar = QMenuBar(window)
    window.setMenuBar(menu_bar)
    # adding first action
    file_menu = menu_bar.addMenu('File')
    # creating and adding the central widget to house the tiles
    window.central_widget = QFrame(window)
    window.central_layout = QGridLayout()
    window.central_layout.setContentsMargins(0, 0, 0, 0)
    window.central_layout.setSpacing(0)
    # creating lists of all tiles and MIME tiles for later use in game logic
    window.tile_list = []
    window.mime_list = []
    # setting height and width of map/matrix as class attribs with the intent of later introducing functionality of
    # changing them by the player via additional dialog
    window.map_width = 10
    window.map_height = 10
    # same as above - number of mimes to deploy to be determined by player in future
    window.mimes_to_be_deployed = 20
    window.central_widget.setLayout(window.central_layout)
    window.setCentralWidget(window.central_widget)
    window.setStyleSheet(dark_grey)


def create_tiles(window):
    # iterating through double loop based on map size to generate tile objects
    for x in range(window.map_width):
        for y in range(window.map_height):
            tile = Tile(window)
            window.central_layout.addWidget(tile, x, y, 1, 1)









