from PyQt5.QtWidgets import *
from src.gui.main_create_gui import mimesweeper_main_create_gui, create_tiles, generate_mimes, generate_clean_tiles, \
    create_matrix


class MimeSweeperMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        mimesweeper_main_create_gui(self)
        create_tiles(self)
        generate_mimes(self)
        create_matrix(self)
        generate_clean_tiles(self)