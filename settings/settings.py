"""
Settings for bsimextract
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk

"""
Importing internal modules
"""
# #* IMPORTANT: DO NOT CHANGE THESE LINES
# import os
# import sys
# sys.path = os.getcwd()
# #* IMPORTANT: DO NOT CHANGE THESE LINES


#! Colors
# Source: https://www.color-hex.com/color-palette/78917
#* Main program colors
COLOR_1 = "#f6f6f4"
COLOR_2 = "#edeae5"
COLOR_3 = "#ced9dd"
COLOR_4 = "#979fa5"
COLOR_5 = "#2f3d4c"
#* Widget fg color
FG_COLOR = "transparent"
#* Table formatting colors
COLORS = [
    ("Red", "#ff0000"),
    ("Lime", "#00ff00"),
    ("Blue", "#0000ff"),
    ("Purple", "#800080"),
    ("Orange", "#ffa500"),
    ("Yellow", "#ffff00"),
    ("Green", "#008000"),
    ("Teal", "#008080"),
    ("Aqua", "#00ffff"),
    ("Fuchsia", "#ff00ff")
]

#* Plotly colors
PLOTLY_COLORS = [
    "#211a52",
    "#594fbf",
    "#54616e",
    "#bb5b17",
    "#007fa3",
    "#0e8563",
    "#cc445b",
    "#97701f",
    "#a16547",
]

PLOTLY_COLORS_2 = [
    "#df8e2e",
    "#b19335",
    "#31a9c1",
    "#cc8b66",
    "#5caf8d",
    "#e78293",
]

#! Appearance
# COLOR_MODE = "dark"
COLOR_MODE = "light"

#! Grid structure
#* Standard column width
STANDARD_COLUMN_WIDTH_TOTAL = 300
STANDARD_COLUMN_WIDTH_2 = STANDARD_COLUMN_WIDTH_TOTAL / 2
STANDARD_COLUMN_WIDTH_2_3 = (STANDARD_COLUMN_WIDTH_TOTAL / 3) * 2
STANDARD_COLUMN_WIDTH_3 = STANDARD_COLUMN_WIDTH_TOTAL / 3
STANDARD_COLUMN_WIDTH_3_4 = (STANDARD_COLUMN_WIDTH_TOTAL / 4) * 3
STANDARD_COLUMN_WIDTH_4 = STANDARD_COLUMN_WIDTH_TOTAL / 4
STANDARD_COLUMN_WIDTH_4_5 = (STANDARD_COLUMN_WIDTH_TOTAL / 5) * 4
STANDARD_COLUMN_WIDTH_5 = STANDARD_COLUMN_WIDTH_TOTAL / 5

#* Standard padx and pady
STANDARD_PADX = 5
STANDARD_PADY = 5
STANDARD_PADX_CHECKBOX = 2
STANDARD_PADY_CHECKBOX = 2


#! Version
VERSION_NUMBER = "0.0.1"

#! Text settings
#* Fonts
TITLE_FONT = "montserrat"
TEXT_FONT = "montserrat"
TITLE_MENU_FONT = "montserrat"
PAGE_MENU_FONT = "montserrat"
#* Size
TITLE_SIZE = 14
TEXT_SIZE = 12
TITLE_MENU_SIZE = 12
PAGE_MENU_SIZE = 14
#* Weight
TITLE_WEIGHT = "bold"
TEXT_WEIGHT = "bold"
TITLE_MENU_WEIGHT = "normal"
PAGE_MENU_WEIGHT = "bold"

#! Start path
START_PATH = ""

#! Start dayprofile
DAYPROFILE_CO2_ALWAYS = "dayprofile_altid.txt"
DAYPROFILE_CO2_SUMMER = "dayprofile_sommer.txt"
DAYPROFILE_CO2_TRANSITION = "dayprofile_overgang.txt"
DAYPROFILE_CO2_WINTER = "dayprofile_vinter.txt"

DAYPROFILE_RH_ALWAYS = "dayprofile_altid.txt"
DAYPROFILE_RH_SUMMER = "dayprofile_sommer.txt"
DAYPROFILE_RH_TRANSITION = "dayprofile_overgang.txt"
DAYPROFILE_RH_WINTER = "dayprofile_vinter.txt"

DAYPROFILE_TEMP_ALWAYS = "dayprofile_altid.txt"
DAYPROFILE_TEMP_SUMMER = "dayprofile_sommer.txt"
DAYPROFILE_TEMP_TRANSITION = "dayprofile_overgang.txt"
DAYPROFILE_TEMP_WINTER = "dayprofile_vinter.txt"

DAYPROFILE_AIRCH_ALWAYS = "dayprofile_altid.txt"
DAYPROFILE_AIRCH_SUMMER = "dayprofile_sommer.txt"
DAYPROFILE_AIRCH_TRANSITION = "dayprofile_overgang.txt"
DAYPROFILE_AIRCH_WINTER = "dayprofile_vinter.txt"

#! Start CO2 settings
# CO2_MAXCO2_ONE = 1000
# CO2_MAXCO2_TWO = 1250
# CO2_MAXCO2_THREE = 1500
# CO2_FORMATCOLOR_ONE = "Yellow"
# CO2_FORMATCOLOR_TWO = "Orange"
# CO2_FORMATCOLOR_THREE = "Red"

CO2_PARAMETER_ALWAYS = [950, 1200]
# CO2_PARAMETER_ALWAYS = [950]
CO2_PARAMETER_SUMMER = [950, 1200]
CO2_PARAMETER_TRANSITION = [950, 1200]
CO2_PARAMETER_WINTER = [950, 1200]

#! Start Temp settings
# TEMP_HOUR_100 = 100
# TEMP_HOUR_25 = 25

# TEMP_MINTEMP = 20
# TEMP_MAXTEMP_100H = 27
# TEMP_MAXTEMP_25H = 28
# TEMP_FORMATCOLOR_MINTEMP = "Aqua"
# TEMP_FORMATCOLOR_MAXTEMP_100H = "Orange"
# TEMP_FORMATCOLOR_MAXTEMP_25H = "Red"

# TEMP_BETWEEN_MAX_SUMMER = 26
# TEMP_BETWEEN_MIN_SUMMER = 22
# TEMP_BETWEEN_MAX_TRANS = 26
# TEMP_BETWEEN_MIN_TRANS = 21
# TEMP_BETWEEN_MAX_WINTER = 25
# TEMP_BETWEEN_MIN_WINTER = 21
# TEMP_FORMATCOLOR_BETWEEN = "Purple"

TEMP_PARAMETER_ALWAYS = [27, 28]
TEMP_PARAMETER_SUMMER = ["-23", "23-26", 26]
TEMP_PARAMETER_TRANSITION = ["-20", "20-26", 26]
TEMP_PARAMETER_WINTER = ["-20", "20-25", 25]

#! Start RH settings
# RH_MINRH = 30
# RH_LOWMAXRH = 45
# RH_MAXRH = 70
# RH_FORMATCOLOR_MINRH = "Aqua"
# RH_FORMATCOLOR_LOWMAXRH = "Orange"
# RH_FORMATCOLOR_MAXRH = "Red"

RH_PARAMETER_ALWAYS = ["-25", "25-60", 60]
RH_PARAMETER_SUMMER = ["-25", "25-60", 60]
# RH_PARAMETER_SUMMER = ["-25", "25-45", 45]
RH_PARAMETER_TRANSITION = ["-25", "25-60", 60]
RH_PARAMETER_WINTER = ["-25", "25-60", 60]

#! Start Airch settings
# AIRCH_MAXAIRCH_ONE = 2
# AIRCH_MAXAIRCH_TWO = 3
# AIRCH_MAXAIRCH_THREE = 4 
# AIRCH_FORMATCOLOR_ONE = "Yellow"
# AIRCH_FORMATCOLOR_TWO = "Orange"
# AIRCH_FORMATCOLOR_THREE = "Red"

AIRCH_PARAMETER_ALWAYS = ["-2", "2-4", 4]
AIRCH_PARAMETER_SUMMER = ["-2", "2-4", 4]
AIRCH_PARAMETER_TRANSITION = ["-2", "2-4", 4]
AIRCH_PARAMETER_WINTER = ["-2", "2-4", 4]

#! Plotly
PLOTLY_STANDARD_MARGIN = dict(l=20, r=35, t=35, b=20)
PLOTLY_STANDARD_AUTOSIZE = True
# PLOTLY_STANDARD_AUTOMARGIN = True
PLOTLY_STANDARD_HEIGHT = 400
PLOTLY_STANDARD_WIDTH = 800
PLOTLY_STANDARD_PAPER_BACKGROUND_COLOR = "white"