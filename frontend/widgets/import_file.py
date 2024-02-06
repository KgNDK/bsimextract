"""
Importing file widget
"""

"""
# TODO LIST

# TODO: Change the warning toplevel widget to a modular one from function. This needs to be created first
"""

"""
Importing extern modules
"""
import tkinter as tk
from tkinter import filedialog, ttk, Label
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *

class import_file(ctk.CTkFrame):
    def __init__(self, parent, text_button = "Import Data"):
        super().__init__(master = parent, fg_color = FG_COLOR)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)
        
        # grid layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((0), weight = 1, uniform = "a")
        self.columnconfigure((1), weight = 2, uniform = "a")

        self.entry_var = tk.StringVar(self)

        ctk.CTkButton(self, text = text_button, command = self.browse_file, width = STANDARD_COLUMN_WIDTH_3, font = text_font).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, textvariable = self.entry_var, state = "readonly", width = STANDARD_COLUMN_WIDTH_2_3).grid(row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Tekstfiler", "*.txt"), ("Alle filer", "*.*")])
        if file_path and not os.path.basename(file_path).startswith("dayprofile"):
            self.entry_var.set(os.path.basename(file_path))
        if file_path and os.path.basename(file_path).startswith("dayprofile"):
            self.show_warning("You have tried to import a dayprofile file. Please try importing BSim Data in a .txt format instead.")
        if file_path and os.path.basename(file_path).startswith("requirement"):
            self.show_warning("You have tried to import the requirements file. Please try importing BSim Data in a .txt format instead.")
        if file_path and not os.path.basename(file_path).endswith("txt"):
            self.show_warning("The file you have tried to import is not a .txt file. Please try importing BSim Data in a .txt format instead.")
    
    def show_warning(self, text_msg = "You have tried to import a dayprofile. Please try importing BSim Data in a .txt format instead."):
        msg = CTkMessagebox(message = text_msg,
                            title = "Warning Message!",
                            icon = "warning",
                            option_1 = "Cancel",
                            option_2 = "Retry")
        response = msg.get()

        if response == "Retry":
            self.browse_file()
        elif response == "Cancel":
            pass



if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: import_file")
    root.geometry("400x50")

    import_file(root).pack()

    root.mainloop()