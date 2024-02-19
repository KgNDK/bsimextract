"""
Scatter plot with plotly 
"""

"""
# TODO LIST
Airchange has to be fixed
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
    def __init__(self, parent, df):
        tk.Frame.__init__(self, parent)

        label = df.columns[5].split()[0]
        # print(label)
        print(df)
        
        fig = go.Figure()

        if label.lower() == "co2":
            label = "CO2"
            unit = "ppm" 
            max_dtick_x = max(50, round(len(df)/50, -2))
            max_dtick_y = max(50, round(int(df[5:].astype(float).max().iloc[0])/10), -2)
            fig.update_layout(
                yaxis=dict(
                    dtick=50,
                    tick0=400,
                    gridcolor='LightGrey'
                ),
                xaxis=dict(
                    dtick=max_dtick_x,
                    gridcolor='LightGrey'
                ),
                yaxis_showgrid=True,
            )
        elif label.lower() == "top":
            label = "Operativ temperatur"
            unit = "°C"
            max_dtick_x = max(50, round(len(df)/50, -2))
            tick0_y = int(df[5:].astype(float).min().iloc[0]) - 1
            print(tick0_y)
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
        elif label.lower() == "relhumid":
            unit = "%"
            label = "Relativ luftfugtighed"
            max_dtick_x = max(50, round(len(df)/50, -2))
            tick0_y = round(int(df[5:].astype(float).min().iloc[0]) - 5, -1)
            print(tick0_y)
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
        # elif label.lower() == "ventilout":
        #     unit = "$h^{-1}$"
        #     label = "AirChange"
        #     max_dtick_x = max(50, round(len(df)/50, -2))
        #     tick0_y = int(df[5:].astype(float).min().iloc[0]) - 1
        #     print(tick0_y)
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
        else:
            unit = ""


        

        for column in df.columns[5:]:
            # if column.startswith('label'):
                print(column)
                print(max(df[column]))
                # sorted_values = df[column].sort_values()
                fig.add_trace(go.Scatter(
                            x=list(range(len(df))), 
                            y=df[column],
                            mode='lines',
                            name=column))
                # df[column].to_excel(r'C:\Users\Mikkel H. Lauridsen\OneDrive - Aalborg Universitet\Undervisning\06 Prjekt\test.xlsx', index=False)
                
        # fig.add_trace(go.Scatter(
        #     x=list(range(len(df))),
        #     y=df["Co2 002"],
        # ))
                
        fig.update_layout(
            # xaxis_title="Brugstid [h]",
            # yaxis_title=f"{label} [{unit}]",
            width = (len(df)/2)+200,
            height = 300,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor = PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR,
            plot_bgcolor="white",
            # gridcolor='LightGrey',
            autosize = PLOTLY_STANDARD_AUTOSIZE,
            xaxis = dict(
                # showgrid=True,
                gridcolor='LightGrey',
                range=[0, len(df)],
                title = "Brugstid [h]",
            ),
            yaxis = dict(
                # showgrid=False,
                range=[0, max(df[5:])],
                title = f"{label} [{unit}]",
            ),
            autotypenumbers="convert types"
        )


        # fig.update_layout(yaxis=dict(
        #     title="Udnyttelses-faktor [%]",
        #     overlaying="y",
        #     side="right",
        #     range=[0,105], showgrid=False
        # ))

        # # fig.update_layout(
        # #     width=size_x*cell_x,
        # #     height=size_y*cell_y,
        # #     # margin=dict(l=5, r=5, t=5, b=5),
        # #     margin=dict(l=0, r=0, t=0, b=0),
        # #     paper_bgcolor = PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR,
        # #     # automargin = PLOTLY_STANDARD_AUTOMARGIN,
        # #     autosize = PLOTLY_STANDARD_AUTOSIZE,
        # #     )

        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        
        # Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save(f'figures output/ScatterPlot{label}.png')

        root.destroy()

if __name__ == "__main__":

    root = tk.Tk()

    path_var = os.path.normpath("C:\\Users\\Mikkel H. Lauridsen\\OneDrive - Aalborg Universitet\\Programmer\\03 BSimExtract\\Bsimdata.txt")
    dayprofile_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract/dayprofiles/dayprofile_altid.txt")
    # df = import_data(path_var)
    df = discard_data(import_data_dayprofile(path_var, dayprofile_var), "Co2")
    ScatterPlot(root, df)#.pack()

    root.mainloop()