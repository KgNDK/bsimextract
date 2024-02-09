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

#! Appearance
COLOR_MODE = "dark"

#! Grid structure
#* Standard column width
STANDARD_COLUMN_WIDTH_TOTAL = 300
STANDARD_COLUMN_WIDTH_2 = STANDARD_COLUMN_WIDTH_TOTAL / 2
STANDARD_COLUMN_WIDTH_2_3 = (STANDARD_COLUMN_WIDTH_TOTAL / 3) * 2
STANDARD_COLUMN_WIDTH_3 = STANDARD_COLUMN_WIDTH_TOTAL / 3
STANDARD_COLUMN_WIDTH_3_4 = (STANDARD_COLUMN_WIDTH_TOTAL / 4) * 3
STANDARD_COLUMN_WIDTH_4 = STANDARD_COLUMN_WIDTH_TOTAL / 4
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
DAYPROFILE_CO2 = ""
DAYPROFILE_TEMP = ""
DAYPROFILE_RH = ""
DAYPROFILE_AIRCH = "" 

#! Start CO2 settings
CO2_MAXCO2_ONE = 1000
CO2_MAXCO2_TWO = 1250
CO2_MAXCO2_THREE = 1500
CO2_FORMATCOLOR_ONE = ""
CO2_FORMATCOLOR_TWO = "Orange"
CO2_FORMATCOLOR_THREE = "Red"

#! Start Temp settings

#! Start RH settings

#! Start Airch settings
AIRCH_MAXAIRCH_ONE = 2
AIRCH_MAXAIRCH_TWO = 3
AIRCH_MAXAIRCH_THREE = 4
AIRCH_FORMATCOLOR_ONE = ""
AIRCH_FORMATCOLOR_TWO = "Orange"
AIRCH_FORMATCOLOR_THREE = "Red"


