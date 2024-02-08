"""
Page menu RelHumid page
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
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *
from frontend.widgets.dayprofile_single import dayprofile_single

class page_menu_rh(ctk.CTkFrame):
    def __init__(self, parent, rh_dayprofile_var):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for RelHumid under this
        dayprofile_single(self, "RelHumid", rh_dayprofile_var).pack(fill = "x", expand = True)

if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: Page menu RelHumid page")
    root.geometry("400x300")

    page_menu_rh(root).pack()

    root.mainloop()