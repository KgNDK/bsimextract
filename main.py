"""
Main file
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
import pandas as pd
import kaleido
from PIL import Image, ImageTk
import plotly.graph_objs as go
import plotly.io as pio
import io
import tenacity
import decimal
import uuid
import email
import quopri
import matplotlib
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import openpyxl
from openpyxl.workbook import Workbook

"""
Importing internal modules
"""
from settings.settings import *
from frontend.widgets.title_menu import title_menu
from frontend.widgets.page_menu import page_menu
from backend.variable_changes import on_variable_change, on_variable_change_int, on_page_menu_var_change
from frontend.pages.display_start import display_start
from frontend.pages.display_co2 import display_co2
from frontend.pages.display_airchange import display_airchange
from frontend.pages.display_relhumid import display_relhumid
from frontend.pages.display_temperature import display_temperature
from backend.clearup import clear_figure_output



class app(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__()
        ctk.set_appearance_mode(COLOR_MODE)
        self.geometry("1800x1000")
        self.title(f"BSimExtract {VERSION_NUMBER}")
        self.minsize(800, 500)
        self.init_parameters()
        
        # layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((0), weight = 1)
        self.columnconfigure((1), weight = 25)

        # title menu
        title_menu(self)

        # clear old data
        clear_figure_output()

        #! widgets
        # data visualization
        function_dict = {
            "display_start": display_start,
            "display_co2": display_co2,
            "display_relhumid": display_relhumid,
            "display_temperature": display_temperature,
            "display_airchange": display_airchange
            }
        dayprofile_var = None
        display_start(self, self.new_data_var, self.page_menu_var, self.path_var, dayprofile_var).grid(row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        self.page_menu_var.trace("w", lambda 
                                 name, 
                                 index, 
                                 mode, 
                                 var=self.page_menu_var: on_page_menu_var_change(name, 
                                                                                 index, 
                                                                                 mode, 
                                                                                 var, 
                                                                                 self, 
                                                                                 function_dict, 
                                                                                 self.new_data_var, 
                                                                                 self.path_var, 
                                                                                 self.co2_dayprofile_var_always, 
                                                                                 self.rh_dayprofile_var_always, 
                                                                                 self.temp_dayprofile_var_always, 
                                                                                 self.airch_dayprofile_var_always))

        # page menu
        page_menu(self,
                  self.path_var,
                  self.page_menu_var,
                  self.new_data_var, 
                  self.co2_dayprofile_var_always, 
                  self.co2_dayprofile_var_summer, 
                  self.co2_dayprofile_var_transition, 
                  self.co2_dayprofile_var_winter,
                  self.rh_dayprofile_var_always,
                  self.rh_dayprofile_var_summer,
                  self.rh_dayprofile_var_transition,
                  self.rh_dayprofile_var_winter,
                  self.temp_dayprofile_var_always,
                  self.temp_dayprofile_var_summer,
                  self.temp_dayprofile_var_transition,
                  self.temp_dayprofile_var_winter,
                  self.airch_dayprofile_var_always,
                  self.airch_dayprofile_var_summer,
                  self.airch_dayprofile_var_transition,
                  self.airch_dayprofile_var_winter,
                  self.co2_parameter_var_always,
                  self.co2_parameter_var_summer,
                  self.co2_parameter_var_transition,
                  self.co2_parameter_var_winter,
                  self.rh_parameter_var_always,
                  self.rh_parameter_var_summer,
                  self.rh_parameter_var_transition,
                  self.rh_parameter_var_winter,
                  self.temp_parameter_var_always,
                  self.temp_parameter_var_summer,
                  self.temp_parameter_var_transition,
                  self.temp_parameter_var_winter,
                  self.airch_parameter_var_always,
                  self.airch_parameter_var_summer,
                  self.airch_parameter_var_transition,
                  self.airch_parameter_var_winter
                  
                  
                  
                  
                  ).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        
        
        

        self.mainloop()

    def init_parameters(self):
        """
        Initialize parameters for path, dayprofile, co2, rh, temp, and airchange variables and their trace variables.
        """
        
        #! path
        #* path variables
        self.path_var = ctk.StringVar(value = START_PATH, name = "path_var")

        #* path trace variables
        self.path_var.trace("w", lambda name, index, mode, var=self.path_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))

        #! data
        #* data variables
        self.new_data_var = ctk.BooleanVar(name = "new_data_var")

        #* data trace variables
        self.new_data_var.trace("w", lambda name, index, mode, var=self.new_data_var: print(f"{name} has been changed to: {var.get()}"))


        # #! display 
        # self.display_height_var = ctk.IntVar(name = "display_height_var")
        # self.display_width_var = ctk.IntVar(name = "display_width_var")

        # self.display_height_var.trace("w", lambda name, index, mode, var=self.display_height_var: on_variable_change_int(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.display_width_var.trace("w", lambda name, index, mode, var=self.display_width_var: on_variable_change_int(name, index, mode, var, text_before = f"{name} has been changed to: "))

        #! dayprofile
        #* dayprofile variables
        # self.co2_dayprofile_var = ctk.StringVar(value = DAYPROFILE_CO2, name = "co2_dayprofile_var")
        # self.rh_dayprofile_var = ctk.StringVar(value = DAYPROFILE_RH, name = "rh_dayprofile_var")
        # self.temp_dayprofile_var = ctk.StringVar(value = DAYPROFILE_TEMP, name = "temp_dayprofile_var")
        # self.airch_dayprofile_var = ctk.StringVar(value = DAYPROFILE_AIRCH, name = "airch_dayprofile_var")

        # #* dayprofile trace variables
        # self.co2_dayprofile_var.trace("w", lambda name, index, mode, var=self.co2_dayprofile_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.rh_dayprofile_var.trace("w", lambda name, index, mode, var=self.rh_dayprofile_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.temp_dayprofile_var.trace("w", lambda name, index, mode, var=self.temp_dayprofile_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.airch_dayprofile_var.trace("w", lambda name, index, mode, var=self.airch_dayprofile_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        
        #* dayprofile variables
        self.co2_dayprofile_var_always = ctk.StringVar(value = DAYPROFILE_CO2_ALWAYS, name = "co2_dayprofile_var_always")
        self.co2_dayprofile_var_summer = ctk.StringVar(value = DAYPROFILE_CO2_SUMMER, name = "co2_dayprofile_var_summer")
        self.co2_dayprofile_var_transition = ctk.StringVar(value = DAYPROFILE_CO2_TRANSITION, name = "co2_dayprofile_var_transition")
        self.co2_dayprofile_var_winter = ctk.StringVar(value = DAYPROFILE_CO2_WINTER, name = "co2_dayprofile_var_winter")

        self.rh_dayprofile_var_always = ctk.StringVar(value = DAYPROFILE_RH_ALWAYS, name = "rh_dayprofile_var_always")
        self.rh_dayprofile_var_summer = ctk.StringVar(value = DAYPROFILE_RH_SUMMER, name = "rh_dayprofile_var_summer")
        self.rh_dayprofile_var_transition = ctk.StringVar(value = DAYPROFILE_RH_TRANSITION, name = "rh_dayprofile_var_transition")
        self.rh_dayprofile_var_winter = ctk.StringVar(value = DAYPROFILE_RH_WINTER, name = "rh_dayprofile_var_winter")
        
        self.temp_dayprofile_var_always = ctk.StringVar(value = DAYPROFILE_TEMP_ALWAYS, name = "temp_dayprofile_var_always")
        self.temp_dayprofile_var_summer = ctk.StringVar(value = DAYPROFILE_TEMP_SUMMER, name = "temp_dayprofile_var_summer")
        self.temp_dayprofile_var_transition = ctk.StringVar(value = DAYPROFILE_TEMP_TRANSITION, name = "temp_dayprofile_var_transition")
        self.temp_dayprofile_var_winter = ctk.StringVar(value = DAYPROFILE_TEMP_WINTER, name = "temp_dayprofile_var_winter")

        self.airch_dayprofile_var_always = ctk.StringVar(value = DAYPROFILE_AIRCH_ALWAYS, name = "airch_dayprofile_var_always")
        self.airch_dayprofile_var_summer = ctk.StringVar(value = DAYPROFILE_AIRCH_SUMMER, name = "airch_dayprofile_var_summer")
        self.airch_dayprofile_var_transition = ctk.StringVar(value = DAYPROFILE_AIRCH_TRANSITION, name = "airch_dayprofile_var_transition")
        self.airch_dayprofile_var_winter = ctk.StringVar(value = DAYPROFILE_AIRCH_WINTER, name = "airch_dayprofile_var_winter")


        #* dayprofile trace variables
        self.co2_dayprofile_var_always.trace("w", lambda name, index, mode, var=self.co2_dayprofile_var_always: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.co2_dayprofile_var_summer.trace("w", lambda name, index, mode, var=self.co2_dayprofile_var_summer: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.co2_dayprofile_var_transition.trace("w", lambda name, index, mode, var=self.co2_dayprofile_var_transition: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.co2_dayprofile_var_winter.trace("w", lambda name, index, mode, var=self.co2_dayprofile_var_winter: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        
        self.rh_dayprofile_var_always.trace("w", lambda name, index, mode, var=self.rh_dayprofile_var_always: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.rh_dayprofile_var_summer.trace("w", lambda name, index, mode, var=self.rh_dayprofile_var_summer: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.rh_dayprofile_var_transition.trace("w", lambda name, index, mode, var=self.rh_dayprofile_var_transition: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.rh_dayprofile_var_winter.trace("w", lambda name, index, mode, var=self.rh_dayprofile_var_winter: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))

        self.temp_dayprofile_var_always.trace("w", lambda name, index, mode, var=self.temp_dayprofile_var_always: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.temp_dayprofile_var_summer.trace("w", lambda name, index, mode, var=self.temp_dayprofile_var_summer: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.temp_dayprofile_var_transition.trace("w", lambda name, index, mode, var=self.temp_dayprofile_var_transition: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.temp_dayprofile_var_winter.trace("w", lambda name, index, mode, var=self.temp_dayprofile_var_winter: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))

        self.airch_dayprofile_var_always.trace("w", lambda name, index, mode, var=self.airch_dayprofile_var_always: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.airch_dayprofile_var_summer.trace("w", lambda name, index, mode, var=self.airch_dayprofile_var_summer: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.airch_dayprofile_var_transition.trace("w", lambda name, index, mode, var=self.airch_dayprofile_var_transition: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        self.airch_dayprofile_var_winter.trace("w", lambda name, index, mode, var=self.airch_dayprofile_var_winter: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))


        #! co2
        #* co2 variables
        # self.co2_maxco2_one_var = ctk.StringVar(value = CO2_MAXCO2_ONE, name = "co2_maxco2_one_var")
        # self.co2_maxco2_two_var = ctk.StringVar(value = CO2_MAXCO2_TWO, name = "co2_maxco2_two_var")
        # self.co2_maxco2_three_var = ctk.StringVar(value = CO2_MAXCO2_THREE, name = "co2_maxco2_three_var")
        # self.co2_formatcolor_one_var = ctk.StringVar(value = CO2_FORMATCOLOR_ONE, name = "co2_formatcolor_one_var")
        # self.co2_formatcolor_two_var = ctk.StringVar(value = CO2_FORMATCOLOR_TWO, name = "co2_formatcolor_two_var")
        # self.co2_formatcolor_three_var = ctk.StringVar(value = CO2_FORMATCOLOR_THREE, name = "co2_formatcolor_three_var")

        self.co2_parameter_var_always = ctk.StringVar(value = CO2_PARAMETER_ALWAYS, name = "co2_parameter_var_always")
        self.co2_parameter_var_summer = ctk.StringVar(value = CO2_PARAMETER_SUMMER, name = "co2_parameter_var_summer")
        self.co2_parameter_var_transition = ctk.StringVar(value = CO2_PARAMETER_TRANSITION, name = "co2_parameter_var_transition")
        self.co2_parameter_var_winter = ctk.StringVar(value = CO2_PARAMETER_WINTER, name = "co2_parameter_var_winter")

        #* co2 trace variables
        # self.co2_maxco2_one_var.trace("w", lambda name, index, mode, var=self.co2_maxco2_one_var: on_variable_change_int(name, index, mode, var, CO2_MAXCO2_ONE, text_before = f"{name} has been changed to: "))
        # self.co2_maxco2_two_var.trace("w", lambda name, index, mode, var=self.co2_maxco2_two_var: on_variable_change_int(name, index, mode, var, CO2_MAXCO2_TWO, text_before = f"{name} has been changed to: "))
        # self.co2_maxco2_three_var.trace("w", lambda name, index, mode, var=self.co2_maxco2_three_var: on_variable_change_int(name, index, mode, var, CO2_MAXCO2_THREE, text_before = f"{name} has been changed to: "))
        # self.co2_formatcolor_one_var.trace("w", lambda name, index, mode, var=self.co2_formatcolor_one_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.co2_formatcolor_two_var.trace("w", lambda name, index, mode, var=self.co2_formatcolor_two_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.co2_formatcolor_three_var.trace("w", lambda name, index, mode, var=self.co2_formatcolor_three_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))

    

        #! rh
        #* rh variables
        # self.rh_minrh_var = ctk.StringVar(value = RH_MINRH, name = "rh_minrh_var")
        # self.rh_lowmaxrh_var = ctk.StringVar(value = RH_LOWMAXRH, name = "rh_lowmaxrh_var")
        # self.rh_maxrh_var = ctk.StringVar(value = RH_MAXRH, name = "rh_maxrh_var")
        # self.rh_formatcolor_minrh_var = ctk.StringVar(value = RH_FORMATCOLOR_MINRH, name = "rh_formatcolor_minrh_var")
        # self.rh_formatcolor_lowmaxrh_var = ctk.StringVar(value = RH_FORMATCOLOR_LOWMAXRH, name = "rh_formatcolor_lowmaxrh_var")
        # self.rh_formatcolor_maxrh_var = ctk.StringVar(value = RH_FORMATCOLOR_MAXRH, name = "rh_formatcolor_maxrh_var")

        self.rh_parameter_var_always = ctk.StringVar(value = RH_PARAMETER_ALWAYS, name = "rh_parameter_var_always")
        self.rh_parameter_var_summer = ctk.StringVar(value = RH_PARAMETER_SUMMER, name = "rh_parameter_var_summer")
        self.rh_parameter_var_transition = ctk.StringVar(value = RH_PARAMETER_TRANSITION, name = "rh_parameter_var_transition")
        self.rh_parameter_var_winter = ctk.StringVar(value = RH_PARAMETER_WINTER, name = "rh_parameter_var_winter")

        #* rh trace variables
        # self.rh_minrh_var.trace("w", lambda name, index, mode, var=self.rh_minrh_var: on_variable_change_int(name, index, mode, var, RH_MINRH, text_before = f"{name} has been changed to: "))
        # self.rh_lowmaxrh_var.trace("w", lambda name, index, mode, var=self.rh_lowmaxrh_var: on_variable_change_int(name, index, mode, var, RH_LOWMAXRH, text_before = f"{name} has been changed to: "))
        # self.rh_maxrh_var.trace("w", lambda name, index, mode, var=self.rh_maxrh_var: on_variable_change_int(name, index, mode, var, RH_MAXRH, text_before = f"{name} has been changed to: "))
        # self.rh_formatcolor_minrh_var.trace("w", lambda name, index, mode, var=self.rh_formatcolor_minrh_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.rh_formatcolor_lowmaxrh_var.trace("w", lambda name, index, mode, var=self.rh_formatcolor_lowmaxrh_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.rh_formatcolor_maxrh_var.trace("w", lambda name, index, mode, var=self.rh_formatcolor_maxrh_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))

        #! temp
        #* temp variables
        # self.temp_mintemp_var = ctk.StringVar(value = TEMP_MINTEMP, name = "temp_mintemp_var")
        # self.temp_maxtemp_100h_var = ctk.StringVar(value = TEMP_MAXTEMP_100H, name = "temp_maxtemp_100h_var")
        # self.temp_maxtemp_25h_var = ctk.StringVar(value = TEMP_MAXTEMP_25H, name = "temp_maxtemp_25h_var")
        # self.temp_formatcolor_mintemp_var = ctk.StringVar(value = TEMP_FORMATCOLOR_MINTEMP, name = "temp_formatcolor_mintemp_var")
        # self.temp_formatcolor_maxtemp_100h_var = ctk.StringVar(value = TEMP_FORMATCOLOR_MAXTEMP_100H, name = "temp_formatcolor_maxtemp_100h_var")
        # self.temp_formatcolor_maxtemp_25h_var = ctk.StringVar(value = TEMP_FORMATCOLOR_MAXTEMP_25H, name = "temp_formatcolor_maxtemp_25h_var")
        # self.temp_between_max_summer_var = ctk.StringVar(value = TEMP_BETWEEN_MAX_SUMMER, name = "temp_between_max_summer_var")
        # self.temp_between_min_summer_var = ctk.StringVar(value = TEMP_BETWEEN_MIN_SUMMER, name = "temp_between_min_summer_var")
        # self.temp_between_max_trans_var = ctk.StringVar(value = TEMP_BETWEEN_MAX_TRANS, name = "temp_between_max_trans_var")
        # self.temp_between_min_trans_var = ctk.StringVar(value = TEMP_BETWEEN_MIN_TRANS, name = "temp_between_min_trans_var")
        # self.temp_between_max_winter_var = ctk.StringVar(value = TEMP_BETWEEN_MAX_WINTER, name = "temp_between_max_winter_var")
        # self.temp_between_min_winter_var = ctk.StringVar(value = TEMP_BETWEEN_MIN_WINTER, name = "temp_between_min_winter_var")
        # self.temp_formatcolor_between_var = ctk.StringVar(value = TEMP_FORMATCOLOR_BETWEEN, name = "temp_formatcolor_between_var")

        self.temp_parameter_var_always = ctk.StringVar(value = TEMP_PARAMETER_ALWAYS, name = "temp_parameter_var_always")
        self.temp_parameter_var_summer = ctk.StringVar(value = TEMP_PARAMETER_SUMMER, name = "temp_parameter_var_summer")
        self.temp_parameter_var_transition = ctk.StringVar(value = TEMP_PARAMETER_TRANSITION, name = "temp_parameter_var_transition")
        self.temp_parameter_var_winter = ctk.StringVar(value = TEMP_PARAMETER_WINTER, name = "temp_parameter_var_winter")

        #* temp trace variables
        # self.temp_mintemp_var.trace("w", lambda name, index, mode, var=self.temp_mintemp_var: on_variable_change_int(name, index, mode, var, TEMP_MINTEMP, text_before = f"{name} has been changed to: "))
        # self.temp_maxtemp_100h_var.trace("w", lambda name, index, mode, var=self.temp_maxtemp_100h_var: on_variable_change_int(name, index, mode, var, TEMP_MAXTEMP_100H, text_before = f"{name} has been changed to: "))
        # self.temp_maxtemp_25h_var.trace("w", lambda name, index, mode, var=self.temp_maxtemp_25h_var: on_variable_change_int(name, index, mode, var, TEMP_MAXTEMP_25H, text_before = f"{name} has been changed to: "))
        # self.temp_formatcolor_mintemp_var.trace("w", lambda name, index, mode, var=self.temp_formatcolor_mintemp_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.temp_formatcolor_maxtemp_100h_var.trace("w", lambda name, index, mode, var=self.temp_formatcolor_maxtemp_100h_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.temp_formatcolor_maxtemp_25h_var.trace("w", lambda name, index, mode, var=self.temp_formatcolor_maxtemp_25h_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.temp_between_max_summer_var.trace("w", lambda name, index, mode, var=self.temp_between_max_summer_var: on_variable_change_int(name, index, mode, var, TEMP_BETWEEN_MAX_SUMMER, text_before = f"{name} has been changed to: "))
        # self.temp_between_min_summer_var.trace("w", lambda name, index, mode, var=self.temp_between_min_summer_var: on_variable_change_int(name, index, mode, var, TEMP_BETWEEN_MIN_SUMMER, text_before = f"{name} has been changed to: "))
        # self.temp_between_max_trans_var.trace("w", lambda name, index, mode, var=self.temp_between_max_trans_var: on_variable_change_int(name, index, mode, var, TEMP_BETWEEN_MAX_TRANS, text_before = f"{name} has been changed to: "))
        # self.temp_between_min_trans_var.trace("w", lambda name, index, mode, var=self.temp_between_min_trans_var: on_variable_change_int(name, index, mode, var, TEMP_BETWEEN_MIN_TRANS, text_before = f"{name} has been changed to: "))
        # self.temp_between_max_winter_var.trace("w", lambda name, index, mode, var=self.temp_between_max_winter_var: on_variable_change_int(name, index, mode, var, TEMP_BETWEEN_MAX_WINTER, text_before = f"{name} has been changed to: "))
        # self.temp_between_min_winter_var.trace("w", lambda name, index, mode, var=self.temp_between_min_winter_var: on_variable_change_int(name, index, mode, var, TEMP_BETWEEN_MIN_WINTER, text_before = f"{name} has been changed to: "))
        # self.temp_formatcolor_between_var.trace("w", lambda name, index, mode, var=self.temp_formatcolor_between_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))

        #! airchange
        #* airchange variables
        # self.airch_maxairch_one_var = ctk.StringVar(value = AIRCH_MAXAIRCH_ONE, name = "airch_maxairch_one_var")
        # self.airch_maxairch_two_var = ctk.StringVar(value = AIRCH_MAXAIRCH_TWO, name = "airch_maxairch_two_var")
        # self.airch_maxairch_three_var = ctk.StringVar(value = AIRCH_MAXAIRCH_THREE, name = "airch_maxairch_three_var")
        # self.airch_formatcolor_one_var = ctk.StringVar(value = AIRCH_FORMATCOLOR_ONE, name = "airch_formatcolor_one_var")
        # self.airch_formatcolor_two_var = ctk.StringVar(value = AIRCH_FORMATCOLOR_TWO, name = "airch_formatcolor_two_var")
        # self.airch_formatcolor_three_var = ctk.StringVar(value = AIRCH_FORMATCOLOR_THREE, name = "airch_formatcolor_three_var")

        self.airch_parameter_var_always = ctk.StringVar(value = AIRCH_PARAMETER_ALWAYS, name = "airch_parameter_var_always")
        self.airch_parameter_var_summer = ctk.StringVar(value = AIRCH_PARAMETER_SUMMER, name = "airch_parameter_var_summer")
        self.airch_parameter_var_transition = ctk.StringVar(value = AIRCH_PARAMETER_TRANSITION, name = "airch_parameter_var_trans")
        self.airch_parameter_var_winter = ctk.StringVar(value = AIRCH_PARAMETER_WINTER, name = "airch_parameter_var_winter")

        #* airchange trace variables
        # self.airch_maxairch_one_var.trace("w", lambda name, index, mode, var=self.airch_maxairch_one_var: on_variable_change_int(name, index, mode, var, AIRCH_MAXAIRCH_ONE, text_before = f"{name} has been changed to: "))
        # self.airch_maxairch_two_var.trace("w", lambda name, index, mode, var=self.airch_maxairch_two_var: on_variable_change_int(name, index, mode, var, AIRCH_MAXAIRCH_TWO, text_before = f"{name} has been changed to: "))
        # self.airch_maxairch_three_var.trace("w", lambda name, index, mode, var=self.airch_maxairch_three_var: on_variable_change_int(name, index, mode, var, AIRCH_MAXAIRCH_THREE, text_before = f"{name} has been changed to: "))
        # self.airch_formatcolor_one_var.trace("w", lambda name, index, mode, var=self.airch_formatcolor_one_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.airch_formatcolor_two_var.trace("w", lambda name, index, mode, var=self.airch_formatcolor_two_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        # self.airch_formatcolor_three_var.trace("w", lambda name, index, mode, var=self.airch_formatcolor_three_var: on_variable_change(name, index, mode, var, text_before = f"{name} has been changed to: "))
        
        #! tabview menu
        #* tabview menu variables
        self.page_menu_var = ctk.StringVar(name = "page_menu_var")

        #* tabview menu trace variables
        self.page_menu_var.trace("w", lambda name, index, mode, var=self.page_menu_var, text_before="Tabview: ", text_after=", has been selected.": on_variable_change(name, index, mode, var, text_before, text_after))

    
       

app()

    