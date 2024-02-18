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
from backend.import_data import import_data
from backend.timemeasure import timeit

@timeit
class TablePlot(tk.Frame):
    def __init__(self, parent, df, size_y = 30, size_x = 20, cell_y = 20, cell_x = 70):
        tk.Frame.__init__(self, parent)

        # column_names = [column for column in df.columns[:size_y]]
        # print(column_names)

        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns[:size_x]),
                        fill_color=PLOTLY_COLORS[0],
                        align='center',
                        font=dict(color="white", size=12)),
            cells=dict(values=[df.iloc[:,num] for num in range(0, size_x)],
                    fill_color='#e8e8ed',
                    align='center',
                    font=dict(color="black", size=10)))
        ])

        fig.update_layout(
            width=size_x*cell_x,
            height=size_y*cell_y,
            # margin=dict(l=5, r=5, t=5, b=5),
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor = PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR,
            # automargin = PLOTLY_STANDARD_AUTOMARGIN,
            autosize = PLOTLY_STANDARD_AUTOSIZE,
            )

        if not os.path.exists("figures output"):
            os.mkdir("figures output")
        
        # Save the plot as a PNG
        img_bytes = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_bytes))
        img.save('figures output/TableStart.png')
        

# if __name__ == "__main__":

#     path_var = "C:\\Users\\Mikkel H. Lauridsen\\OneDrive - Aalborg Universitet\\Programmer\\03 BSimExtract\\Bsimdata.txt"
#     df = import_data(path_var)
#     TablePlot(root, df).pack()

# #     root.mainloop()