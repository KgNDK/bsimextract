"""
Let side menu for choosing setting for current page
"""

"""
# TODO LIST

# TODO: Make page_menu_start give values to other page_menu frames
# TODO: Finish page_menu frames
"""

"""
Importing extern modules
"""
import tkinter as tk
import customtkinter as ctk
from CTkMenuBar import *
import CTkMessagebox as CTkMessagebox
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

#* page menus
from frontend.pages.page_menu_start import page_menu_start
from frontend.pages.page_menu_co2 import page_menu_co2
from frontend.pages.page_menu_rh import page_menu_rh
from frontend.pages.page_menu_temp import page_menu_temp
from frontend.pages.page_menu_airch import page_menu_airch


class page_menu(ctk.CTkTabview):
    def __init__(self,
                 parent,
                 path_var,
                 page_menu_var,
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
                 airch_dayprofile_var_winter,

                 co2_parameter_var_always,
                 co2_parameter_var_summer,
                 co2_parameter_var_transition,
                 co2_parameter_var_winter,

                 rh_parameter_var_always,
                 rh_parameter_var_summer,
                 rh_parameter_var_transition,
                 rh_parameter_var_winter,

                 temp_parameter_var_always,
                 temp_parameter_var_summer,
                 temp_parameter_var_transition,
                 temp_parameter_var_winter,

                 airch_parameter_var_always,
                 airch_parameter_var_summer,
                 airch_parameter_var_transition,
                 airch_parameter_var_winter,
                 
                 
                 
                 ):
        super().__init__(master = parent, width = 200, command=lambda: page_menu_var.set(page_menu.get(self)))

        # tabs
        self.add("Start")
        self.add("CO2")
        self.add("RelHumid")
        self.add("Temperature")
        self.add("AirChange")

        # widgets
        page_menu_start(self.tab("Start"), 
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
                        )
        page_menu_co2(self.tab("CO2"),
                      co2_dayprofile_var_always,
                      co2_dayprofile_var_summer,
                      co2_dayprofile_var_transition,
                      co2_dayprofile_var_winter,
                      co2_parameter_var_always,
                      co2_parameter_var_summer,
                      co2_parameter_var_transition,
                      co2_parameter_var_winter
                      )
        
        page_menu_rh(self.tab("RelHumid"),
                     rh_dayprofile_var_always,
                     rh_dayprofile_var_summer,
                     rh_dayprofile_var_transition,
                     rh_dayprofile_var_winter,
                     rh_parameter_var_always,
                     rh_parameter_var_summer,
                     rh_parameter_var_transition, 
                     rh_parameter_var_winter
                     )
        page_menu_temp(self.tab("Temperature"),
                       temp_dayprofile_var_always,
                       temp_dayprofile_var_summer,
                       temp_dayprofile_var_transition,
                       temp_dayprofile_var_winter,
                       temp_parameter_var_always,
                       temp_parameter_var_summer,
                       temp_parameter_var_transition,
                       temp_parameter_var_winter,
                       )
        
        page_menu_airch(self.tab("AirChange"),
                        airch_dayprofile_var_always,
                        airch_dayprofile_var_summer,
                        airch_dayprofile_var_transition,
                        airch_dayprofile_var_winter,
                        airch_parameter_var_always,
                        airch_parameter_var_summer,
                        airch_parameter_var_transition,
                        airch_parameter_var_winter,
                        )

    
if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: page_menu")
    root.geometry("800x300")

    page_menu(root).pack()

    root.mainloop()
