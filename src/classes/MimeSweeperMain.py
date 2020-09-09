from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from src.gui.main_create_gui import mimesweeper_main_create_gui, create_tiles
from src.mechanics.mechanics import generate_mimes, generate_clean_tiles, create_matrix
from src.classes.DifficultyDialog import DifficultyDialog


class MimeSweeperMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.width = 0
        self.height = 0
        self.map_width = 0
        self.map_height = 0
        self.mimes_to_be_deployed = 0
        difficulty_dialog = DifficultyDialog(self)
        difficulty_dialog.exec_()
        # creating main window gui
        mimesweeper_main_create_gui(self)
        # creating tiles
        create_tiles(self)
        # assigning MIME content to random tiles
        generate_mimes(self)
        # creating 2d map of tiles
        create_matrix(self)
        # assigning content to tiles that are not MIME tiles
        generate_clean_tiles(self)

    def start_new_game(self):
        self.close()
        new_window = MimeSweeperMain()
        new_window.show()

    def stepped_on_a_mime(self):
        # # dialog to be displayed if stepped on a mime
        game_over_box = QMessageBox.question(self, 'Game over',
                                             'You stepped on a mime. Game over man! \n Do you want to start over?',
                                             QMessageBox.Yes, QMessageBox.No)
        if game_over_box == QMessageBox.Yes:
            self.start_new_game()
        else:
            self.close()
