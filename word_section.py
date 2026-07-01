
from dictionary_api import WordData
from customtkinter import CTkFrame


class WordSection(CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.audio_url = ""
        self.current_word_data: WordData | None = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        