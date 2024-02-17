"""
TITLE
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

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *

class TablePlot(tk.Frame):
    def __init__(self, parent, df, cell_y = 20, cell_x = 70):
        tk.Frame.__init__(self, parent)

        fig = go.Figure(data=[go.Table(
            # height=plot_height,
            # width=plot_width,
            header=dict(values=list(df.columns)[:5],
                        fill_color='paleturquoise',
                        align='left'
                        ),
            cells=dict(values=[df[column_name][:5] for column_name in list(df.columns)[:5]],
                    fill_color='lavender',
                    align='left',
                    height = 30),
            # columnwidth=[10] * len(column_names)
            )])
        print(list(df.columns)[:5])
        print([df[column_name][:5] for column_name in list(df.columns)[:5]])
        print("2")
        fig.update_layout(
            width=len(df.columns)*cell_x,
            height=len(df)*cell_y,
            margin=dict(l=5, r=5, t=5, b=5),
            paper_bgcolor = PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR,
            # automargin = PLOTLY_STANDARD_AUTOMARGIN,
            autosize = PLOTLY_STANDARD_AUTOSIZE,
            )
        print("3")
        # fig.show()
        
        # Making a export folder if not present
        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        print("4")
        # Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        print("5")
        img = Image.open(io.BytesIO(img_bytes))
        print("6")
        img.save('figures output/Imported Data Table.png')