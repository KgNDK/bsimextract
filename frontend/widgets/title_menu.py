"""
title menu for file, edit, view, and help and so on
"""

import tkinter as tk
import customtkinter as ctk
from CTkMenuBar import *






class title_menu:
    def __init__(self, parent):
        super().__init__(parent)

        self.text = ctk.CTkLabel(self, text="Title", font=TITLE_FONT)
        # # main title menu buttons
        # self.menu = CTkMenuBar(self)
        # self.button_file = self.menu.add_cascade("File")
        # self.button_edit = self.menu.add_cascade("Settings")
        # self.button_help = self.menu.add_cascade("Help")
        # self.button_report = self.menu.add_cascade("Report Bug")

        # # file dropdown menu
        # self.menu_dropdown_1 = CustomDropdownMenu(widget=self.button_file)
        # self.menu_dropdown_1.add_option(option="Import Data", command=lambda: print("Importing data"), font=TITLE_MENU_FONT)
        # self.menu_dropdown_1.add_option(option="Open", command=lambda: print("Opening file"), font=TITLE_MENU_FONT)
        # self.menu_dropdown_1.add_option(option="Save As", command=lambda: print("Save As"), font=TITLE_MENU_FONT)
        # self.menu_dropdown_1.add_option(option="Save Report", command=lambda: print("Save Report"), font=TITLE_MENU_FONT)






if __name__ == "__main__":  
    root = ctk.CTk()

    #! TO BE REMOVED - TEMPORARY
    TITLE_FONT = ctk.CTkFont(family="montserrat", size=20, weight="bold")
    TEXT_FONT= ctk.CTkFont(family="montserrat", size=12)
    TITLE_MENU_FONT= ctk.CTkFont(family="montserrat", size=12)
    PAGE_MENU_FONT = ctk.CTkFont(family="montserrat", size=14, weight="bold")
    COLOR_1 = "#f6f6f4"
    COLOR_2 = "#edeae5"
    COLOR_3 = "#ced9dd"
    COLOR_4 = "#979fa5"
    COLOR_5 = "#2f3d4c"


    root.title(f"TEST: {__doc__}")
    root.geometry("500x100")

    title_menu(root).pack()

    root.mainloop()
