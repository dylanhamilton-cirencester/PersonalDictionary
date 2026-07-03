from customtkinter import CTkFrame, CTkLabel, CTkScrollableFrame
from word_section import WordSectionFrame
from database import DictionaryDB

class FavouritesFrame(CTkFrame):
    
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.audio_url = ""

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.db = DictionaryDB()
        # add widgets onto the frame

        # Row 0

        self.favourites_label = CTkLabel(self, text="Favourites", height=20)
        self.favourites_label.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="ew")

        # Row 1
        self.grid_rowconfigure(1, weight=2)

        self.dictionary_words_frame = CTkScrollableFrame(self)
        self.dictionary_words_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10, columnspan=3)
        self.dictionary_words_frame.grid_columnconfigure(0, weight=1)
        
        # Get words from database and display them
        self.add_favourites()

    def add_favourites(self):
        # Display favourite words
        word_datas = self.db.get_words()

        if len(word_datas) == 0:
            no_results_label = WordSectionFrame(
                self.dictionary_words_frame,
                controller=self.controller,
                text="No favourite words. Add some from the search page",
                show_favourite_button=False,
            )
            no_results_label.grid(row=0, column=0, sticky="nsew", padx=20, pady=20, columnspan=3)
        else:
            for i, word_data in enumerate(word_datas):
                word_section_frame = WordSectionFrame(
                    self.dictionary_words_frame,
                    controller=self.controller,
                    word_data=word_data,
                    is_favourite=True,
                )
                word_section_frame.grid(row=i, column=0, sticky="nsew", padx=20, pady=20, columnspan=3)
