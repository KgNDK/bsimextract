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
    def __init__(self, parent, df):
        tk.Frame.__init__(self, parent)

        fig = go.Figure()

        #* Parameters
        # length_df = len(df)
        label = df.columns[5].split()[0]
        name = label

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
        
        # sorted_df = df[df.columns[5:]].apply(lambda x: x.sort_values(ignore_index=True, ascending=True)).reset_index(drop=True)
        sorted_df = df[df.columns[5:]].apply(lambda x: x.sort_values(ignore_index=True, ascending=True, kind="stable")).apply(lambda x: x.sort_values(ignore_index=True, ascending=True, kind="mergesort")).reset_index(drop=True)

        num=0
        for column in sorted_df.columns:
            fig.add_trace(go.Scatter(
                x=sorted_df.index,
                y=sorted_df[column],
                mode='lines',
                name=column,
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
                title = "Andel af brugstid [%]",
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

        # #! REMEMBER TO REMOVE
        # root.destroy()
        # #! REMEMBER TO REMOVE

        

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

    DistributionPlot(root, df)#.pack()

    root.mainloop()