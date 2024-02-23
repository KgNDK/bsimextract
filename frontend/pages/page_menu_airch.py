"""
Page menu AirChange page
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
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
from frontend.widgets.dayprofile_single import dayprofile_single
from frontend.widgets.co2_format_widget import co2_format_widget
from frontend.widgets.dayprofile_all import dayprofile_all
from frontend.widgets.parameters import parameters

class page_menu_airch(ctk.CTkFrame):
    def __init__(self,
                 parent,
                 airch_dayprofile_var_always,
                 airch_dayprofile_var_summer,
                 airch_dayprofile_var_transition,
                 airch_dayprofile_var_winter,
                 airch_parameter_var_always,
                 airch_parameter_var_summer,
                 airch_parameter_var_transition,
                 airch_parameter_var_winter,
                 ):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for AirChange under this
        # dayprofile_single(self, "AirChange", airch_dayprofile_var).pack(fill = "x", expand = True)
        dayprofile_all(self, airch_dayprofile_var_always, airch_dayprofile_var_summer, airch_dayprofile_var_transition, airch_dayprofile_var_winter, title_parameter = "AirChange").pack(fill = "x", expand = True)

        #* widgets for formatting AirChange data under this
        parameters(self, airch_parameter_var_always, airch_parameter_var_summer, airch_parameter_var_transition, airch_parameter_var_winter, title_text="AirChange").pack(expand = True, fill = "x")
        # co2_format_widget(self,
        #                   airch_maxairch_one_var,
        #                   airch_maxairch_two_var,
        #                   airch_maxairch_three_var,
        #                   airch_formatcolor_one_var,
        #                   airch_formatcolor_two_var,
        #                   airch_formatcolor_three_var,
        #                   text_title = "AirChange hours above",
        #                   text_button = "Apply",
        #                   text_max = "Max AirChange:",
        #                   text_color = "Formatting color:").pack(expand = True, fill = "x")

if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: Page menu AirChange page")
    root.geometry("400x300")

    page_menu_airch(root).pack()

    root.mainloop()