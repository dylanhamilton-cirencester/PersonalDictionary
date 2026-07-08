from customtkinter import CTk, set_default_color_theme
from favourites import FavouritesFrame
from word_search import WordSearchFrame
from tkinter import Menu

class App(CTk):
    def __init__(self):
        set_default_color_theme("CustomTKinter/theme.json")
        super().__init__()
        self.geometry("600x400")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.menu = Menu(self)
        self.config(menu=self.menu)

        self.menu.add_command(label="Search", command=self.open_word_search_frame)
        self.menu.add_command(label="Favourites", command=self.open_favourites_frame)

        self.my_frame = WordSearchFrame(master=self, controller=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    def open_word_search_frame(self):
        self.my_frame = WordSearchFrame(master=self, controller=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def open_favourites_frame(self):
        self.my_frame = FavouritesFrame(master=self, controller=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

app = App()
app.mainloop()