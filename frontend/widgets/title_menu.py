"""
title menu for file, edit, help, report bug and so on
"""

# TODO: Redo the lambda functions so they work properly
# TODO: Make settings.py in this file

import tkinter as tk
import customtkinter as ctk
from CTkMenuBar import *

class title_menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # title menu
        self.menu = CTkTitleMenu(parent)

        # main title menu buttons
        self.button_file = self.menu.add_cascade("File")
        self.button_edit = self.menu.add_cascade("Settings", command=lambda: print("Opening Settings"), font=TITLE_MENU_FONT)
        self.button_help = self.menu.add_cascade("Help", command=lambda: print("Opening Github Wiki"), font=TITLE_MENU_FONT)
        self.button_report = self.menu.add_cascade("Report Bug", command=lambda: print("Opening Github"), font=TITLE_MENU_FONT)

        # file dropdown menu
        self.menu_dropdown_1 = CustomDropdownMenu(widget=self.button_file)
        self.menu_dropdown_1.add_option(option="Import Data", command=lambda: print("Importing data"), font=TITLE_MENU_FONT)
        self.menu_dropdown_1.add_option(option="Open", command=lambda: print("Opening file"), font=TITLE_MENU_FONT)
        self.menu_dropdown_1.add_option(option="Save As", command=lambda: print("Save As"), font=TITLE_MENU_FONT)
        self.menu_dropdown_1.add_option(option="Save Report", command=lambda: print("Save Report"), font=TITLE_MENU_FONT)



if __name__ == "__main__":  
    root = ctk.CTk()

    #! TO BE REMOVED - TEMPORARY SETTINGS
    TITLE_FONT = ctk.CTkFont(family="montserrat", size=20, weight="bold")
    TEXT_FONT= ctk.CTkFont(family="montserrat", size=12)
    TITLE_MENU_FONT= ctk.CTkFont(family="montserrat", size=12)
    PAGE_MENU_FONT = ctk.CTkFont(family="montserrat", size=14, weight="bold")
    COLOR_1 = "#f6f6f4"
    COLOR_2 = "#edeae5"
    COLOR_3 = "#ced9dd"
    COLOR_4 = "#979fa5"
    COLOR_5 = "#2f3d4c"
    COLOR_MODE = "dark"

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: tile_menu")
    root.geometry("800x300")

    title_menu(root).pack()

    root.mainloop()
