"""
Main file
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
import pandas as pd

"""
Importing internal modules
"""
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
        self.init_parameters()

        
        # layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((0), weight = 1)
        self.columnconfigure((1, 2, 3), weight = 6)

        # title menu
        title_menu(self)

        # widgets
        page_menu(self, self.co2_dayprofile, self.rh_dayprofile, self.temp_dayprofile, self.airch_dayprofile).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        self.mainloop()

    def init_parameters(self):
        # variables
        self.co2_dayprofile = ctk.StringVar()
        self.rh_dayprofile = ctk.StringVar()
        self.temp_dayprofile = ctk.StringVar()
        self.airch_dayprofile = ctk.StringVar()

        # # trace testing
        # self.co2_dayprofile.trace("w", self.update_test)
        # self.rh_dayprofile.trace("w", self.update_test)
        # self.temp_dayprofile.trace("w", self.update_test)
        # self.airch_dayprofile.trace("w", self.update_test)

    # # trace testing
    # def update_test(self, *args):
    #     print(self.co2_dayprofile.get())
    #     print(self.rh_dayprofile.get())
    #     print(self.temp_dayprofile.get())
    #     print(self.airch_dayprofile.get())


        
        

       

app()

    