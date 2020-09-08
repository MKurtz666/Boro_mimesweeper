from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QDialog, QLayout, QDesktopWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from src.stylesheets.stylesheets import dark_grey


def diff_dialog_create_gui(window):
    window.setWindowIcon(QIcon('://mime_face.png'))
    window.setFixedSize(QSize(300, 170))
    window.setStyleSheet(dark_grey)
    # retrieving the geometry of the main window
    qt_rectangle = window.frameGeometry()
    # retrieving the center point of the desktop (will depend on desktop resolution)
    center_point = QDesktopWidget().availableGeometry().center()
    # moving the center of window to the center of the desktop
    qt_rectangle.moveCenter(center_point)
    window.move(qt_rectangle.topLeft())
    layout = QGridLayout()
    # creating field size selection label
    set_field_size = QLabel('Set field size:')
    set_field_size.setAlignment(Qt.AlignCenter)
    layout.addWidget(set_field_size, 1, 1)
    # creating mime number setting label
    set_mime_number = QLabel('Set mime population:')
    set_mime_number.setAlignment(Qt.AlignCenter)
    layout.addWidget(set_mime_number, 1, 2)
    # creating small size button
    small_size = QPushButton('Small 10x10')
    small_size.setCheckable(True)
    small_size.clicked.connect(lambda: window.size_button_checked(small_size, 430, 450, 10, 10))
    window.size_buttons.append(small_size)
    # creating medium size button
    layout.addWidget(small_size, 2, 1)
    medium_size = QPushButton('Medium 15x15')
    medium_size.setCheckable(True)
    medium_size.clicked.connect(lambda: window.size_button_checked(medium_size, 645, 670, 15, 15))
    window.size_buttons.append(medium_size)
    layout.addWidget(medium_size, 3, 1)
    # creating large size button
    large_size = QPushButton('Large 20x20')
    large_size.setCheckable(True)
    large_size.clicked.connect(lambda: window.size_button_checked(large_size, 860, 885, 20, 20))
    window.size_buttons.append(large_size)
    layout.addWidget(large_size, 4, 1)
    # creating ten mimes button
    ten_mimes = QPushButton('10 mimes')
    ten_mimes.setCheckable(True)
    window.mime_pop_buttons.append(ten_mimes)
    ten_mimes.clicked.connect(lambda: window.mime_pop_button_checked(ten_mimes, 10))
    layout.addWidget(ten_mimes, 2, 2)
    # creating twenty mimes button
    twenty_mimes = QPushButton('20 mimes')
    twenty_mimes.setCheckable(True)
    window.mime_pop_buttons.append(twenty_mimes)
    twenty_mimes.clicked.connect(lambda: window.mime_pop_button_checked(twenty_mimes, 20))
    layout.addWidget(twenty_mimes, 3, 2)
    # creating thirty mimes button
    thirty_mimes = QPushButton('30 mimes')
    thirty_mimes.setCheckable(True)
    window.mime_pop_buttons.append(thirty_mimes)
    thirty_mimes.clicked.connect(lambda: window.mime_pop_button_checked(thirty_mimes, 30))
    layout.addWidget(thirty_mimes, 4, 2)
    # creating proceed button
    proceed = QPushButton('** PROCEED **')
    proceed.clicked.connect(window.close)
    layout.addWidget(proceed, 5, 1, 1, 2)

    layout.setSpacing(0)
    window.setLayout(layout)
