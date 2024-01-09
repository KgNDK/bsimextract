"""
main file
"""
import tkinter as tk
import customtkinter as ctk

from frontend.widgets.title_menu import *
from settings.settings import *

class app(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__()
        ctk.set_appearance_mode(COLOR_MODE)
        self.geometry("1600x1000")
        self.title(f"BSimExtract {VERSION_NUMBER}")
        self.minsize(800, 500)

        # layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((1, 2, 3), weight = 1)
        self.columnconfigure((0), weight = 1)

        # title menu
        title_menu(self)

        # widgets





        
        self.mainloop()

       

app()

    