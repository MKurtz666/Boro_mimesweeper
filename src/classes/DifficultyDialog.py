from PyQt5.QtWidgets import QDialog, QMessageBox
from src.gui.diff_dialog_create_gui import diff_dialog_create_gui
import resources


class DifficultyDialog(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self)
        self.size_buttons = []
        self.mime_pop_buttons = []
        self.parent = parent
        diff_dialog_create_gui(self)

    def size_button_checked(self, button_checked, window_width, window_height, map_width, map_height):
        #  creating a func for 1) applying the button contents to relevant game attribs, 2) de-selecting other buttons
        # in a given 'category'
        for button in self.size_buttons:
            if button is not button_checked:
                button.setChecked(False)
        self.parent.width = window_width
        self.parent.height = window_height
        self.parent.map_width = map_width
        self.parent.map_height = map_height

    def mime_pop_button_checked(self, button_checked, mime_population):
        for button in self.mime_pop_buttons:
            if button is not button_checked:
                button.setChecked(False)
        self.parent.mimes_to_be_deployed = mime_population

    def closeEvent(self, event):
        # overriding the closeEvent so that the user is unable to close the window until the size and pop are chosen
        for size_button in self.size_buttons:
            if size_button.isChecked():
                for pop_button in self.mime_pop_buttons:
                    if pop_button.isChecked():
                        event.accept()
                        return
        warning = QMessageBox.question(self, 'Error',
                                             'Please select game area and mime population!',
                                             QMessageBox.Ok)
        if warning == QMessageBox.Ok:
            event.ignore()









