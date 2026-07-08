# PyQt6 Intro

A beginners guide to using PyQt6.

## What is PyQt6

PyQt6 is a wrapper for a cpp framework used to create graphical user interfaces (GUI).

## How to start

Firstly you will need to install the library using pip. Assuming you have python and pip installed you will need to run

`pip install PyQt6`

to install PyQt6 on your system.

Once this is done we can start programming using PyQt6.

## My First GUI

This section will lay out a simple gui with text input, buttons and some layouts to help you understand how to use this library.

Below is some sample code, follow along step by step to help you understand how to make this from scratch in the future.

### Import components

Firstly we will have to import all the components we are going to use in this application. Mainly, the application class, the specific widgets we will use and some other functionality that will be useful.

```python
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt
```

### Create your app

Here is an example app with a __Label__, __Text input__ and a __Button__. For now they won't do anything but show up on the screen.

We will also use a layout, specifically the grid layout which is the most common and powerful layout available and quite easy to use.

```python
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # First set the window position and size
        self.setGeometry(100, 100, 300, 400)

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

        # Add the name of the window to the app
        self.setWindowTitle('My App')
        # Show the app, windows are hidden by default so make sure you add this!
        self.show()
```

This might seem like a lot, but we will break it down piece by piece.

Firstly, we have to create a window. We can do this by inheriting from the __QWidget__ class.

```python
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
```

> Make sure to call `super().__init__()` in your `__init__` method or the window will not work at all

We also call `init_ui` in our `__init__` method to load all of the gui elements for ease.

Let's look at that method now.

At the top of that method we use `setGeometry` the first two arguments are the x and y positions for the app to appear on the screen, the next two arguments are the width and height of your application. Both of these are in pixels.

Next we add a `QGridLayout` to the window. This allows us to easily arrange our widgets later on and let them automatically scale with the window size.

After this we add some widgets. Each widget has different constructors so you will have to look them up and see what arguments they take. For this app we use `QLabel`, `QLineEdit` and `QPushButton`. These will be the most common ones you will use but you may want to use others so get comfortable with looking up the documentation for this.

You can find the documentation for PyQT6 Widgets [here](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#module-PySide6.QtWidgets).

We can also name our window with `setWindowTitle`.

Finally make sure to use the `show` method to have the window display anything. This is not done by default so if nothing shows up, this is probably the issue.

The last step is to create an application and run our window inside it.

```python
# Create an app
app = QApplication(sys.argv)
# Load our window
ex = MyApp()
# Run the app
sys.exit(app.exec())
```