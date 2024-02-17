"""
Random filler plot for testing gui
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
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

class TestPlot(tk.Frame):
    def __init__(self, parent, x_values = None, y_values = None, title = ""):


        tk.Frame.__init__(self, parent)
        
        # If no data is provided, generate random data
        N = 100
        test = False
        if x_values == None:
            x_values = np.random.randn(N)
            test = True
        if y_values == None:
            y_values = np.random.randn(N)
            test = True
        if test == True:
            colors = np.random.rand(N)
            sz = np.random.rand(N) * 30

        # Setting data
        x = x_values
        y = y_values

        # Create a plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=go.scatter.Marker(
                size=sz,
                color=colors,
                opacity=0.6,
                colorscale="Viridis"
            ),
            
        ))
        fig.update_layout(width=PLOTLY_STANDARD_WIDTH,
            height=PLOTLY_STANDARD_HEIGHT,
            margin=PLOTLY_STANDARD_MARGIN,
            paper_bgcolor = PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR,
            # automargin = PLOTLY_STANDARD_AUTOMARGIN,
            autosize = PLOTLY_STANDARD_AUTOSIZE,
            )

        # Making a export folder if not present
        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        
        # Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save('figures output/TestPlot.png')
        
        # Display the plot in the Tkinter GUI
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack()

class TestTable(tk.Frame):
    def __init__(self, parent, plot_height = PLOTLY_STANDARD_HEIGHT, plot_width = PLOTLY_STANDARD_WIDTH, size_y = 30, size_x = 20, cell_y = 20, cell_x = 70):
        tk.Frame.__init__(self, parent)

        # Create a random 100x4 array
        array_1 = np.random.randint(0, 101, size=(size_y, size_x))

        # Create a list of column names from 'A' to 'Z' and beyond
        column_names = ["".join(item) for item in itertools.product(string.ascii_uppercase, repeat=2)][:array_1.shape[1]]

        # Create a DataFrame from the array with column names
        df = pd.DataFrame(array_1, columns=column_names)

        fig = go.Figure(data=[go.Table(
            # height=plot_height,
            # width=plot_width,
            header=dict(values=list(df.columns),
                        fill_color='paleturquoise',
                        align='left'
                        ),
            cells=dict(values=[df[column_name] for column_name in column_names],
                    fill_color='lavender',
                    align='left',
                    height = 30),
            columnwidth=[10] * len(column_names)
            )])

        fig.update_layout(
            width=size_x*cell_x,
            height=size_y*cell_y,
            margin=dict(l=5, r=5, t=5, b=5),
            paper_bgcolor = PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR,
            # automargin = PLOTLY_STANDARD_AUTOMARGIN,
            autosize = PLOTLY_STANDARD_AUTOSIZE,
            )

        
        
        # Making a export folder if not present
        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        
        # Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save('figures output/TestTable.png')
