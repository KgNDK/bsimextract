"""
Frame for displaying temp data visually
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


class display_temperature(ctk.CTkFrame):
    def __init__(self, parent, new_data_var, page_menu_var, path_var, temp_dayprofile_var_always, temp_dayprofile_var_summer, temp_dayprofile_var_transition, temp_dayprofile_var_winter, temp_param_var_always, temp_param_var_summer, temp_param_var_transition, temp_param_var_winter):
        super().__init__(master = parent)

        # layout
        self.rowconfigure((0, 1), weight = 1, uniform="a")
        self.columnconfigure((0, 1), weight = 1, uniform="a")

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # parameters
        name = "Top"
        # parameters = [27, 28] # Always
        # parameters = ["-23", "23-26", 26] # Summer period
        # parameters = ["-20", "20-26", 26] # Transition period
        # parameters = ["-20", "20-25", 25] # Winter period
        path = path_var.get()
        # dayprofile = temp_dayprofile_var.get()

        dayprofile_always = temp_dayprofile_var_always.get()
        dayprofile_summer = temp_dayprofile_var_summer.get()
        dayprofile_transition = temp_dayprofile_var_transition.get()
        dayprofile_winter = temp_dayprofile_var_winter.get()

        # parameters = [950, 1200]
        parameters_always = temp_param_var_always.get()
        parameters_summer = temp_param_var_summer.get()
        parameters_transition = temp_param_var_transition.get()
        parameters_winter = temp_param_var_winter.get()

        # label
        ctk.CTkLabel(self, text = f"NewPlot{name}?", font = title_font).grid(row = 1, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, rowspan = 3)
        ctk.CTkLabel(self, text = f"ScatterPlot{name}", font = title_font).grid(row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)
        ctk.CTkLabel(self, text = f"BarPlot{name}", font = title_font).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)
        ctk.CTkLabel(self, text = f"DistributionPlot{name}", font = title_font).grid(row = 1, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY, columnspan = 2)

        # auto plot variables
        auto_plot_Scatter = ctk.BooleanVar(value = True)
        auto_plot_Bar = ctk.BooleanVar(value = True)
        auto_plot_Distribution = ctk.BooleanVar(value = True)
        auto_plot_Table = ctk.BooleanVar(value = True)

        # plots
        day_profiles = {
        "dayprofile_winter": dayprofile_winter,
        "dayprofile_transition": dayprofile_transition,
        "dayprofile_summer": dayprofile_summer,
        "dayprofile_always": dayprofile_always
        }
        
        for key, value in day_profiles.items():
            dayprofile = value
            if path == "":
                CTkMessagebox.CTkMessagebox(title="Error", message="No data path selected")
                return
            elif dayprofile == "":
                CTkMessagebox.CTkMessagebox(title="Error", message=f"No dayprofile for {name.upper()} selected")
                return
            else:
                if dayprofile == "":
                    continue
                if dayprofile != "" and dayprofile.endswith(".txt"):
                    dayprofile = os.path.normpath(f"{os.getcwd()}/dayprofiles/{dayprofile}")
                    df = discard_data(import_data_dayprofile(path, dayprofile), f"{name.lower().capitalize()}")
                    period = key.split("_")[1].capitalize()
                    if period.lower() == "always":
                        input = str(parameters_always).replace("(", "").replace(")", "").replace(" ", "").split(",")
                        parameters = [int(x) if "-" not in x else x for x in input]
                    elif period.lower() == "summer":
                        input = str(parameters_summer).replace("(", "").replace(")", "").replace(" ", "").split(",")
                        parameters = [int(x) if "-" not in x else x for x in input]
                    elif period.lower() == "transition":
                        input = str(parameters_transition).replace("(", "").replace(")", "").replace(" ", "").split(",")
                        parameters = [int(x) if "-" not in x else x for x in input]
                    elif period.lower() == "winter":
                        input = str(parameters_winter).replace("(", "").replace(")", "").replace(" ", "").split(",")
                        parameters = [int(x) if "-" not in x else x for x in input]
                    else:
                        parameters = [27, 28]

                    if auto_plot_Scatter.get() == True:
                        ScatterPlot(self, df, period, parameters)
                        if dayprofile == dayprofile_always:
                            img_ScatterPlot = tk.PhotoImage(file=f'figures output/ScatterPlot{name.upper()}{period}.png')
                            ScrollableImage(self, image = img_ScatterPlot, scrollbarwidth=20).grid(row=0, column=1, sticky="nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
                            auto_plot_Scatter.set(False)

                    if auto_plot_Bar.get() == True:
                        BarPlot(self, df, period, parameters)
                        if dayprofile == dayprofile_always:
                            img_BarPlot = tk.PhotoImage(file=f'figures output/BarPlot{name.upper()}{period}.png')
                            ScrollableImage(self, image = img_BarPlot, scrollbarwidth=20).grid(row=0, column=0, sticky="nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
                            auto_plot_Bar.set(False)

                    if auto_plot_Distribution.get() == True:
                        DistributionPlot(self, df, period, parameters)
                        if dayprofile == dayprofile_always:
                            img_DistributionPlot = tk.PhotoImage(file=f'figures output/DistributionPlot{name.upper()}{period}.png')
                            ScrollableImage(self, image = img_DistributionPlot, scrollbarwidth=20).grid(row=1, column=0, sticky="nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
                            auto_plot_Distribution.set(False)
            plots = [
                        ("ScatterPlot", 0, 1, auto_plot_Scatter),
                        ("BarPlot", 0, 0, auto_plot_Bar),
                        ("DistributionPlot", 1, 0, auto_plot_Distribution)
                    ]

            for plot_type, row, column, auto_plot_var in plots:
                if os.path.isfile(f'figures output/{plot_type}{name.upper()}Always.png'):
                    img = tk.PhotoImage(file=f'figures output/{plot_type}{name.upper()}Always.png')
                    ScrollableImage(self, image=img, scrollbarwidth=20).grid(row=row, column=column, sticky="nsew", columnspan=1, padx=STANDARD_PADX, pady=STANDARD_PADY)
                    auto_plot_var.set(False)

            #* ExtraPlot
            # if os.path.isfile(f'figures output/TablePlot{name.upper()}.png'):
            #     img_TablePlot = tk.PhotoImage(file=f'figures output/TablePlot{name.upper()}.png')
            #     ScrollableImage(self, image = img_TablePlot, scrollbarwidth=20).grid(row=1, column=1, sticky="nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
            #     auto_plot_Table.set(False)

        


if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: display_rh")
    root.geometry("800x300")

    display_temperature(root).pack()

    root.mainloop()