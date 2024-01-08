"""
Let side menu for choosing setting for current page
"""

import tkinter as tk
import customtkinter as ctk
from CTkMenuBar import *

# TODO: Make settings.py in this file

class page_menu(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(master = parent)

        # tabs
        self.add("Start")
        self.add("Co2")
        self.add("RelHumid")
        self.add("Temperature")
        self.add("AirChange")

        # widgets
        page_menu_start(self.tab("Start"))
        page_menu_co2(self.tab("Co2"))
        page_menu_rh(self.tab("RelHumid"))
        page_menu_temp(self.tab("Temperature"))
        page_menu_airch(self.tab("AirChange"))
        
class page_menu_start(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for start under this

class page_menu_co2(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for Co2 under this

class page_menu_rh(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for RelHumid under this

class page_menu_temp(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for Temperature under this

class page_menu_airch(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for AirChange under this




if __name__ == "__main__":  
    root = ctk.CTk()

    #! TO BE REMOVED - TEMPORARY SETTINGS
    TITLE_FONT = ctk.CTkFont(family="montserrat", size=20, weight="bold")
    TEXT_FONT= ctk.CTkFont(family="montserrat", size=12)
    TITLE_MENU_FONT= ctk.CTkFont(family="montserrat", size=12)
    PAGE_MENU_FONT = ctk.CTkFont(family="montserrat", size=14, weight="bold")
    COLOR_1 = "#f6f6f4"
    COLOR_2 = "#edeae5"
    COLOR_3 = "#ced9dd"
    COLOR_4 = "#979fa5"
    COLOR_5 = "#2f3d4c"
    COLOR_MODE = "dark"

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: page_menu")
    root.geometry("800x300")

    page_menu(root).pack()

    root.mainloop()
