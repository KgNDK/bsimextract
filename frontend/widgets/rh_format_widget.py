"""
Rh formatting of data widget where the user can choose max values and color formatting
"""

"""
# TODO LIST

# TODO: Make an error box appear when apply is pressed and the max value is not a int, nothing has been entered and max value is a float
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
from backend.apply_format import apply_format

class rh_format_widget(ctk.CTkFrame):
    def __init__(self, parent,
                 rh_minrh_var,
                 rh_lowmaxrh_var,
                 rh_maxrh_var,
                 rh_formatcolor_minrh_var,
                 rh_formatcolor_lowmaxrh_var,
                 rh_formatcolor_maxrh_var):
        
        super().__init__(master = parent, fg_color = FG_COLOR, width = 200)

        # grid layout
        self.rowconfigure((0, 1, 2), weight = 1)
        self.columnconfigure((0, 1, 2, 3), weight = 1)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # label
        ctk.CTkLabel(self, text = "RelHumid formatting", font = title_font, width = STANDARD_COLUMN_WIDTH_4).grid(row = 0, column = 0, columnspan = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Min", font = text_font, width = STANDARD_COLUMN_WIDTH_4).grid(row = 1, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Low,max", font = text_font, width = STANDARD_COLUMN_WIDTH_4).grid(row = 1, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Max", font = text_font, width = STANDARD_COLUMN_WIDTH_4).grid(row = 1, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "RelHumid:", font = text_font, width = STANDARD_COLUMN_WIDTH_4).grid(row = 2, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Format", font = text_font, width = STANDARD_COLUMN_WIDTH_4).grid(row = 3, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # entry
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = rh_minrh_var).grid(row = 2, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = rh_lowmaxrh_var).grid(row = 2, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = rh_maxrh_var).grid(row = 2, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # combobox
        ctk.CTkComboBox(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, values = list(zip(*COLORS))[0], variable = rh_formatcolor_minrh_var, state="readonly").grid(row = 3, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkComboBox(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, values = list(zip(*COLORS))[0], variable = rh_formatcolor_lowmaxrh_var, state="readonly").grid(row = 3, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkComboBox(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, values = list(zip(*COLORS))[0], variable = rh_formatcolor_maxrh_var, state="readonly").grid(row = 3, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # button
        ctk.CTkButton(self, text = "Apply", command = apply_format, width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 0, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

    


if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: co2_format_widget")
    root.geometry("600x150")

    rh_format_widget(root).pack()

    root.mainloop()