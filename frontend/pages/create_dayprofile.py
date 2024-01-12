"""
Toplevel page for creating a custom dayprofile
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
from CTkMenuBar import *
import webbrowser

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *

class create_dayprofile(ctk.CTkToplevel):
    def __init__(self, parent, text_top_title = "Create a new dayprofile:"):
        super().__init__(master = parent)

        # setup
        self.title(text_top_title)
        self.geometry("600x400")

        # grid layout
        self.rowconfigure((1, 2, 3, 4, 5), weight = 1)
        # self.rowconfigure((0, 6))
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26), weight = 1)
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # text
        ctk.CTkLabel(self, text = "This page is currently under construction. Please check back later!", font = title_font).grid(row = 0, column = 0, columnspan = 25, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Please mark all the boxes that the dayprofile should be active for", font = text_font).grid(row = 6, column = 0, columnspan = 20, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Hours:", font = text_font).grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Days:", font = text_font).grid(row = 2, column = 0, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Weeks:", font = text_font).grid(row = 3, column = 0, rowspan = 2, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Months:", font = text_font).grid(row = 5, column = 0, sticky = "nsew", padx = 5, pady = 5)


        # button
        ctk.CTkButton(self, text = "Create dayprofile", command = self.make_dayprofile, font = text_font).grid(row = 6, column = 26, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkButton(self, text = "Open dayprofile", command = self.open_dayprofile, font = text_font).grid(row = 0, column = 26, sticky = "nsew", padx = 5, pady = 5)


    def make_dayprofile(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Creating a new dayprofile_XXX.txt file is not yet implemented", icon = "warning")

    def open_dayprofile(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Opening of an existing dayprofile_XXX.txt file is not yet implemented", icon = "warning")


if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode(COLOR_MODE)
    root.geometry("200x10")
    create_dayprofile(root)
    root.mainloop()