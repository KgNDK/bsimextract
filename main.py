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
        display_start(self).grid(row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

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
                                                                                 ))

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
        self.co2_parameter_var_always = ctk.StringVar(value = CO2_PARAMETER_ALWAYS, name = "co2_parameter_var_always")
        self.co2_parameter_var_summer = ctk.StringVar(value = CO2_PARAMETER_SUMMER, name = "co2_parameter_var_summer")
        self.co2_parameter_var_transition = ctk.StringVar(value = CO2_PARAMETER_TRANSITION, name = "co2_parameter_var_transition")
        self.co2_parameter_var_winter = ctk.StringVar(value = CO2_PARAMETER_WINTER, name = "co2_parameter_var_winter")

        #* co2 trace variables

        #! rh
        #* rh variables
        self.rh_parameter_var_always = ctk.StringVar(value = RH_PARAMETER_ALWAYS, name = "rh_parameter_var_always")
        self.rh_parameter_var_summer = ctk.StringVar(value = RH_PARAMETER_SUMMER, name = "rh_parameter_var_summer")
        self.rh_parameter_var_transition = ctk.StringVar(value = RH_PARAMETER_TRANSITION, name = "rh_parameter_var_transition")
        self.rh_parameter_var_winter = ctk.StringVar(value = RH_PARAMETER_WINTER, name = "rh_parameter_var_winter")

        #* rh trace variables
        
        #! temp
        #* temp variables
        self.temp_parameter_var_always = ctk.StringVar(value = TEMP_PARAMETER_ALWAYS, name = "temp_parameter_var_always")
        self.temp_parameter_var_summer = ctk.StringVar(value = TEMP_PARAMETER_SUMMER, name = "temp_parameter_var_summer")
        self.temp_parameter_var_transition = ctk.StringVar(value = TEMP_PARAMETER_TRANSITION, name = "temp_parameter_var_transition")
        self.temp_parameter_var_winter = ctk.StringVar(value = TEMP_PARAMETER_WINTER, name = "temp_parameter_var_winter")

        #* temp trace variables

        #! airchange
        #* airchange variables
        self.airch_parameter_var_always = ctk.StringVar(value = AIRCH_PARAMETER_ALWAYS, name = "airch_parameter_var_always")
        self.airch_parameter_var_summer = ctk.StringVar(value = AIRCH_PARAMETER_SUMMER, name = "airch_parameter_var_summer")
        self.airch_parameter_var_transition = ctk.StringVar(value = AIRCH_PARAMETER_TRANSITION, name = "airch_parameter_var_trans")
        self.airch_parameter_var_winter = ctk.StringVar(value = AIRCH_PARAMETER_WINTER, name = "airch_parameter_var_winter")

        #* airchange trace variables
        
        #! tabview menu
        #* tabview menu variables
        self.page_menu_var = ctk.StringVar(name = "page_menu_var")

        #* tabview menu trace variables
        self.page_menu_var.trace("w", lambda name, index, mode, var=self.page_menu_var, text_before="Tabview: ", text_after=", has been selected.": on_variable_change(name, index, mode, var, text_before, text_after))

    
       

app()

    