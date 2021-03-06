from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFrame, QMenuBar, QDesktopWidget, QLayout, QGridLayout, QMessageBox, QAction, QToolBar, \
    QLabel, QWidget, QSizePolicy
from PyQt5.QtGui import QIcon
from src.classes.Tile import Tile
from src.stylesheets.stylesheets import dark_grey
from random import choice
from datetime import timedelta


def mimesweeper_main_create_gui(window):
    window.setWindowIcon(QIcon('://mime_face.png'))
    # setting height and width as class attribs with the intent of later introducing functionality of changing them
    # by the player via additional dialog
    window.setFixedSize(QSize(window.width, window.height))
    # retrieving the geometry of the main window
    qt_rectangle = window.frameGeometry()
    # retrieving the center point of the desktop (will depend on desktop resolution)
    center_point = QDesktopWidget().availableGeometry().center()
    # moving the center of window to the center of the desktop
    qt_rectangle.moveCenter(center_point)
    window.move(qt_rectangle.topLeft())
    # creating and adding the central widget to house the tiles
    window.central_widget = QFrame(window)
    window.central_layout = QGridLayout()
    window.central_layout.setContentsMargins(0, 0, 0, 0)
    window.central_layout.setSpacing(0)
    window.central_widget.setLayout(window.central_layout)
    window.setCentralWidget(window.central_widget)
    window.setStyleSheet(dark_grey)
    window.show()
    # creating menu bar
    menu_bar = QMenuBar(window)
    window.setMenuBar(menu_bar)

    # creating toolbar
    window.toolbar = window.addToolBar('toolbar')
    window.toolbar.setFixedHeight(40)
    window.toolbar.setMovable(False)
    # creating left spacer to center the timer display
    left_spacer = QWidget()
    left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    window.toolbar.addWidget(left_spacer)
    # creating timer display
    window.timer_display = QLabel(str(timedelta(seconds=window.time_elapsed)))
    window.timer_display.setStyleSheet('QLabel {background-color: black; color: red; font: 42px, Fixedsys; '
                                       'border-style: inset; border-width: 3px; border-color: #6e8291;}')
    window.toolbar.addWidget(window.timer_display)
    # creating right spacer to center the timer display
    right_spacer = QWidget()
    right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    window.toolbar.addWidget(right_spacer)

    # adding file menu
    file_menu = menu_bar.addMenu('File')
    # adding 'new game' action to the file menu
    new_game_action = QAction('New Game', window)
    new_game_action.setShortcut('Ctrl+N')
    new_game_action.triggered.connect(window.start_new_game)
    file_menu.addAction(new_game_action)
    file_menu.addSeparator()
    # adding 'quit' action to the file menu
    quit_game_action = QAction('Quit game', window)
    quit_game_action.setShortcut('Ctrl+Q')
    quit_game_action.triggered.connect(window.close)
    file_menu.addAction(quit_game_action)


def create_tiles(window):
    # iterating through double loop based on map size to generate tile objects
    for x in range(window.map_width):
        for y in range(window.map_height):
            tile = Tile(window)
            window.central_layout.addWidget(tile, x, y, 1, 1)









