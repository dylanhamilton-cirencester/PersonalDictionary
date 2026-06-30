from tkinter import Label, Text
from typing import Any, Tuple
from customtkinter import END, CTkButton, CTkFont, CTkFrame, CTkLabel, ThemeManager
from dictionary_api import DictionaryAPI, WordData
from audio_player import playurl

class DefinitionLabel(CTkLabel):
    def __init__(self, master, **kwargs):
        
        theme = ThemeManager.theme

        my_theme = theme.get("DefinitionLabel", {})

        # Merge theme values with kwargs (kwargs override theme)
        merged_kwargs = {**my_theme, **kwargs}

        super().__init__(master, text = "", **merged_kwargs)

        self.bind('<Configure>', lambda e: self.configure(wraplength=self.winfo_width() * 0.75))

class WordSearchFrame(CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.audio_url = ""

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.dict_api = DictionaryAPI()

        # add widgets onto the frame

        # Row 0

        self.search_label = CTkLabel(self, text="Search for a word", height=20)
        self.search_label.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="ew")

        self.audio_play_button = CTkButton(self, text="Listen", command=self.play_phonetics)
        self.audio_play_button.grid(row=0, column=2, padx=20, sticky="w")

        # Row 1

        self.search_box = Text(self, height=1, font=CTkFont())
        self.search_box.grid(row=1, column=0, sticky="we", padx=20, columnspan=2)
        self.search_box.insert("0.0", "")

        self.search_button = CTkButton(self, text="Search", command=self.search)
        self.search_button.grid(row=1, column=2, padx=20, sticky="w")

        # Row 2
        self.grid_rowconfigure(2, weight=2)

        self.word_def_label = DefinitionLabel(self, font=CTkFont(), justify="left")
        self.word_def_label.grid(row=2, column=0, sticky="nesw", padx=20, pady=20, columnspan=3, rowspan=4)

    def search(self):
        # Display definition
        word = self.search_box.get(0.0, END)
        word_data = self.dict_api.get_word_data(word)
        self.word_def_label.configure(text = str(word_data))

        # Set up audio play
        if type(word_data) == WordData:
            self.audio_url = word_data.get_audio_url()
        else:
            self.audio_url = ""


    def play_phonetics(self):
        if self.audio_url != "":
            playurl(self.audio_url)

