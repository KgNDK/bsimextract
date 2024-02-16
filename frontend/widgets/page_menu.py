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
                 co2_dayprofile_var,
                 rh_dayprofile_var,
                 temp_dayprofile_var,
                 airch_dayprofile_var,
                 path_var,
                 co2_maxco2_one_var,
                 co2_maxco2_two_var,
                 co2_maxco2_three_var,
                 co2_formatcolor_one_var,
                 co2_formatcolor_two_var,
                 co2_formatcolor_three_var,
                 airch_maxairch_one_var,
                 airch_maxairch_two_var,
                 airch_maxairch_three_var,
                 airch_formatcolor_one_var,
                 airch_formatcolor_two_var,
                 airch_formatcolor_three_var,
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
                 temp_formatcolor_between_var,
                 rh_minrh_var,
                 rh_lowmaxrh_var,
                 rh_maxrh_var,
                 rh_formatcolor_minrh_var,
                 rh_formatcolor_lowmaxrh_var,
                 rh_formatcolor_maxrh_var,
                 page_menu_var,
                 new_data_var
                 
                 
                 
                 ):
        super().__init__(master = parent, width = 200, command=lambda: page_menu_var.set(page_menu.get(self)))

        # tabs
        self.add("Start")
        self.add("CO2")
        self.add("RelHumid")
        self.add("Temperature")
        self.add("AirChange")

        # widgets
        page_menu_start(self.tab("Start"), co2_dayprofile_var,
                                           rh_dayprofile_var,
                                           temp_dayprofile_var,
                                           airch_dayprofile_var,
                                           path_var,
                                           new_data_var
                                           
                                           
                                           
                                           )
        page_menu_co2(self.tab("CO2"), co2_dayprofile_var,
                                       co2_maxco2_one_var,
                                       co2_maxco2_two_var,
                                       co2_maxco2_three_var,
                                       co2_formatcolor_one_var,
                                       co2_formatcolor_two_var,
                                       co2_formatcolor_three_var
                                       
                                       
                                       )
        page_menu_rh(self.tab("RelHumid"), rh_dayprofile_var,
                                           rh_minrh_var,
                                           rh_lowmaxrh_var,
                                           rh_maxrh_var,
                                           rh_formatcolor_minrh_var,
                                           rh_formatcolor_lowmaxrh_var,
                                           rh_formatcolor_maxrh_var
                                           
                                           
                                           )
        page_menu_temp(self.tab("Temperature"), temp_dayprofile_var,
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
                                                
                                                
                                                )
        page_menu_airch(self.tab("AirChange"), airch_dayprofile_var,
                                               airch_maxairch_one_var,
                                               airch_maxairch_two_var,
                                               airch_maxairch_three_var,
                                               airch_formatcolor_one_var,
                                               airch_formatcolor_two_var,
                                               airch_formatcolor_three_var
                                               
                                               
                                               )

    
if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: page_menu")
    root.geometry("800x300")

    page_menu(root).pack()

    root.mainloop()
