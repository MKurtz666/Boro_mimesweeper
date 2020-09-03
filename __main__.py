from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.gui.main_create_gui import mimesweeper_main_create_gui, create_tiles, generate_mimes, generate_clean_tiles


class MimeSweeperMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        mimesweeper_main_create_gui(self)

        # ---------------------  the below will be moved to gui creation file later in the development
        self.setGeometry(320, 320, 430, 450)
        self.setWindowIcon(QIcon('://main_icon.png'))
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu('File')
        self.central_widget = QFrame(self)
        self.central_layout = QGridLayout()
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)
        self.tile_list = []
        self.mime_list = []
        self.mimes_to_be_deployed = 20
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        self.setFixedSize(self.size())

        create_tiles(self)
        generate_mimes(self)
        generate_clean_tiles(self)


if __name__ == '__main__':
    mime_sweeper = QApplication([])
    mime_sweeper.setApplicationName('Mimesweeper')
    main_window = MimeSweeperMain()
    main_window.show()
    mime_sweeper.exec_()
