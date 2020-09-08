from PyQt5.QtWidgets import QApplication
from src.classes.MimeSweeperMain import MimeSweeperMain


if __name__ == '__main__':
    mime_sweeper = QApplication([])
    mime_sweeper.setApplicationName('Mimesweeper')
    main_window = MimeSweeperMain()
    mime_sweeper.exec_()

