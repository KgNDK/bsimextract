"""
Frame for displaying CO2 data visually
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
# import seaborn as sns
import kaleido
from PIL import Image, ImageTk
import plotly.graph_objs as go
import plotly.io as pio
import io
import tenacity
import decimal
import uuid
import webbrowser
import pprint
import plotly.express as px
import pandas as pd
import random
import email
import quopri
import matplotlib 


"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *
from func.figures.random_plot import TestPlot



class display_co2(ctk.CTkFrame):
    def __init__(self, parent, new_data_var, page_menu_var, path_var, co2_dayprofile_var):
        super().__init__(master = parent)

        # layout
        self.rowconfigure((0, 1, 2), weight = 1)
        self.columnconfigure((0, 1, 2), weight = 1)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # label
        ctk.CTkLabel(self, text = "CO2_Table_data", font = title_font).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, rowspan = 3)
        ctk.CTkLabel(self, text = "CO2_Figure_Box_Plot", font = title_font).grid(row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)
        ctk.CTkLabel(self, text = "CO2_Figure_Distribution_Curve", font = title_font).grid(row = 1, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)
        ctk.CTkLabel(self, text = "CO2_Figure_Bar_Chart", font = title_font).grid(row = 2, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)

        print(co2_dayprofile_var.get())

        # plots
        if new_data_var.get() == True:
            pass


        


if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    new_data_var = ""
    page_menu_var = ""
    path_var = ""

    root.title("TEST: display_co2")
    root.geometry("800x300")

    display_co2(root, new_data_var, page_menu_var, path_var).pack()

    root.mainloop()