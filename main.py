"""
Main file
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
import customtkinter as ctk

"""
Importing internal modules
"""
# import sys
# sys.path.append("c:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract")
from settings.settings import *
from frontend.widgets.title_menu import title_menu
from frontend.widgets.page_menu import page_menu



class app(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__()
        ctk.set_appearance_mode(COLOR_MODE)
        self.geometry("1800x1000")
        self.title(f"BSimExtract {VERSION_NUMBER}")
        self.minsize(800, 500)

        # layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((0), weight = 1)
        self.columnconfigure((1, 2, 3), weight = 6)

        # title menu
        title_menu(self)

        # widgets
        page_menu(self).grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)




        
        self.mainloop()

       

app()

    