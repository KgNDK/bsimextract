"""
Let side menu for choosing setting for current page
"""

"""
# TODO LIST

# TODO: Make page_menu_start give values to other page_menu frames
# TODO: Finish page_menu frames
"""

"""
Importing extern modules
"""
import tkinter as tk
import customtkinter as ctk
from CTkMenuBar import *

"""
Importing internal modules
"""
import sys
sys.path.append("c:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/bsimextract")
from settings.settings import *


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

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: page_menu")
    root.geometry("800x300")

    page_menu(root).pack()

    root.mainloop()
