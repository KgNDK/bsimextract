"""
Page menu Co2 page
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
import CTkMenuBar
import webbrowser
import pandas as pd

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

class page_menu_co2(ctk.CTkFrame):
    def __init__(self,
                 parent,
                 co2_dayprofile_var_always,
                 co2_dayprofile_var_summer, 
                 co2_dayprofile_var_transition, 
                 co2_dayprofile_var_winter,
                 co2_parameter_var_always,
                 co2_parameter_var_summer,
                 co2_parameter_var_transition,
                 co2_parameter_var_winter
                 ):
        super().__init__(master = parent, fg_color="transparent", width = 200)
        self.pack(expand = True, fill = "both")

        # widgets for CO2 under this
        # dayprofile_single(self, "CO2", co2_dayprofile_var).pack(expand = True, fill = "x")
        dayprofile_all(self, co2_dayprofile_var_always, co2_dayprofile_var_summer, co2_dayprofile_var_transition, co2_dayprofile_var_winter, title_parameter = "CO2").pack(expand = True, fill = "x")

        #* widgets for formatting CO2 data under this
        parameters(self, co2_parameter_var_always, co2_parameter_var_summer, co2_parameter_var_transition, co2_parameter_var_winter, title_text = "CO2").pack(expand = True, fill = "x")

if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: Page menu CO2 page")
    root.geometry("400x300")

    page_menu_co2(root).pack()

    root.mainloop()