from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt
import sys

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # First set the window position and size
        self.setGeometry(100, 100, 300, 200)

        # Add a layout
        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.grid)

        # Add a label to the application
        self.label = QLabel("Welcome!")
        self.grid.addWidget(self.label, 0, 0)

        # Add a text input
        self.text_input = QLineEdit()
        # Add that to the grid layout in row 0, column 0
        self.grid.addWidget(self.text_input, 1, 0)

        # Add a button
        self.my_button = QPushButton("Press Me")
        self.grid.addWidget(self.my_button, 2, 0)

        self.setWindowTitle('My App')
        self.show()

app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec())