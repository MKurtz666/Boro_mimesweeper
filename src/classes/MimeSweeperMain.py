from PyQt5.QtWidgets import QMainWindow, QMessageBox
from src.gui.main_create_gui import mimesweeper_main_create_gui, create_tiles
from src.mechanics.mechanics import generate_mimes, generate_clean_tiles, create_matrix


class MimeSweeperMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
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

    def closeEvent(self, event):
        # overriding closeEvent of main window to include the game over message box
        game_over_box = QMessageBox.question(self, 'Game over',
                                             'You stepped on a mime. Game over man! \n Do you want to start over?',
                                             QMessageBox.Yes, QMessageBox.No)
        if game_over_box == QMessageBox.Yes:
            event.accept()
            new_window = MimeSweeperMain()
            new_window.show()
        else:
            event.accept()

