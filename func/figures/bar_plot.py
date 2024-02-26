"""
Bar plot with plotly 
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

class BarPlot(tk.Frame):
    def __init__(self, parent, df, period, parameters, Interval = "Timer", Interval_unit = "h"):
        tk.Frame.__init__(self, parent)

        fig = go.Figure()

        #* Start parameters
        length_df = len(df)
        label = df.columns[5].split()[0]
        name = label

        #* Custom settings based on input column names
        unit = "NoUnit"
        if label.lower() == "co2":
            label = "CO2"
            unit = "ppm"
        elif label.lower() == "top":
            label = "Operativ temperatur"
            unit = "°C"
        elif label.lower() == "relhumid":
            unit = "%"
            label = "Relativ luftfugtighed"
        elif label.lower() == "airchange":
            unit = "h^-1"
            label = "Luftskifte"
        

        
        
        #* Parameters
        data = []
        
        #* Preparing data
        for column in df.columns[5:]:
            counts = []
            for param in parameters:
                if isinstance(param, int):
                    counts.append(sum(df[column].astype(float) > param))
                else:
                    if param.startswith("'-"):
                        param = str(param).replace("'", "")
                        right = int(param[1:]) - 0.1
                        counts.append(sum(df[column].astype(float) < right))
                    else:
                        param = str(param).replace("'", "")
                        left, right = map(int, param.split("-"))
                        counts.append(sum((df[column].astype(float) > left) & (df[column].astype(float) < right)))
            data.append(counts)


        #* Adding traces with data based on df input
        column_names = [f"{Interval} under: {str(param).replace("'", "")[1:]} {unit}" if str(param).replace("'", "").startswith("-") else f"{Interval} mellem: {str(param).replace("'", "")} {unit}" if '-' in str(param).replace("'", "") else f"{Interval} over: {str(param).replace("'", "")} {unit}" for param in parameters]
        df_counts = pd.DataFrame(data, columns=column_names, index=df.columns[5:])

        color_mapping = {param: color for param, color in zip(df_counts.columns, PLOTLY_COLORS)}

        for param in df_counts.columns:
            room_counts = {}
            cleaned_index = []
            for item in df_counts.index:
                room_name = " ".join(item.split(" ")[1:])

                if room_name in room_counts:
                    room_counts[room_name] += 1
                    cleaned_index.append(f"{room_name} {room_counts[room_name]}")
                else:
                    room_counts[room_name] = 0
                    cleaned_index.append(f"{room_name}")
            fig.add_trace(go.Bar(
                x=cleaned_index,
                y=df_counts[param],
                name=param,
                text=df_counts[param],
                marker_color=color_mapping[param],
                texttemplate='%{y}',
                textposition='outside',
            ))

        #* Secondary y axis auto scaling 
        adjustment = df_counts.max().max()/10
        ratio = round(1. / (length_df - adjustment), 5)

        fig.add_trace(go.Scatter(
            x=[],
            y=[],
            yaxis="y2",
            opacity=0,
        ))

        #* Setting layout
        fig.update_layout(
            barmode="group",
            height=500,
            width=max(1000, (len(df.columns[5:])*len(parameters)*60)+200),
            hovermode="x",
            margin=dict(b=5,t=10,l=5,r=10),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(
                family="Calibri",
                size=20
            ),
            legend=dict(
                x=0,
                y=-0.1,
                bgcolor="White",
                orientation="h",
                font=dict(
                    size=16,
                    color="black",
                    family="Calibri",
                ),
            ),
            yaxis = dict(
                title = f"{Interval} [{Interval_unit}]",
                range = [0, round(df_counts.max().max() + adjustment, -2)],
                showgrid=True,
                showticklabels=True,
                gridcolor="LightGrey",
            ),
            yaxis2 = dict(
                title = "Andel af total brugstid [%]",
                overlaying = "y",
                side = "right",
                range = [0, df_counts.max().max()*ratio*100],
                showgrid = False
            )
        )                
        
        #* Making folder for figures if it doesn't exist
        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        
        #* Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save(f'figures output/BarPlot{name.upper()}{period}.png')

        #* Test code
        # #! REMEMBER TO REMOVE
        # root.destroy()
        # #! REMEMBER TO REMOVE

if __name__ == "__main__":

    root = tk.Tk()

    path_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/DATA/Bsimdata.txt")
    dayprofile_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract/dayprofiles/dayprofile_altid.txt")
    df = discard_data(import_data_dayprofile(path_var, dayprofile_var), "Top ")
    period = "TEST"

    #? example of parameters
    # parameters = ["-500", "500-700", 700, "600-1000", 800] # Co2
    parameters = ["-27", "-28"] # Top
    # parameters = ["-100", "10-20", 20, "20-30", 30] # RelHumid
    # parameters = ["-1", "1-2", 2, "2-3", 3, 0] # AirChange


    #? different graphs
    #* "Co2" for CO2 concentration
    #* "RelHumid" for relative humidity
    #* "Top " for temperature - Remember the space after
    #* "AirChange" for air change

    BarPlot(root, df, period, parameters)#.pack()

    root.mainloop()