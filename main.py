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
                #   self.rh_dayprofile_var,
                #   self.temp_dayprofile_var,
                #   self.airch_dayprofile_var
                  
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



    

        def on_variable_change(name, index, mode, variable):
            """
            This function handles the event of a variable change. It takes in four parameters:
                - name: the name of the variable
                - index: the index of the variable
                - mode: the mode of the variable change
                - variable: the variable that has changed
            This function does not return anything.
            """
            print(variable.get())
        
        

       

app()

    