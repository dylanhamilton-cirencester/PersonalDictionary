from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt
import sys

class CustomButton(QPushButton):

    def __init__(self):
        super().__init__("Unpressed")
        self.setObjectName("RedButton")
        self.clicked.connect(self.do_press)

    def do_press(self):
        self.setText("Pressed")


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
        self.grid.addWidget(self.label, 0, 0,)

        # Add a text input
        self.text_input = QLineEdit()
        # Add that to the grid layout in row 0, column 0
        self.grid.addWidget(self.text_input, 1, 0)

        # Add a button
        self.my_button = QPushButton("Press Me")
        self.my_button.clicked.connect(self.set_label_text)
        self.grid.addWidget(self.my_button, 1, 1)

        # Add custom button
        self.custom_button = CustomButton()
        self.grid.addWidget(self.custom_button, 2, 0, 2, 2)

        # Add the name of the window to the app
        self.setWindowTitle('My App')
        # Show the app, windows are hidden by default so make sure you add this!
        self.show()

    def set_label_text(self):
        text = self.text_input.text()
        self.label.setText(text)


app = QApplication(sys.argv)
app.setStyleSheet(open("PyQT6/my-style.css").read())
ex = MyApp()
sys.exit(app.exec())