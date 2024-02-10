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

class co2_format_widget(ctk.CTkFrame):
    def __init__(self, parent, 
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

       


    def apply_formatting(self):
        print("Applying formatting")


if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: co2_format_widget")
    root.geometry("600x150")

    co2_format_widget(root).pack()

    root.mainloop()