dark_grey = """

QMenuBar {
            spacing: 2px;
            background-color: #7c8e9c;
}

QMenuBar::item {   
            background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:3, stop:0 #7c8e9c, stop:1 000066);         
            padding: 5px 25px;
            color: #e2e6e9;            
}

QMenuBar::item::selected {
            background-color: #d3d9de;
            color: #161a1d;
}

QMenu {   
        background-color: #7c8e9c;   
}

QMenu::item {                         
            color: #e2e6e9;
}

QMenu::item::selected {
        background-color: #d3d9de;
        color: #161a1d;
}

QToolBar { 
        padding: 4px 5px;
        spacing: 10px;
        background-color: #7c8e9c;   
}

QToolButton {        
        background-color: #7c8e9c;        
        color: #e2e6e9;                  
}

QPushButton {        
        background-color: #7c8e9c;
        font-size: 25px;
        color: #e2e6e9;                  
}

QPushButton::checked {  
        border-style: inset; 
        border-width: 5px;                
}

QMessageBox {        
        background-color: #7c8e9c;
}

QMessageBox QLabel {
        color: #e2e6e9;
}

QMessageBox QPushButton {         
        background-color: #7c8e9c;
        font-size: 15px;
        color: #e2e6e9;
}

QDialog {
        background-color: #7c8e9c;        
}

QDialog QPushButton {         
        background-color: #7c8e9c;
        color: #e2e6e9;
}

QDialog QLabel{
        color: #e2e6e9;
}

QStatusBar QLineEdit {
        color: #e2e6e9; 
        border: none; 
        background-color: #7c8e9c; 
        border-radius: 2px;
}

"""

mime_tile_checked = """

QPushButton {
        background-color: #990000; 
        border-color: #b30000;
}

"""

zero_tile_checked = """

QPushButton {
        background-color: #66cc66; 
        color: white; 
        border-color: #53c653;
}

"""

number_tile_checked = """

QPushButton {
        background-color: #ff8000; 
        color: blue; 
        border-color: #e67300;
}

"""