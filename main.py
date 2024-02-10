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

"""
Importing internal modules
"""
from settings.settings import *
from frontend.widgets.title_menu import title_menu
from frontend.widgets.page_menu import page_menu
from func.variable_changes import on_variable_change


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
        self.columnconfigure((1, 2, 3), weight = 6)

        # title menu
        title_menu(self)

        # widgets
        page_menu(self,
                  self.co2_dayprofile_var,
                  self.rh_dayprofile_var,
                  self.temp_dayprofile_var,
                  self.airch_dayprofile_var,
                  self.path_var,
                  self.co2_maxco2_one_var,
                  self.co2_maxco2_two_var,
                  self.co2_maxco2_three_var,
                  self.co2_formatcolor_one_var,
                  self.co2_formatcolor_two_var,
                  self.co2_formatcolor_three_var,
                  self.airch_maxairch_one_var,
                  self.airch_maxairch_two_var,
                  self.airch_maxairch_three_var,
                  self.airch_formatcolor_one_var,
                  self.airch_formatcolor_two_var,
                  self.airch_formatcolor_three_var


                  
                  ).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        self.mainloop()

    def init_parameters(self):
        
        #! path
        # path variables
        self.path_var = ctk.StringVar(value = START_PATH)

        # path trace variables
        self.path_var.trace("w", lambda name, index, mode, var=self.path_var: on_variable_change(name, index, mode, var))

        #! dayprofile
        # dayprofile variables
        self.co2_dayprofile_var = ctk.StringVar(value = DAYPROFILE_CO2)
        self.rh_dayprofile_var = ctk.StringVar(value = DAYPROFILE_RH)
        self.temp_dayprofile_var = ctk.StringVar(value = DAYPROFILE_TEMP)
        self.airch_dayprofile_var = ctk.StringVar(value = DAYPROFILE_AIRCH)

        # dayprofile trace variables
        self.co2_dayprofile_var.trace("w", lambda name, index, mode, var=self.co2_dayprofile_var: on_variable_change(name, index, mode, var))
        self.rh_dayprofile_var.trace("w", lambda name, index, mode, var=self.rh_dayprofile_var: on_variable_change(name, index, mode, var))
        self.temp_dayprofile_var.trace("w", lambda name, index, mode, var=self.temp_dayprofile_var: on_variable_change(name, index, mode, var))
        self.airch_dayprofile_var.trace("w", lambda name, index, mode, var=self.airch_dayprofile_var: on_variable_change(name, index, mode, var))

        #! co2
        # co2 variables
        self.co2_maxco2_one_var = ctk.StringVar(value = CO2_MAXCO2_ONE)
        self.co2_maxco2_two_var = ctk.StringVar(value = CO2_MAXCO2_TWO)
        self.co2_maxco2_three_var = ctk.StringVar(value = CO2_MAXCO2_THREE)
        self.co2_formatcolor_one_var = ctk.StringVar(value = CO2_FORMATCOLOR_ONE)
        self.co2_formatcolor_two_var = ctk.StringVar(value = CO2_FORMATCOLOR_TWO)
        self.co2_formatcolor_three_var = ctk.StringVar(value = CO2_FORMATCOLOR_THREE)

        # co2 trace variables
        self.co2_maxco2_one_var.trace("w", lambda name, index, mode, var=self.co2_maxco2_one_var: on_variable_change(name, index, mode, var))
        self.co2_maxco2_two_var.trace("w", lambda name, index, mode, var=self.co2_maxco2_two_var: on_variable_change(name, index, mode, var))
        self.co2_maxco2_three_var.trace("w", lambda name, index, mode, var=self.co2_maxco2_three_var: on_variable_change(name, index, mode, var))
        self.co2_formatcolor_one_var.trace("w", lambda name, index, mode, var=self.co2_formatcolor_one_var: on_variable_change(name, index, mode, var))
        self.co2_formatcolor_two_var.trace("w", lambda name, index, mode, var=self.co2_formatcolor_two_var: on_variable_change(name, index, mode, var))
        self.co2_formatcolor_three_var.trace("w", lambda name, index, mode, var=self.co2_formatcolor_three_var: on_variable_change(name, index, mode, var))

        #! rh
        # rh variables

        # rh trace variables


        #! temp
        # temp variables
        self.temp_maxtemp_one_var = ctk.StringVar(value = TEMP_MAXTEMP_ONE)
        self.temp_maxtemp_two_var = ctk.StringVar(value = TEMP_MAXTEMP_TWO)
        self.temp_acceptedmaxtemp_var = ctk.StringVar(value = TEMP_ACCEPTEDMAXTEMP)
        self.temp_acceptedmintemp_var = ctk.StringVar(value = TEMP_ACCEPTEDMINTEMP)
        self.temp_mintemp_var = ctk.StringVar(value = TEMP_MINTEMP)
        self.temp_formatcolor_maxone_var = ctk.StringVar(value = TEMP_FORMATCOLOR_MAXONE)
        self.temp_formatcolor_maxtwo_var = ctk.StringVar(value = TEMP_FORMATCOLOR_MAXTWO)
        self.temp_formatcolor_accepted_var = ctk.StringVar(value = TEMP_FORMATCOLOR_ACCEPTED)
        self.temp_formatcolor_mintemp_var = ctk.StringVar(value = TEMP_FORMATCOLOR_MINTEMP)

        # temp trace variables

        #! airchange
        # airchange variables
        self.airch_maxairch_one_var = ctk.StringVar(value = AIRCH_MAXAIRCH_ONE)
        self.airch_maxairch_two_var = ctk.StringVar(value = AIRCH_MAXAIRCH_TWO)
        self.airch_maxairch_three_var = ctk.StringVar(value = AIRCH_MAXAIRCH_THREE)
        self.airch_formatcolor_one_var = ctk.StringVar(value = AIRCH_FORMATCOLOR_ONE)
        self.airch_formatcolor_two_var = ctk.StringVar(value = AIRCH_FORMATCOLOR_TWO)
        self.airch_formatcolor_three_var = ctk.StringVar(value = AIRCH_FORMATCOLOR_THREE)

        # airchange trace variables
        self.airch_maxairch_one_var.trace("w", lambda name, index, mode, var=self.airch_maxairch_one_var: on_variable_change(name, index, mode, var))
        self.airch_maxairch_two_var.trace("w", lambda name, index, mode, var=self.airch_maxairch_two_var: on_variable_change(name, index, mode, var))
        self.airch_maxairch_three_var.trace("w", lambda name, index, mode, var=self.airch_maxairch_three_var: on_variable_change(name, index, mode, var))
        self.airch_formatcolor_one_var.trace("w", lambda name, index, mode, var=self.airch_formatcolor_one_var: on_variable_change(name, index, mode, var))
        self.airch_formatcolor_two_var.trace("w", lambda name, index, mode, var=self.airch_formatcolor_two_var: on_variable_change(name, index, mode, var))
        self.airch_formatcolor_three_var.trace("w", lambda name, index, mode, var=self.airch_formatcolor_three_var: on_variable_change(name, index, mode, var))

        
        

       

app()

    