"""
Script for plotting measurement data
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

from backend.import_data import import_data
from settings.settings import *
from backend.import_data import import_data
from backend.import_data import import_data_dayprofile
from backend.time import timeit
from backend.sort_data import discard_data
from func.figures.scatter_plot import ScatterPlot
from func.figures.bar_plot import BarPlot
from func.figures.distribution_plot import DistributionPlot



path_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/DATA/Data til Mikkel 1.th..txt")
dayprofile_var = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract/dayprofiles/dayprofile_altid.txt")
df = discard_data(import_data(path_var), "Top ")
# df = df.drop(634)

# print(len(df.columns))

# parameters = []
# parameters = [950, 1200] # Co2
parameters = [27, 28] # Top
# parameters = ["-25", "25-60", 60] # RelHumid
# parameters = [PAS] # AirChange





# print(df)


if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: display_rh")
    root.geometry("800x300")

    ScatterPlot(root, df, Interval_unit = "d", parameters = parameters)
    BarPlot(root, df, parameters, Interval = "Dage", Interval_unit = "d")
    DistributionPlot(root, df, parameters=parameters)

    root.destroy()

    root.mainloop()