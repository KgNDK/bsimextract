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
from func.figures.scatter_plot import ScatterPlot
from func.figures.bar_plot import BarPlot
from func.figures.distribution_plot import DistributionPlot



class display_co2(ctk.CTkFrame):
    def __init__(self, parent, new_data_var, page_menu_var, path_var, co2_dayprofile_var):
        super().__init__(master = parent)

        # layout
        self.rowconfigure((0, 1, 2), weight = 1, uniform="a")
        self.columnconfigure((0, 1, 2), weight = 1)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # parameters
        name = "CO2"
        parameters = [950, 1200]
        path = path_var.get()
        dayprofile = co2_dayprofile_var.get()

        # label
        ctk.CTkLabel(self, text = f"TablePlot{name}", font = title_font).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, rowspan = 3)
        ctk.CTkLabel(self, text = f"ScatterPlot{name}", font = title_font).grid(row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)
        ctk.CTkLabel(self, text = f"BarPlot{name}", font = title_font).grid(row = 1, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)
        ctk.CTkLabel(self, text = f"DistributionPlot{name}", font = title_font).grid(row = 2, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)

        # auto plot variables
        auto_plot_Scatter = ctk.BooleanVar(value = True)
        auto_plot_Bar = ctk.BooleanVar(value = True)
        auto_plot_Distribution = ctk.BooleanVar(value = True)
        auto_plot_Table = ctk.BooleanVar(value = True)

        # plots
        if path == "":
            CTkMessagebox.CTkMessagebox(title="Error", message="No data path selected")
            return
        elif dayprofile == "":
            CTkMessagebox.CTkMessagebox(title="Error", message=f"No dayprofile for {name.upper()} selected")
            return
        else:
            dayprofile = os.path.normpath(f"{os.getcwd()}/dayprofiles/{dayprofile}")
            df = discard_data(import_data_dayprofile(path, dayprofile), f"{name.lower().capitalize()}")

            plots = [
                ("ScatterPlot", 0, auto_plot_Scatter),
                ("BarPlot", 1, auto_plot_Bar),
                ("DistributionPlot", 2, auto_plot_Distribution)
            ]

            for plot_type, row, auto_plot_var in plots:
                if os.path.isfile(f'figures output/{plot_type}{name.upper()}.png'):
                    img = tk.PhotoImage(file=f'figures output/{plot_type}{name.upper()}.png')
                    ScrollableImage(self, image=img, scrollbarwidth=20).grid(row=row, column=1, sticky="nsew", columnspan=2, padx=STANDARD_PADX, pady=STANDARD_PADY)
                    auto_plot_var.set(False)

            if os.path.isfile(f'figures output/TablePlot{name.upper()}.png'):
                img_TablePlot = tk.PhotoImage(file=f'figures output/TablePlot{name.upper()}.png')
                ScrollableImage(self, image = img_TablePlot, scrollbarwidth=20).grid(row=0, column=0, sticky="nsew", rowspan = 3, padx = STANDARD_PADX, pady = STANDARD_PADY)
                auto_plot_Table.set(False)
            
            if auto_plot_Scatter.get() == True:
                ScatterPlot(self, df, parameters)
                img_ScatterPlot = tk.PhotoImage(file=f'figures output/ScatterPlot{name.upper()}.png')
                ScrollableImage(self, image = img_ScatterPlot, scrollbarwidth=20).grid(row=0, column=1, sticky="nsew", columnspan = 2, padx = STANDARD_PADX, pady = STANDARD_PADY)
                auto_plot_Scatter.set(False)

            if auto_plot_Bar.get() == True:
                BarPlot(self, df, parameters)
                img_BarPlot = tk.PhotoImage(file=f'figures output/BarPlot{name.upper()}.png')
                ScrollableImage(self, image = img_BarPlot, scrollbarwidth=20).grid(row=1, column=1, sticky="nsew", columnspan = 2, padx = STANDARD_PADX, pady = STANDARD_PADY)
                auto_plot_Bar.set(False)

            if auto_plot_Distribution.get() == True:
                DistributionPlot(self, df, parameters)
                img_DistributionPlot = tk.PhotoImage(file=f'figures output/DistributionPlot{name.upper()}.png')
                ScrollableImage(self, image = img_DistributionPlot, scrollbarwidth=20).grid(row=2, column=1, sticky="nsew", columnspan = 2, padx = STANDARD_PADX, pady = STANDARD_PADY)
                auto_plot_Distribution.set(False)

            
    


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