
import sys
from PyQt6.QtWidgets import QApplication, QScrollArea, QVBoxLayout, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from dictionary_api import DictionaryAPI, WordData
from audio_player import playurl
from database import DictionaryDB

class SearchResult(QWidget):
    def __init__(self, word_data: WordData):
        super().__init__()
        # Allows CSS for #SearchResult to be applied to this object
        self.setObjectName("SearchResult")
        # Specifically needed for background-color changes
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.word_data = word_data
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.result_label = QLabel(str(self.word_data))
        self.result_label.setWordWrap(True)
        grid.addWidget(self.result_label, 0, 0, 3, 2)

        self.listen_button = QPushButton('Listen')
        self.listen_button.clicked.connect(self.play_phonetics)
        grid.addWidget(self.listen_button, 3, 0, 1, 2)

    def play_phonetics(self):
        if self.word_data.get_audio_url() != "":
            self.disable_listen_button()
            playurl(self.word_data.get_audio_url(), self.enable_listen_button)

    def disable_listen_button(self):
        self.listen_button.setEnabled(False)

    def enable_listen_button(self):
        self.listen_button.setEnabled(True)

    def add_to_favourites(self):
        if self.word_data is not None:
            db = DictionaryDB()
            db.add_word(self.word_data)

class DictionaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.dictionary_api = DictionaryAPI()
        self.results_list = []

    def init_ui(self):
        self.setGeometry(100, 100, 600, 400)

        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.grid)
        
        self.search_bar = QLineEdit()
        self.search_bar.setMaxLength(25)
        self.grid.addWidget(self.search_bar, 0, 0, 1, 2)

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_word)
        self.grid.addWidget(self.search_button, 0, 2)
        
        self.results_area = QScrollArea()
        self.results_area.setWidgetResizable(True)
        self.results_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.results_container = QWidget()
        self.results_layout = QVBoxLayout(self.results_container)
        self.results_area.setWidget(self.results_container)

        self.grid.addWidget(self.results_area, 1, 0, 1, 3)

        self.setWindowTitle('Dictionary')
        self.show()

    def search_word(self):
        # Clear the previous results
        for widget in self.results_list:
            widget.setParent(None)
        self.results_list.clear()

        # Get the word from the search bar
        word = self.search_bar.text()
        # Get the word data from the API
        dictionary_result = self.dictionary_api.get_word_data(word)

        # Add the results to the gui
        if dictionary_result is not None:
            for word_data in dictionary_result:
                search_result_widget = SearchResult(word_data)
                self.results_layout.addWidget(search_result_widget)
                self.results_list.append(search_result_widget)

app = QApplication(sys.argv)
app.setStyleSheet(open("PyQT6/style.css").read())
ex = DictionaryApp()
sys.exit(app.exec())