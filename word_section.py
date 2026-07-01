from audio_player import playurl
from dictionary_api import WordData
from customtkinter import DISABLED, NORMAL, CTkButton, CTkFont, CTkFrame, CTkLabel, CTkTextbox, ThemeManager
from database import DictionaryDB

class DefinitionLabel(CTkTextbox):
    def __init__(self, master, **kwargs):
        
        theme = ThemeManager.theme

        my_theme = theme.get("DefinitionLabel", {})

        # Merge theme values with kwargs (kwargs override theme)
        merged_kwargs = {**my_theme, **kwargs}

        super().__init__(master, wrap="word", **merged_kwargs)


class WordSectionFrame(CTkFrame):
    def __init__(
        self,
        master=None,
        controller=None,
        word_data: WordData | None = None,
        text="",
        audio_url="",
        show_favourite_button=True,
        is_favourite=False,
        **kwargs,
    ):
        super().__init__(master, **kwargs)

        self.controller = controller
        self.audio_url = audio_url
        self.word_data = word_data

        if word_data is not None:
            text = str(word_data)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        
        self.word_def_label = DefinitionLabel(self, font=CTkFont())
        self.word_def_label.grid(row=0, column=0, sticky="nesw", padx=20, pady=20, columnspan=3)
        self.word_def_label.insert(0.0, text)
        self.word_def_label.configure(state=DISABLED)

        if show_favourite_button:
            if is_favourite:
                self.favorite_button = CTkButton(self, text="Remove from Favourites", command=self.remove_from_favourites)
                self.favorite_button.grid(row=1, column=0, padx=20, pady=20, sticky="w")
            else:
                self.favorite_button = CTkButton(self, text="Add to Favourites", command=self.add_to_favourites)
                self.favorite_button.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        if self.audio_url != "":
            self.audio_play_button = CTkButton(self, text="Listen", command=self.play_phonetics)
            self.audio_play_button.grid(row=1, column=2, padx=20, sticky="w", columnspan=1)
            # Add some space under the button
            self.spacer_label = CTkLabel(self, text="")
            self.spacer_label.grid(row=2, column=0, padx=10, sticky="w", columnspan=3)

    def play_phonetics(self):
        if self.audio_url != "":
            self.disable_listen_button()
            playurl(self.audio_url, self.enable_listen_button)

    def disable_listen_button(self):
        self.audio_play_button.configure(state = DISABLED)

    def enable_listen_button(self):
        self.audio_play_button.configure(state = NORMAL)

    def add_to_favourites(self):
        if self.word_data is not None:
            db = DictionaryDB()
            db.add_word(self.word_data)

    def remove_from_favourites(self):
        if self.word_data is not None:
            db = DictionaryDB()
            if not self.word_data.id:
                raise ValueError("WordData object must have an id to be removed from favourites.")
            db.remove_word(self.word_data.id)

            # Reload window to reflect changes
            if self.controller is not None:
                self.controller.open_favourites_frame()
        