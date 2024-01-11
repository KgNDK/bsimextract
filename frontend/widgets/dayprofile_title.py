"""
Title of dayprofile widgets with create dayprofile button
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import CTkMessagebox as CTkMessagebox
import customtkinter as ctk

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES
from settings.settings import *


class dayprofile_title(ctk.CTkFrame):
    def __init__(self, parent, title_text = "Choose a dayprofile:"):
        super().__init__(master = parent, fg_color = FG_COLOR)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # grid layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((0, 1, 2), weight = 1, uniform="a")

        # text widgets
        ctk.CTkLabel(self, text = title_text, width = STANDARD_COLUMN_WIDTH_2_3, font = title_font).grid(row = 0, column = 0, columnspan = 2, sticky = "nsew", padx = 5, pady = 5)

        # button widget
        ctk.CTkButton(self, text = "Create dayprofile", command = self.create_dayprofile, width = STANDARD_COLUMN_WIDTH_3).grid(row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)

    def create_dayprofile(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Creation of dayprofiles is not yet implemented", icon = "warning")


if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: dayprofile_title")
    root.geometry("400x50")

    dayprofile_title(root).pack()

    root.mainloop()