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
# The widgets we will use
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
# Common flags for alignment and other features
from PyQt6.QtCore import Qt
# Access to the system and system information
import sys
```

### Create your app

Here is an example app with a **Label**, **Text input** and a **Button**. For now they won't do anything but show up on the screen.

We will also use a layout, specifically the grid layout which is the most common and powerful layout available and quite easy to use.

```python
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

        # Add the name of the window to the app
        self.setWindowTitle('My App')
        # Show the app, windows are hidden by default so make sure you add this!
        self.show()
```

This might seem like a lot, but we will break it down piece by piece.

Firstly, we have to create a window. We can do this by inheriting from the `QWidget` class.

```python
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
```

> Make sure to call `super().__init__()` in your `__init__` method or the window will not work at all

We also call `init_ui` in our `__init__` method to load all of the gui elements for ease.

---

#### Let's look at that method now.

At the top of that method we use `setGeometry`.

```python
# First set the window position and size
self.setGeometry(100, 100, 300, 200)
```

The first two arguments are the **x** and **y** positions for the app to appear on the screen.\
The next two arguments are the **width** and **height** of your application. Both of these are in pixels.

Next we add a `QGridLayout` to the window.\
This allows us to easily arrange our widgets later on and let them automatically scale with the window size.

```python
# Add a layout
self.grid = QGridLayout()
self.grid.setAlignment(Qt.AlignmentFlag.AlignTop)
self.setLayout(self.grid)
```

The first line creates the grid layout.\
The second sets the alignment of this layout so that it builds down from the top (other options are available).\
Finally we set the layout of our window to the grid we've just made.

---

After this we add some widgets.\
Let's look at a the `QLabel` for now.\

```python
# Add a label to the application
self.label = QLabel("Welcome!")
self.grid.addWidget(self.label, 0, 0)
```

Firstly, we create the label and set it's text to say "Welcome!"
The only thing left is to place it in our grid.\
We use `addWidget` on the `grid` to add the label.\
The first parameter is the widget we wish to add, then we set what **row** and **column** we want the widget to be in.\
We can also have elements go over multiple rows and/or columns. Check out he [documentation for QGridLayout](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGridLayout.html) to find out how.

---

Here are some other widget we can add and place them in our grid.

```python
# Add a text input
self.text_input = QLineEdit()
# Add that to the grid layout in row 0, column 0
self.grid.addWidget(self.text_input, 1, 0)

# Add a button
self.my_button = QPushButton("Press Me")
self.grid.addWidget(self.my_button, 2, 2, 0, 1)
```

Each widget has different constructors so you will have to look them up and see what arguments they take.\
For this app we use `QLabel`, `QLineEdit` and `QPushButton`.\
These will be the most common ones you will use but you may want to use others so get comfortable with looking up the documentation for this.

You can find the documentation for PyQT6 Widgets [here](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#module-PySide6.QtWidgets).

---

We can also name our window with `setWindowTitle`.

```python
# Add the name of the window to the app
self.setWindowTitle("My App")
```

Finally make sure to use the `show` method to have the window display anything. This is not done by default so if nothing shows up, this is probably the issue.

```python
# Show the app, windows are hidden by default so make sure you add this!
self.show()
```

---

The last step is to create an application and run our window inside it.

```python
# Create an app
app = QApplication(sys.argv)
# Load our window
ex = MyApp()
# Run the app
sys.exit(app.exec())
```

---

## Signals and Slots

If you followed this document closely you'll have a working app.\
However, it doesn't do much at the moment, let's change that.

Let's make the button do something shall we?

In PyQt6 we use **signals** and **slots**.

A **signal** is send when an action is performed.

A **slot** is any function that we want to be called when the **signal** is sent.

Starting with **slot**. An example of one in our program might be.

```python
def set_label_text():
    text = self.text_input.text()
    self.label.setText(text)
```

> Note: Make sure this method is inside your MyApp class for it to access the text_input and label widgets.


An example of a **signal** in our program:\
`QPushButton` has a `clicked` signal we can access like this `self.my_button.clicked`.\
And to add the **slot** to this **signal** we can call the `emit` method.

```python
...
# Add a button
self.my_button = QPushButton("Press Me")
self.my_button.clicked.connect(self.set_label_text)
self.grid.addWidget(self.my_button, 1, 1)
...

```

Try this out and see what other signals you can find.

### Further Reading

**Events**

Events are built in signals that widgets have that you can overwrite and run code when certain actions are performed by the user e.g. `mousePressEvent`.\
Look up the documentation for more information

---

## Styles

Lastly we will look at how to make your program look good.\
If you have used CSS before this part will be very easy for you, if not don't worry, it is very simple.

Firstly you will need to create a file with the `.css` extension e.g. `my-style.css`

In the file you will put all of your styles for different widgets.

Here is an example of using css in PyQt6.

Here is an example for changing the background colour, text colour, border and padding for all `QPushButton`s in our project.

```css
QPushButton {
    background-color: #3A7EBF;
    color: white;
    border-radius: 5px;
    padding: 5px 10px;
}
```

We start by calling using the name of the class, then in a set of curly brackets we can use normal css properties to change what our button looks like.

The only thing left is to tell our program to use `my-style.css`.\
At the bottom of our scrip we can add this line.

```python
...
app = QApplication(sys.argv)
# This line will tell our program to 
app.setStyleSheet(open("my-style.css").read())
ex = MyApp()
sys.exit(app.exec())
...
```

Doing this did remove the `hover` and `pressed` styles so if you want to add those back in you can add new styles for those too.

```css
QPushButton:hover {...}

QPushButton:pressed {...}
```

> These key words after the colons are called pseudo-classes, they control the actions that can be taken or the positions or language of elements on a page

Another way to change the look of individual elements is by using object names. These work the same as ids in html.

Start by giving your widget an object name. Here I have created a custom widget and added an attribute to that.

```python
class CustomButton(QPushButton):

    def __init__(self):
        super().__init__("Unpressed")
        self.setObjectName("RedButton")
        self.clicked.connect(self.do_press)

    def do_press(self):
        self.setText("Pressed")
```

Then you can add the css using the **#** symbol before the object name.

```css
/* my-style.css */
#RedButton {
    background-color: #bf3a3a;
}
```
