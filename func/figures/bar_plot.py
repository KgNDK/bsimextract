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
    def __init__(self, parent, df):
        tk.Frame.__init__(self, parent)

        fig = go.Figure()

        #* Parameters
        length_df = len(df)
        label = df.columns[5].split()[0]
        max_df = int(df.iloc[:, 5:].astype(float).values.max()) # Maximal value from df[5:]

        print(df)
        print(max_df)

        # if label.lower() == "co2":
        #     label = "CO2"
        #     unit = "ppm" 
        #     max_dtick_x = max(50, round(length_df/50, -2))
        #     max_dtick_y = max(50, round(int(df[5:].astype(float).max().iloc[0])/10), -2)
        #     fig.update_layout(
        #         yaxis=dict(
        #             dtick=50,
        #             tick0=400,
        #             gridcolor='LightGrey'
        #         ),
        #         xaxis=dict(
        #             dtick=max_dtick_x,
        #             gridcolor='LightGrey'
        #         ),
        #         yaxis_showgrid=True,
        #     )
        # elif label.lower() == "top":
        #     label = "Operativ temperatur"
        #     unit = "°C"
        #     max_dtick_x = max(50, round(length_df/50, -2))
        #     tick0_y = int(df[5:].astype(float).min().iloc[0]) - 1
        #     fig.update_layout(
        #         yaxis=dict(
        #             dtick=1,
        #             tick0=tick0_y,
        #             gridcolor='LightGrey'
        #         ),
        #         xaxis=dict(
        #             dtick=max_dtick_x,
        #             gridcolor='LightGrey'
        #         ),
        #         yaxis_showgrid=True,
        #     )
        # elif label.lower() == "relhumid":
        #     unit = "%"
        #     label = "Relativ luftfugtighed"
        #     max_dtick_x = max(50, round(length_df/50, -2))
        #     tick0_y = round(int(df[5:].astype(float).min().iloc[0]) - 5, -1)
        #     fig.update_layout(
        #         yaxis=dict(
        #             dtick=10,
        #             tick0=tick0_y,
        #             gridcolor='LightGrey'
        #         ),
        #         xaxis=dict(
        #             dtick=max_dtick_x,
        #             gridcolor='LightGrey'
        #         ),
        #         yaxis_showgrid=True,
        #     )
        # elif label.lower() == "airchange":
        #     unit = "h^-1"
        #     label = "Luftskifte"
        #     max_dtick_x = max(50, round(length_df/50, -2))
        #     fig.update_layout(
        #         yaxis=dict(
        #             dtick=2,
        #             tick0=0,
        #             gridcolor='LightGrey'
        #         ),
        #         xaxis=dict(
        #             dtick=max_dtick_x,
        #             gridcolor='LightGrey'
        #         ),
        #         yaxis_showgrid=True,
        #     )
        # else:
        #     unit = ""

        # num = 0
        # parameter = [1000, 1250, 1500]
        # for column in df.columns[5:]:
        #     # fig.add_trace(go.Scatter(
        #     #             x=list(range(length_df)), 
        #     #             y=df[column],
        #     #             mode='lines',
        #     #             name=column))
        #     for offset in range(0,3):
        #         fig.add_trace(go.Bar(
        #             x=num, 
        #             y=np.sum(df[column] >= parameter[offset]),
        #             offsetgroup=offset,
        #         ))
        #     num += 1

        parameters = [500, 750, 1000]

        #? axis

        ratio = round(1. / length_df, 5)
        tick_pos = range(0, int(max_df) + 1, 7)
        print(ratio)

        data = []


        for column in df.columns[5:]:
            counts = [sum(df[column].astype(float) > param) for param in parameters]
            data.append(counts)

        df_counts = pd.DataFrame(data, columns=[f'Timer over: {param}' for param in parameters], index=df.columns[5:])

        color_mapping = {param: color for param, color in zip(df_counts.columns, PLOTLY_COLORS)}

        for param in df_counts.columns:
            fig.add_trace(go.Bar(
                x=df_counts.index,
                y=df_counts[param],
                name=param,
                text=df_counts[param],
                marker_color=color_mapping[param]
            ))

        fig.add_trace(go.Scatter(
            x=[],
            y=[],
            yaxis="y2",
            opacity=0,
        ))

        fig.update_layout(
            barmode="group",
            height=500,
            width=700,
            hovermode="x",
            margin=dict(b=0,t=10,l=0,r=10),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(
                family="Calibri",
                size=20
            ),
            legend=dict(
                x=0,
                y=-0.15,
                bgcolor="White",
                orientation="h",
                font=dict(
                    size=16,
                    color="black",
                    family="Calibri",
                ),
            ),
            yaxis = dict(
                title = "Timer over [h]",
                range = [0, round(df_counts.max().max()+50, -2)],
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

        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        
        #* Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save(f'figures output/TestPlot{label}.png')

        root.destroy()

if __name__ == "__main__":

    root = tk.Tk()

    path_var = os.path.normpath("C:\\Users\\Mikkel H. Lauridsen\\OneDrive - Aalborg Universitet\\Programmer\\03 BSimExtract\\Bsimdata.txt")
    dayprofile_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract/dayprofiles/dayprofile_altid.txt")
    df = discard_data(import_data_dayprofile(path_var, dayprofile_var), "Co2")

    #? different graphs
    #* "Co2" for CO2 concentration
    #* "RelHumid" for relative humidity
    #* "Top " for temperature - Remember the space after
    #* "AirChange" for air change

    BarPlot(root, df)#.pack()

    root.mainloop()