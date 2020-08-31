from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.gui.main_create_gui import mimesweeper_main_create_gui
from src.classes.Tile import Tile

import resources
from random import randint


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

        for x in range(10):
            for y in range(10):
                tile = Tile(self)
                central_layout.addWidget(tile, x, y, 1, 1)
        # running check to make sure that the given number of mimes is always present
        while self.mine_count < 10:
            for tile in self.tile_list:
                chance = randint(1, 10)
                if chance == 1:
                    tile.content = 'X'
                    tile.setText('B')
                    self.mine_count += 1
                    tile.clicked.connect(lambda: tile.setText(tile.content))
        self.central_widget.setLayout(central_layout)
        self.setCentralWidget(self.central_widget)
        self.setFixedSize(self.size())




if __name__ == '__main__':
    mime_sweeper = QApplication([])
    mime_sweeper.setApplicationName('Mimesweeper')
    main_window = MimeSweeperMain()
    main_window.show()
    mime_sweeper.exec_()
