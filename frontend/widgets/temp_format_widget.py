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

class temp_format_widget(ctk.CTkFrame):
    def __init__(self,
                 parent,
                 temp_mintemp_var,
                 temp_maxtemp_100h_var,
                 temp_maxtemp_25h_var,
                 temp_formatcolor_mintemp_var,
                 temp_formatcolor_maxtemp_100h_var,
                 temp_formatcolor_maxtemp_25h_var,
                 temp_between_max_summer_var,
                 temp_between_min_summer_var,
                 temp_between_max_trans_var,
                 temp_between_min_trans_var,
                 temp_between_max_winter_var,
                 temp_between_min_winter_var,
                 temp_formatcolor_between_var
                 
                 ):
        
        super().__init__(master = parent, fg_color = FG_COLOR, width = 200)

        # grid layout
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight = 1)
        self.columnconfigure((0, 1, 2, 3), weight = 1)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # label
        ctk.CTkLabel(self, text = "Temperatures formatting", width = STANDARD_COLUMN_WIDTH_3_4, font = title_font).grid(row = 0, column = 0, columnspan = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Min:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 1, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = f"{TEMP_HOUR_100}h<:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 1, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY) # Needs a variable that changes 100 according to settings
        ctk.CTkLabel(self, text = f"{TEMP_HOUR_25}h<:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 1, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY) # Needs a variable that changes 25 according to settings
        ctk.CTkLabel(self, text = "Total:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 2, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Format:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 3, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        ctk.CTkLabel(self, text = "Temperatures between formatting", width = STANDARD_COLUMN_WIDTH_TOTAL, font = title_font).grid(row = 4, column = 0, columnspan = 4, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Min:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 7, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Max:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 6, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Summer:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 5, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Transition:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 5, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Winter:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 5, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Format:", width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 8, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # button
        ctk.CTkButton(self, text = "Apply", command = apply_format, width = STANDARD_COLUMN_WIDTH_4, font = text_font).grid(row = 0, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # entry
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_mintemp_var).grid(row = 2, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_maxtemp_100h_var).grid(row = 2, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_maxtemp_25h_var).grid(row = 2, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_between_max_summer_var).grid(row = 6, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_between_max_trans_var).grid(row = 6, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_between_max_winter_var).grid(row = 6, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_between_min_summer_var).grid(row = 7, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_between_min_trans_var).grid(row = 7, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkEntry(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, textvariable = temp_between_min_winter_var).grid(row = 7, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # # combobox
        ctk.CTkComboBox(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, values = list(zip(*COLORS))[0], variable = temp_formatcolor_mintemp_var, state="readonly").grid(row = 3, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkComboBox(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, values = list(zip(*COLORS))[0], variable = temp_formatcolor_maxtemp_100h_var, state="readonly").grid(row = 3, column = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkComboBox(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, values = list(zip(*COLORS))[0], variable = temp_formatcolor_maxtemp_25h_var, state="readonly").grid(row = 3, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkComboBox(self, width = STANDARD_COLUMN_WIDTH_4, font = text_font, values = list(zip(*COLORS))[0], variable = temp_formatcolor_between_var, state="readonly").grid(row = 8, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)



if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: temp_format_widget")
    root.geometry("600x600")

    temp_format_widget(root).pack()

    root.mainloop()