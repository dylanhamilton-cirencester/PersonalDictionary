from tkinter import Text
from customtkinter import END, CTkButton, CTkFont, CTkFrame, CTkLabel, CTkScrollableFrame
from dictionary_api import DictionaryAPI
from word_section import WordSectionFrame

class WordSearchFrame(CTkFrame):
    
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.audio_url = ""

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.dict_api = DictionaryAPI()

        # add widgets onto the frame

        # Row 0

        self.search_label = CTkLabel(self, text="Search for a word", height=20)
        self.search_label.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="ew")

        # Row 1

        self.search_box = Text(self, height=1, font=CTkFont())
        self.search_box.grid(row=1, column=0, sticky="we", padx=20, columnspan=2)
        self.search_box.insert("0.0", "")

        self.search_button = CTkButton(self, text="Search", command=self.search)
        self.search_button.grid(row=1, column=2, padx=20, sticky="w")

        # Row 2
        self.grid_rowconfigure(2, weight=2)

        self.dictionary_words_frame = CTkScrollableFrame(self)
        self.dictionary_words_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10, columnspan=3)
        self.dictionary_words_frame.grid_columnconfigure(0, weight=1)
        # We will add the words to this frame later


    def search(self):
        # Clear previous results
        for widget in self.dictionary_words_frame.winfo_children():
                widget.destroy()

        # Display definitions
        word = self.search_box.get(0.0, END)
        word_datas = self.dict_api.get_word_data(word)

        if len(word_datas) == 0:
            no_results_label = WordSectionFrame(self.dictionary_words_frame, controller=self.controller, text="No results found.", show_favourite_button=False)
            no_results_label.grid(row=0, column=0, sticky="nsew", padx=20, pady=20, columnspan=3)
        else:
            for i, word_data in enumerate(word_datas):
                word_section_frame = WordSectionFrame(
                    self.dictionary_words_frame,
                    controller=self.controller,
                    word_data=word_data,
                    audio_url=word_data.get_audio_url(),
                )
                word_section_frame.grid(row=i, column=0, sticky="nsew", padx=20, pady=20, columnspan=3)

        # Set up audio play
        if word_datas:
            self.audio_url = word_datas[0].get_audio_url()
        else:
            self.audio_url = ""


    

