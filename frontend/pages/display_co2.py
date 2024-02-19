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
import tkinter as tk
import kaleido



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
from backend.scrollableimage import ScrollableImage
from backend.import_data import import_data
from func.figures.table_plot import TablePlot
from backend.import_data import import_data_dayprofile
from backend.time import delay_decorator
from backend.sort_data import discard_data
from backend.import_data import import_dayprofile



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

        # table data
        auto_plot = ctk.BooleanVar(value = True)
        print(auto_plot.get())

        def test(path, dayprofile):                
            df = discard_data(import_data_dayprofile(path, dayprofile), "Co2")
            print(df.head())

        path = path_var.get()
        dayprofile = co2_dayprofile_var.get()

        if auto_plot.get() == True:
            if path == "":
                CTkMessagebox.CTkMessagebox(title="Error", message="No data path selected")
                return
            elif dayprofile == "":
                CTkMessagebox.CTkMessagebox(title="Error", message="No dayprofile for CO2 selected")
                return
            else:
                dayprofile = os.path.normpath(f"{os.getcwd()}/dayprofiles/{dayprofile}")
                



                
                auto_plot.set(False)

        


        if os.path.isfile('figures output/TableCo2.png'):
            img = tk.PhotoImage(file='figures output/TableCo2.png')
            ScrollableImage(self, image = img, scrollbarwidth=20).grid(row=0, column=0, sticky="nsew")

        

        def add_plot(self, var, path_var, co2_dayprofile_var):
            path = path_var.get()
            path_dayprofile = co2_dayprofile_var.get()
            print("plotting co2 table")
            if var.get() == True:
                print("plotting co2 table")
                pass
                import_data_dayprofile(path, path_dayprofile)



            # path = path_var.get()
            # import_data(path)
            # if var.get() == True:
            #     TablePlot(self, import_data(path), size_y=70, size_x=30)
            #     img = tk.PhotoImage(file='figures output/TableStart.png')
            #     ScrollableImage(self, image = img, scrollbarwidth=20).grid(row=0, column=0, sticky="nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        


if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    new_data_var = ctk.StringVar(value = "")
    page_menu_var = ctk.StringVar(value = "")
    path_var = ctk.StringVar(value = "")
    co2_dayprofile_var = ctk.StringVar(value = "test string for dayprofile")

    root.title("TEST: display_co2")
    root.geometry("800x300")

    display_co2(root, new_data_var, page_menu_var, path_var, co2_dayprofile_var).pack()

    root.mainloop()