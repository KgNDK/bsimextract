"""
Page menu Starting page
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

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *
from frontend.widgets.import_file_widget import import_file_widget
from frontend.widgets.dayprofile_all import dayprofile_all

class page_menu_start(ctk.CTkFrame):
    def __init__(self, 
                 parent, 
                 path_var, 
                 new_data_var,

                 co2_dayprofile_var_always,
                 co2_dayprofile_var_summer, 
                 co2_dayprofile_var_transition, 
                 co2_dayprofile_var_winter,

                 rh_dayprofile_var_always,
                 rh_dayprofile_var_summer,
                 rh_dayprofile_var_transition,
                 rh_dayprofile_var_winter,

                 temp_dayprofile_var_always,
                 temp_dayprofile_var_summer,
                 temp_dayprofile_var_transition,
                 temp_dayprofile_var_winter,

                 airch_dayprofile_var_always,
                 airch_dayprofile_var_summer,
                 airch_dayprofile_var_transition,
                 airch_dayprofile_var_winter
                 ):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widget importing data file in .txt format
        
        import_file_widget(self, path_var, new_data_var).pack(expand = True, fill = "x")

        # widgets for start under this
        dayprofile_all(self, co2_dayprofile_var_always, co2_dayprofile_var_summer, co2_dayprofile_var_transition, co2_dayprofile_var_winter, title_parameter="CO2").pack(expand = True, fill = "x")
        dayprofile_all(self, rh_dayprofile_var_always, rh_dayprofile_var_summer, rh_dayprofile_var_transition, rh_dayprofile_var_winter, title_parameter="RelHumid").pack(expand = True, fill = "x")
        dayprofile_all(self, temp_dayprofile_var_always, temp_dayprofile_var_summer, temp_dayprofile_var_transition, temp_dayprofile_var_winter, title_parameter="Temperature").pack(expand = True, fill = "x")
        dayprofile_all(self, airch_dayprofile_var_always, airch_dayprofile_var_summer, airch_dayprofile_var_transition, airch_dayprofile_var_winter, title_parameter="Airchange").pack(expand = True, fill = "x")

if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: dayprofile_single")
    root.geometry("400x400")

    page_menu_start(root).pack()

    root.mainloop()