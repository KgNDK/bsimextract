"""
TITLE
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

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *

# class PlotlyPlot(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
        
#         # Create a plotly figure
#         fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 1, 2], mode='lines'))
        
#         # Save the plot as a PNG
#         img_bytes = fig.to_image(format="png")
#         img = Image.open(io.BytesIO(img_bytes))
#         img.save('plotly_plot.png')
        
#         # Display the plot in the Tkinter GUI
#         photo = ImageTk.PhotoImage(img)
#         label = tk.Label(self, image=photo)
#         label.image = photo
#         label.pack()

# class PlotlyPlot(tk.Frame):
#     def __init__(self, parent, df = None, x_label = "", y_label = "", title = "", marginal_x = 10, marginal_y = 10):
#         tk.Frame.__init__(self, master = parent)
        
#         if df == "":
#             print(f"Dataframe {df} has no data, using random data instead")
#             x_values = np.random.random(50)
#             x_values = ", ".join(map(str, x_values))
#             y_values = np.random.random(50)
#             y_values = ", ".join(map(str, y_values))
#             print(x_values)
#             print(y_values)
            

#         # Create a plotly figure
#         fig = px.scatter(x = x_values, y = y_values, marginal_x=marginal_x, marginal_y=marginal_y, title = title, labels = dict(x = x_label, y = y_label))
        
#         # Save the plot as a PNG
#         img_bytes = fig.to_image(format="png")
#         img = Image.open(io.BytesIO(img_bytes))
#         img.save(f"{str(parent).removeprefix('.!')}_figure.png")
        
#         # Display the plot in the Tkinter GUI
#         photo = ImageTk.PhotoImage(img)
#         label = tk.Label(self, image=photo)
#         label.image = photo
#         label.pack()

# class PlotlyPlot(tk.Frame):
#     def __init__(self, parent, df = None, x_label = "", y_label = "", title = "", marginal_x = 10, marginal_y = 10):
#         tk.Frame.__init__(self, master = parent)
        
#         if df == "" or df == None:
#             print(f"Dataframe {df} has no data, using random data instead")
#             # x_values = np.random.random(50)
#             # x_values_str = ", ".join(map(str, x_values))
#             # y_values = np.random.random(50)
#             # y_values_str = ", ".join(map(str, y_values))
#             # print(x_values_str)
#             # print(y_values_str)
#             array_1 = np.random.randn(50,4)
#             df_1 = pd.DataFrame(array_1, columns=['a', 'b', 'c', 'd'])
#             df_1.head()

#         # Create a plotly figure
#         # fig = px.scatter(df_1, marginal_x=marginal_x, marginal_y=marginal_y, title = title, labels = dict(x = x_label, y = y_label))
#         fig = px.scatter(df_1, x='a', y='b', marginal_x=marginal_x, marginal_y=marginal_y, title = title, labels = dict(x = x_label, y = y_label)) 


#         # Save the plot as a PNG
#         img_bytes = fig.to_image(format="png")
#         img = Image.open(io.BytesIO(img_bytes))
#         img.save(f"{str(parent).removeprefix('.!')}_figure.png")
        
#         # Display the plot in the Tkinter GUI
#         photo = ImageTk.PhotoImage(img)
#         label = tk.Label(self, image=photo)
#         label.image = photo
#         label.pack()

class PlotlyPlot(tk.Frame):
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
        if not os.path.exists("Figures"):
            os.mkdir("Figures")
        
        # Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save('plotly_plot.png')
        
        # Display the plot in the Tkinter GUI
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack()