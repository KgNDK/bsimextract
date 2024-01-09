"""
Page menu AirChange page
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
import customtkinter as ctk

"""
Importing internal modules
"""
import sys
sys.path.append("c:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract")
from settings.settings import *

class page_menu_airch(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for AirChange under this