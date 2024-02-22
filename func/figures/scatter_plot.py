"""
Scatter plot with plotly 
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import CTkMessagebox as CTkMessagebox
import customtkinter as ctk
import tkinter as tk
import kaleido
from PIL import Image, ImageTk
import plotly
import plotly.graph_objs as go
import plotly.io as pio
from plotly.subplots import make_subplots
import io
import decimal
import uuid
import webbrowser
import pprint
import plotly.express as px
import pandas as pd
import random
import numpy as np
import email
import quopri
import matplotlib 
import datetime
import string
import itertools
from openpyxl.workbook import Workbook
import math

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *
from backend.import_data import import_data
from backend.import_data import import_data_dayprofile
from backend.time import timeit
from backend.sort_data import discard_data

class ScatterPlot(tk.Frame):
    def __init__(self, parent, df, parameters = [], Interval_unit = "h"):
        tk.Frame.__init__(self, parent)

        fig = go.Figure()

        #* Parameters
        length_df = len(df)
        label = df.columns[5].split()[0]
        name = label

        if label.lower() == "co2":
            label = "CO2"
            unit = "ppm" 
            max_dtick_x = max(50, round(length_df/50, -2))
            max_dtick_y = max(50, round(int(df[5:].astype(float).max().iloc[0])/6, -2))
            fig.update_layout(
                yaxis=dict(
                    dtick=max_dtick_y,
                    tick0=400,
                    gridcolor='LightGrey'
                ),
                xaxis=dict(
                    dtick=max_dtick_x,
                    gridcolor='LightGrey'
                ),
                yaxis_showgrid=True,
            )
            shape_height = 50
        elif label.lower() == "top":
            label = "Operativ temperatur"
            unit = "°C"
            max_dtick_x = max(50, round(length_df/50, -2))
            tick0_y = int(df[5:].astype(float).min().iloc[0]) - 1
            fig.update_layout(
                yaxis=dict(
                    dtick=1,
                    tick0=tick0_y,
                    gridcolor='LightGrey'
                ),
                xaxis=dict(
                    dtick=max_dtick_x,
                    gridcolor='LightGrey'
                ),
                yaxis_showgrid=True,
            )
            shape_height = 0.3
        elif label.lower() == "relhumid":
            unit = "%"
            label = "Relativ luftfugtighed"
            max_dtick_x = max(50, round(length_df/50, -2))
            tick0_y = round(int(df[5:].astype(float).min().iloc[0]) - 5, -1)
            fig.update_layout(
                yaxis=dict(
                    dtick=10,
                    tick0=tick0_y,
                    gridcolor='LightGrey'
                ),
                xaxis=dict(
                    dtick=max_dtick_x,
                    gridcolor='LightGrey'
                ),
                yaxis_showgrid=True,
            )
            shape_height = 2
        elif label.lower() == "airchange":
            unit = "h^-1"
            label = "Luftskifte"
            max_dtick_x = max(50, round(length_df/50, -2))
            fig.update_layout(
                yaxis=dict(
                    dtick=1,
                    tick0=0,
                    gridcolor='LightGrey'
                ),
                xaxis=dict(
                    dtick=max_dtick_x,
                    gridcolor='LightGrey'
                ),
                yaxis_showgrid=True,
            )
            shape_height = 0.3
        else:
            unit = ""
            shape_height = 1


        color_index = 0

        for param in parameters:
            if isinstance(param, int):
                fig.add_shape(
                    type="line",
                    x0 = 0,
                    y0 = param,
                    x1 = len(df),
                    y1 = param,
                    line=dict(
                        color=PLOTLY_COLORS_2[color_index],
                    )
                )
                for side in (0+0.2, len(df)-0.2):
                    fig.add_shape(
                        type="line",
                        x0 = side,
                        y0 = param,
                        x1 = side,
                        y1 = param + shape_height,
                        # layer="below",
                        line=dict(
                            color=PLOTLY_COLORS_2[color_index],
                        )
                    )
                color_index += 1
            else:
                if param.startswith("-"):
                    right = int(param[1:])
                    fig.add_shape(
                    type="line",
                    x0 = 0,
                    y0 = right,
                    x1 = len(df),
                    y1 = right,
                    layer="below",
                    line=dict(
                        color=PLOTLY_COLORS_2[color_index],
                        )
                    )
                    for side in (0, len(df)):
                        fig.add_shape(
                            type="line",
                            x0 = side,
                            y0 = right,
                            x1 = side,
                            y1 = right - shape_height,
                            layer="below",
                            line=dict(
                                color=PLOTLY_COLORS_2[color_index],
                            )
                        )
                    color_index += 1
                else:
                    left, right = map(int, param.split("-"))
                    fig.add_hrect(
                        y0 = left,
                        y1 = right,
                        fillcolor = PLOTLY_COLORS_2[color_index],
                        layer="below",
                        line_width=0,
                        opacity = 0.2
                    )
                    color_index += 1

        for index, column in enumerate(df.columns[5:]):
            trace_name = " ".join(column.split(" ")[1:])
            fig.add_trace(go.Scatter(
                        x=list(range(length_df)), 
                        y=df[column],
                        mode='lines',
                        name=trace_name,
                        line=dict(
                            color=PLOTLY_COLORS[index],
                            # width=1
                        ),
            ))


        
        fig.update_layout(
            width = max(1000, (length_df/2)+200),
            height = 500,
            margin=dict(b=5,t=10,l=5,r=10),
            paper_bgcolor = PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR,
            plot_bgcolor="white",
            autosize = PLOTLY_STANDARD_AUTOSIZE,
            xaxis = dict(
                gridcolor='LightGrey',
                range=[0, length_df],
                title = f"Brugstid [{Interval_unit}]",
            ),
            yaxis = dict(
                range=[0, max(df[5:])],
                title = f"{label} [{unit}]",
            ),
            autotypenumbers="convert types",
            font=dict(family="Calibri", size=20),
            legend=dict(
                x=0,
                y=-0.2,
                bgcolor="White",
                orientation="h",
                font=dict(
                    size=16,
                    color="black",
                    family="Calibri",
                ),
            ),
        )

        if length_df == 8760:
            tick0_x = (df["Week"] == 0).sum()
            fig.update_layout(
                xaxis = dict(
                    dtick = 168, 
                    tick0 = tick0_x,
                )
            )
                

        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        
        #* Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save(f'figures output/ScatterPlot{name.upper()}.png')

        # #! REMEMBER TO REMOVE
        # root.destroy()
        # #! REMEMBER TO REMOVE

        

if __name__ == "__main__":

    root = tk.Tk()

    path_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/DATA/Bsimdata.txt")
    dayprofile_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract/dayprofiles/dayprofile_altid.txt")
    df = discard_data(import_data_dayprofile(path_var, dayprofile_var), "Top ")

    #? different graphs
    #* "Co2" for CO2 concentration
    #* "RelHumid" for relative humidity
    #* "Top " for temperature - Remember the space after
    #* "AirChange" for air change

    # parameters = ["-800", "900-1000", 1100] # Co2
    # parameters = ["-27", "-28"] # Top
    # parameters = ["-100", "10-20", 20, "20-30", 30] # RelHumid
    # parameters = ["-1", "1-2", 2, "2-3", 3, 0] # AirChange

    ScatterPlot(root, df, parameters)#.pack()

    root.mainloop()