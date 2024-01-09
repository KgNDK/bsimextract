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
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *

#* page menus
from frontend.pages.page_menu_start import page_menu_start
from frontend.pages.page_menu_co2 import page_menu_co2
from frontend.pages.page_menu_rh import page_menu_rh
from frontend.pages.page_menu_temp import page_menu_temp
from frontend.pages.page_menu_airch import page_menu_airch


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
        
if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: page_menu")
    root.geometry("800x300")

    page_menu(root).pack()

    root.mainloop()
