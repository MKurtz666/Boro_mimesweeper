from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from src.gui.main_create_gui import mimesweeper_main_create_gui, create_tiles
from src.mechanics.mechanics import generate_mimes, generate_clean_tiles, create_matrix
from src.classes.DifficultyDialog import DifficultyDialog
from threading import Thread
from datetime import timedelta
from time import sleep


class MimeSweeperMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.width = 0
        self.height = 0
        self.map_width = 0
        self.map_height = 0
        self.mimes_to_be_deployed = 0
        # creating lists of all tiles and MIME tiles for later use in game logic
        self.tile_list = []
        self.mime_list = []
        self.time_elapsed = 0
        self.game_ended = False
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
        self.timer = Thread(target=self.timer)
        self.timer.daemon = True
        self.timer.start()

    def start_new_game(self):
        self.close()
        new_window = MimeSweeperMain()
        new_window.show()

    def stepped_on_a_mime(self):
        # dialog to be displayed if stepped on a mime
        self.game_ended = True
        game_over_box = QMessageBox.question(self, 'Game over',
                                             'You stepped on a mime. Game over man! \n Do you want to start over?',
                                             QMessageBox.Yes, QMessageBox.No)
        if game_over_box == QMessageBox.Yes:
            self.start_new_game()
        else:
            self.close()

    def check_if_victorious(self):
        checked_list = []
        for tile in self.tile_list:
            if tile.isChecked():
                checked_list.append(tile)
        if len(checked_list) == (len(self.tile_list) - len(self.mime_list)):
            self.victory()

    def victory(self):
        self.game_ended = True
        game_over_box = QMessageBox.question(self, 'VICTORY!',
                                             f'Congratulations!\nYour time is: {self.time_elapsed}\nWanna play again?',
                                             QMessageBox.Yes, QMessageBox.No)
        if game_over_box == QMessageBox.Yes:
            self.start_new_game()
        else:
            self.close()

    def timer(self):
        time_elapsed = self.time_elapsed
        while True:
            if self.game_ended:
                return
            self.time_elapsed = timedelta(seconds=time_elapsed)
            self.timer_display.setText(str(self.time_elapsed))
            sleep(1)
            time_elapsed += 1

