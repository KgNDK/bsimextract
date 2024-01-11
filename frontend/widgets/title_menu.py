"""
title menu for file, edit, help, report bug and so on
"""

"""
# TODO LIST

# TODO: Redo the lambda functions so they work properly
# TODO: Make settings.py in this file
"""

"""
Importing extern modules
"""
import tkinter as tk
import customtkinter as ctk
from CTkMenuBar import *

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *

class title_menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # title menu
        self.menu = CTkTitleMenu(parent)

        # main title menu buttons
        self.button_file = self.menu.add_cascade("File",
                                                 font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        self.button_edit = self.menu.add_cascade("Settings",
                                                 command=lambda: print("Opening Settings"),
                                                 font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                                  size=TITLE_MENU_SIZE,
                                                                  weight=TITLE_MENU_WEIGHT))
        self.button_help = self.menu.add_cascade("Help",
                                                 command=lambda: print("Opening Github Wiki"),
                                                 font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                                  size=TITLE_MENU_SIZE,
                                                                  weight=TITLE_MENU_WEIGHT))
        self.button_report = self.menu.add_cascade("Report Bug",
                                                   command=lambda: print("Opening Github"),
                                                   font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                                    size=TITLE_MENU_SIZE,
                                                                    weight=TITLE_MENU_WEIGHT))

        # file dropdown menu
        self.menu_dropdown_1 = CustomDropdownMenu(widget=self.button_file)
        # self.menu_dropdown_1.add_option(option="Import Data",
        #                                 command=lambda: print("Import Data"),
        #                                 font=ctk.CTkFont(family=TITLE_MENU_FONT,
        #                                                  size=TITLE_MENU_SIZE,
        #                                                  weight=TITLE_MENU_WEIGHT))
        self.menu_dropdown_1.add_option(option="Open",
                                        command=lambda: print("Opening file"),
                                        font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        self.menu_dropdown_1.add_option(option="Save",
                                        command=lambda: print("Save"),
                                        font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        self.menu_dropdown_1.add_option(option="Save As",
                                        command=lambda: print("Save As"),
                                        font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        self.menu_dropdown_1.add_option(option="Save Report",
                                        command=lambda: print("Save Report"),
                                        font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))

        

if __name__ == "__main__":  
    root = ctk.CTk()
    
    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: tile_menu")
    root.geometry("800x300")

    title_menu(root).pack()

    root.mainloop()
