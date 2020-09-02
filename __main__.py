from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.gui.main_create_gui import mimesweeper_main_create_gui
from src.classes.Tile import Tile
from random import randint, choice


class MimeSweeperMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        mimesweeper_main_create_gui(self)

        # ---------------------  the below will be moved to gui creation file later in the development
        self.setGeometry(300, 300, 400, 400)
        self.setWindowIcon(QIcon('://main_icon.png'))
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu('File')
        self.central_widget = QFrame(self)
        central_layout = QGridLayout()
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(0)
        self.mine_count = 0
        self.tile_list = []
        self.mime_list = []
        self.mime_number = 20

        # generating tiles
        for x in range(10):
            for y in range(10):
                tile = Tile(self)
                central_layout.addWidget(tile, x, y, 1, 1)
        # generating mimes
        for x in range(self.mime_number):
            chosen_tile = choice(self.tile_list)
            chosen_tile.content = 'MIME'
            chosen_tile.clicked.connect(self.mime_disturbed)
            self.tile_list.remove(chosen_tile)
            self.mime_list.append(chosen_tile)
        self.central_widget.setLayout(central_layout)
        self.setCentralWidget(self.central_widget)
        self.setFixedSize(self.size())

    def mime_disturbed(self):
        for mime in self.mime_list:
            mime.setIcon(QIcon('://mime_face.png'))
            mime.setIconSize(QSize(20, 20))
            mime.setChecked(True)


if __name__ == '__main__':
    mime_sweeper = QApplication([])
    mime_sweeper.setApplicationName('Mimesweeper')
    main_window = MimeSweeperMain()
    main_window.show()
    mime_sweeper.exec_()
