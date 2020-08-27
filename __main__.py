from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from gui.main_create_gui import mimesweeper_main_create_gui

import resources


class MimeSweeperMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        mimesweeper_main_create_gui(self)

        # ---------------------  the below will be moved to gui creation file later in the development
        self.setGeometry(300, 300, 400, 400)
        self.setFixedWidth(400)
        self.setFixedHeight(400)
        self.setWindowIcon(QIcon('://main_icon.png'))
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu('File')
        self.central_widget = QFrame(self)
        central_layout = QGridLayout()
        central_layout.setContentsMargins(20, 20, 20, 20)
        central_layout.setSpacing(0)

        for x in range(19):
            for y in range(19):
                tile = QPushButton(self.central_widget)
                tile.setCheckable(True)
                tile.setFixedWidth(20)
                tile.setFixedHeight(20)
                central_layout.addWidget(tile, x, y, 1, 1)
        self.central_widget.setLayout(central_layout)
        self.setCentralWidget(self.central_widget)


if __name__ == '__main__':
    mime_sweeper = QApplication([])
    mime_sweeper.setApplicationName('Mimesweeper')
    main_window = MimeSweeperMain()
    main_window.show()
    mime_sweeper.exec_()
