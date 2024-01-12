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
import webbrowser
import CTkMessagebox as CTkMessagebox

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

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # title menu
        self.menu = CTkTitleMenu(parent)

        # main title menu buttons
        self.button_file = self.menu.add_cascade("File",
                                                 font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        self.button_edit = self.menu.add_cascade("Settings",
                                                 command=self.open_settings,
                                                 font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                                  size=TITLE_MENU_SIZE,
                                                                  weight=TITLE_MENU_WEIGHT))
        self.button_help = self.menu.add_cascade("Help",
                                                 command=lambda: webbrowser.open("https://github.com/KgNDK/bsimextract/wiki"),
                                                 font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                                  size=TITLE_MENU_SIZE,
                                                                  weight=TITLE_MENU_WEIGHT))
        self.button_report = self.menu.add_cascade("Report Bug",
                                                   command=lambda: webbrowser.open("https://github.com/KgNDK/bsimextract/issues"),
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
                                        command=self.open,
                                        font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        self.menu_dropdown_1.add_option(option="Save",
                                        command=self.save,
                                        font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        self.menu_dropdown_1.add_option(option="Save As",
                                        command=self.save_as,
                                        font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        self.menu_dropdown_1.add_option(option="Save Report",
                                        command=self.save_report,
                                        font=ctk.CTkFont(family=TITLE_MENU_FONT,
                                                         size=TITLE_MENU_SIZE,
                                                         weight=TITLE_MENU_WEIGHT))
        
    def open_settings(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Manual adjustment of settings is not yet implemented. Please go to source code settings.py to change settings.", icon = "warning")

    def open(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Opening of existing files is not yet implemented", icon = "warning")

    def save(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Saving of the current file is not yet implemented", icon = "warning")

    def save_as(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Saving of the current file in specified location is not yet implemented", icon = "warning")

    def save_report(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Saving finalized report is not yet implemented", icon = "warning")

        


if __name__ == "__main__":  
    root = ctk.CTk()
    
    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: tile_menu")
    root.geometry("800x300")

    title_menu(root).pack()

    root.mainloop()
