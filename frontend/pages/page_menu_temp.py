"""
Page menu Temperature page
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
from frontend.widgets.temp_format_widget import temp_format_widget
from frontend.widgets.dayprofile_all import dayprofile_all
from frontend.widgets.parameters import parameters

class page_menu_temp(ctk.CTkFrame):
    def __init__(self,
                 parent,
                 temp_dayprofile_var_always,
                 temp_dayprofile_var_summer,
                 temp_dayprofile_var_transition,
                 temp_dayprofile_var_winter,
                 temp_parameter_var_always,
                 temp_parameter_var_summer,
                 temp_parameter_var_transition,
                 temp_parameter_var_winter,
                 ):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for Temperature
        # dayprofile_single(self, "Temperature", temp_dayprofile_var).pack(fill = "x", expand = True)
        dayprofile_all(self, temp_dayprofile_var_always, temp_dayprofile_var_summer, temp_dayprofile_var_transition, temp_dayprofile_var_winter, title_parameter = "Temperature").pack(fill = "x", expand = True)

        #* widgets for formatting temp data
        parameters(self, temp_parameter_var_always, temp_parameter_var_summer, temp_parameter_var_transition, temp_parameter_var_winter, title_text = "Temperature").pack(fill = "x", expand = True)
        # temp_format_widget(self,
        #                 #    temp_mintemp_var,
        #                 #    temp_maxtemp_100h_var,
        #                 #    temp_maxtemp_25h_var,
        #                 #    temp_formatcolor_mintemp_var,
        #                 #    temp_formatcolor_maxtemp_100h_var,
        #                 #    temp_formatcolor_maxtemp_25h_var,
        #                 #    temp_between_max_summer_var,
        #                 #    temp_between_min_summer_var,
        #                 #    temp_between_max_trans_var,
        #                 #    temp_between_min_trans_var,
        #                 #    temp_between_max_winter_var,
        #                 #    temp_between_min_winter_var,
        #                 #    temp_formatcolor_between_var
                           
                           
                           
        #                    ).pack(fill = "x", expand = True)

if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: Page menu Temperature page")
    root.geometry("400x300")

    page_menu_temp(root).pack()

    root.mainloop()