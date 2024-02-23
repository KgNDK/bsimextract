"""
Page menu RelHumid page
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
from frontend.widgets.rh_format_widget import rh_format_widget
from frontend.widgets.dayprofile_all import dayprofile_all
from frontend.widgets.parameters import parameters

class page_menu_rh(ctk.CTkFrame):
    def __init__(self,
                 parent, 
                 rh_dayprofile_var_always,
                 rh_dayprofile_var_summer,
                 rh_dayprofile_var_transition,
                 rh_dayprofile_var_winter,
                 rh_parameter_var_always,
                 rh_parameter_var_summer,
                 rh_parameter_var_transition,
                 rh_parameter_var_winter
                 ):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for RelHumid under this
        # dayprofile_single(self, "RelHumid", rh_dayprofile_var).pack(fill = "x", expand = True)
        dayprofile_all(self, rh_dayprofile_var_always, rh_dayprofile_var_summer, rh_dayprofile_var_transition, rh_dayprofile_var_winter, title_parameter = "RelHumid").pack(fill = "x", expand = True)

        # widgets for RelHumid format under this
        parameters(self, rh_parameter_var_always, rh_parameter_var_summer, rh_parameter_var_transition, rh_parameter_var_winter, title_text = "RelHumid").pack(fill = "x", expand = True)
        # rh_format_widget(self,
        #         #  rh_minrh_var,
        #         #  rh_lowmaxrh_var,
        #         #  rh_maxrh_var,
        #         #  rh_formatcolor_minrh_var,
        #         #  rh_formatcolor_lowmaxrh_var,
        #         #  rh_formatcolor_maxrh_var
        #          ).pack(fill="x", expand=True)

if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: Page menu RelHumid page")
    root.geometry("400x300")

    page_menu_rh(root).pack()

    root.mainloop()