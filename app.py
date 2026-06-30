from customtkinter import CTk, set_default_color_theme
from word_search import WordSearchFrame

class App(CTk):
    def __init__(self):
        set_default_color_theme("theme.json")
        super().__init__()
        self.geometry("500x400")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = WordSearchFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()