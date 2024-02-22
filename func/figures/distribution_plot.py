"""
Distribution plot with plotly 
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

class DistributionPlot(tk.Frame):
    def __init__(self, parent, df, parameters = []):
        tk.Frame.__init__(self, parent)

        fig = go.Figure()

        #* Parameters
        # length_df = len(df)
        label_input = df.columns[5].split()[0]
        name = label_input

        def sort_segments(x):
            segment_length = len(x) // 5
            partitioned = np.partition(x, segment_length * np.arange(1, 5))
            sorted_segments = np.sort(partitioned.reshape(5, -1), axis=1)
            return pd.Series(sorted_segments.flatten())

        unit = "NoUnit"
        if label_input.lower() == "co2":
            label = "CO2"
            unit = "ppm"
            #* Converting data to int to avoid sorting algorithmic errors
            for column in df.columns[5:]:
                df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).astype(int)
            shape_height = 10
        elif label_input.lower() == "top":
            label = "Operativ temperatur"
            unit = "°C"
            #* Converting data to two decimals to avoid sorting algorithmic errors
            for column in df.columns[5:]:
                df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).round(2)
            shape_height = 0.3
        elif label_input.lower() == "relhumid":
            unit = "%"
            label = "Relativ luftfugtighed"
            #* Converting data to two decimals to avoid sorting algorithmic errors
            for column in df.columns[5:]:
                df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).round(2)
            shape_height = 2
        elif label_input.lower() == "airchange":
            unit = "h^-1"
            label = "Luftskifte"
            #* Converting data to two decimals to avoid sorting algorithmic errors
            for column in df.columns[5:]:
                df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).round(2)
            shape_height = 0.3
            

        #* Sorting data
        sorted_df = df[df.columns[5:]].apply(lambda x: x.sort_values(ignore_index=True, ascending=True)).reset_index(drop=True)

        
        color_index = 0

        for param in parameters:
            if isinstance(param, int):
                fig.add_shape(
                    type="line",
                    x0 = 0,
                    y0 = param,
                    x1 = len(sorted_df),
                    y1 = param,
                    layer="below",
                    line=dict(
                        color=PLOTLY_COLORS_2[color_index],
                    )
                )
                for side in (0, len(sorted_df)):
                    fig.add_shape(
                        type="line",
                        x0 = side,
                        y0 = param,
                        x1 = side,
                        y1 = param + shape_height,
                        layer="below",
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
                    x1 = len(sorted_df),
                    y1 = right,
                    layer="below",
                    line=dict(
                        color=PLOTLY_COLORS_2[color_index],
                        )
                    )
                    for side in (0, len(sorted_df)):
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
                        

        num=0
        for column in sorted_df.columns:
            trace_name = " ".join(column.split(" ")[1:])
            fig.add_trace(go.Scatter(
                x=sorted_df.index,
                y=sorted_df[column],
                mode='lines',
                name=trace_name,
                line=dict(
                    color=PLOTLY_COLORS[num],
                ),
            ))
            num += 1

        fig.add_trace(go.Scatter(
            x=[],
            y=[],
            xaxis="x2",
            opacity=0,
        ))

        fig.update_layout(
            width = 1000,
            height = 500,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor = PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR,
            plot_bgcolor="white",
            autosize = PLOTLY_STANDARD_AUTOSIZE,
            font=dict(family="Calibri", size=20),
            autotypenumbers="convert types",
            xaxis = dict(
                visible=False
                
            ),
            xaxis2 = dict(
                title = "Andel af brugstid under [%]",
                overlaying = "x",
                range = [0, 100],
                showgrid = True,
                gridcolor = 'LightGrey',
                dtick = 10,
                tick0 = 0,
            ),
            yaxis = dict(
                range=[0, max(df[5:])],
                title = f"{label} [{unit}]",
                showgrid = True,
                gridcolor = 'LightGrey',
            ),
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

        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        
        #* Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save(f'figures output/DistributionPlot{name.upper()}.png')

        #! REMEMBER TO REMOVE
        root.destroy()
        #! REMEMBER TO REMOVE

        

if __name__ == "__main__":

    root = tk.Tk()

    path_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/DATA/Bsimdata.txt")
    dayprofile_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract/dayprofiles/dayprofile_altid.txt")
    df = discard_data(import_data_dayprofile(path_var, dayprofile_var), "Co2")

    #? different graphs
    #* "Co2" for CO2 concentration
    #* "RelHumid" for relative humidity
    #* "Top " for temperature - Remember the space after
    #* "AirChange" for air change

    parameters = ["-500", "500-700", 700, "600-1000", 800] # Co2
    # parameters = ["-27", "-28"] # Top
    # parameters = ["-100", "10-20", 20, "20-30", 30] # RelHumid
    # parameters = ["-1", "1-2", 2, "2-3", 3, 0] # AirChange

    DistributionPlot(root, df, parameters)#.pack()

    root.mainloop()