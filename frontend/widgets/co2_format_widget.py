"""
Co2 formatting of data widget where the user can choose max values and color formatting
Used for AirChange as well
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

class co2_format_widget(ctk.CTkFrame):
    def __init__(self, parent,
                 co2_maxco2_one_var,
                 co2_maxco2_two_var,
                 co2_maxco2_three_var,
                 co2_formatcolor_one_var,
                 co2_formatcolor_two_var,
                 co2_formatcolor_three_var, 
                 text_title,
                 text_button,
                 text_max,
                 text_color
                 ):
        
        super().__init__(master = parent, fg_color = FG_COLOR, width = 200)

        # grid layout
        self.rowconfigure((0, 1, 2), weight = 1)
        self.columnconfigure((0, 1, 2, 3), weight = 1)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # text widget
        ctk.CTkLabel(self, text = text_title, width = STANDARD_COLUMN_WIDTH_4, font = title_font).grid(row = 0, column = 0, columnspan = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = text_max, width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 1, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = text_color, width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 2, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # button
        ctk.CTkButton(self, text = text_button, command = apply_format, width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 0, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # max value entry widget
        self.entry_1 = ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, textvariable = co2_maxco2_one_var)
        self.entry_1.grid(row = 1, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        
        self.entry_2 = ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, textvariable = co2_maxco2_two_var)
        self.entry_2.grid(row = 1, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        self.entry_3 = ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, textvariable = co2_maxco2_three_var)
        self.entry_3.grid(row = 1, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # formatting color dropdown widget
        self.dropdown_1 = ctk.CTkComboBox(self, values = list(zip(*COLORS))[0], width = STANDARD_COLUMN_WIDTH_4, variable = co2_formatcolor_one_var, state="readonly")
        self.dropdown_1.grid(row = 2, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        
        self.dropdown_2 = ctk.CTkComboBox(self, values = list(zip(*COLORS))[0], width = STANDARD_COLUMN_WIDTH_4, variable = co2_formatcolor_two_var, state="readonly")
        self.dropdown_2.grid(row = 2, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        
        self.dropdown_3 = ctk.CTkComboBox(self, values = list(zip(*COLORS))[0], width = STANDARD_COLUMN_WIDTH_4, variable = co2_formatcolor_three_var, state="readonly")
        self.dropdown_3.grid(row = 2, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)


if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: co2_format_widget")
    root.geometry("600x150")

    co2_format_widget(root).pack()

    root.mainloop()