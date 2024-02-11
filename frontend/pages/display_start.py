"""
Frame for displaying Start data visually
This will be showing the raw data in a table so the user can see the data has been imported correctly
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
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


class display_start(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)

        # layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((0), weight = 1)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # label
        ctk.CTkLabel(self, text = "Start", font = title_font).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        


if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: display_start")
    root.geometry("800x300")

    display_start(root).pack()

    root.mainloop()