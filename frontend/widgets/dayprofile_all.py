"""
Dayprofile_all widget
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
from tkinter import ttk
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
from frontend.widgets.dayprofile import dayprofile
from frontend.widgets.dayprofile_title import dayprofile_title

class dayprofile_all(ctk.CTkFrame):
    def __init__(self, parent, always_dayprofile_var, summer_dayprofile_var, transition_dayprofile_var, winter_dayprofile_var, label_always = "Always", label_summer = "Summer", label_transition = "Transition", label_winter = "Winter", title_parameter = ""):
        super().__init__(master = parent, fg_color = FG_COLOR)

        #* font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        #* text
        if title_parameter == "":
            title_text = "Dayprofiles: "
        else:
            title_text = f"{title_parameter} dayprofiles: "


        #* text widgets
        dayprofile_title(self, title_text).pack(fill = "x", expand = True)

        #* combobox widget
        dayprofile(self, label_always, always_dayprofile_var).pack(fill = "x", expand = True)
        dayprofile(self, label_summer, summer_dayprofile_var).pack(fill = "x", expand = True)
        dayprofile(self, label_transition, transition_dayprofile_var).pack(fill = "x", expand = True)
        dayprofile(self, label_winter, winter_dayprofile_var).pack(fill = "x", expand = True)







if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: dayprofile_single")
    root.geometry("400x400")

    dayprofile_all(root).pack()

    root.mainloop()