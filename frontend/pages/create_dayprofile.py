"""
Toplevel page for creating a custom dayprofile
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
from CTkMenuBar import *
import webbrowser

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *
from frontend.widgets.create_dayprofile_widgets.create_dayprofile_checkbox import *

class create_dayprofile(ctk.CTkToplevel):
    def __init__(self, parent, text_top_title = "Create a new dayprofile:"):
        super().__init__(master = parent)

        # setup
        self.title(text_top_title)
        self.geometry("1200x340")
        self.minsize(1200, 340)

        # grid layout
        self.columnconfigure((0, 2), weight = 1)
        self.columnconfigure((1), weight = 3)
        total_width = 1000
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # text
        ctk.CTkLabel(self, text = "Please mark all the boxes that the dayprofile should be active for", font = title_font).grid(row = 0, column = 0, columnspan = 2, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "!This will be changes for a select name widget!", font = text_font).grid(row = 5, column = 0, columnspan = 2, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Hours:", font = text_font).grid(row = 1, rowspan = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Days:", font = text_font).grid(row = 2, rowspan = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Weeks:", font = text_font).grid(row = 3, rowspan = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Months:", font = text_font).grid(row = 4, rowspan = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)


        # button
        ctk.CTkButton(self, text = "Open dayprofile", command = self.open_dayprofile, font = text_font).grid(row = 0, column = 2, sticky = "ew", padx = 5, pady = 5)
        ctk.CTkButton(self, text = "All hours", command = self.all_hours, font = text_font).grid(row = 1, rowspan = 1, column = 2, sticky = "ew", padx = 5, pady = 5)
        ctk.CTkButton(self, text = "All days", command = self.all_days, font = text_font).grid(row = 2, rowspan = 1, column = 2, sticky = "ew", padx = 5, pady = 5)
        ctk.CTkButton(self, text = "All weeks", command = self.all_weeks, font = text_font).grid(row = 3, rowspan = 1, column = 2, sticky = "ew", padx = 5, pady = 5)
        ctk.CTkButton(self, text = "All months", command = self.all_months, font = text_font).grid(row = 4, rowspan = 1, column = 2, sticky = "ew", padx = 5, pady = 5)
        ctk.CTkButton(self, text = "Create dayprofile", command = self.make_dayprofile, font = text_font).grid(row = 5, column = 2, sticky = "ew", padx = 5, pady = 5)

        # Checkboxes
        hours_widget(self, total_width).grid(row = 1, column = 1)
        days_widget(self, total_width).grid(row = 2, column = 1)
        weeks_widget(self, total_width).grid(row = 3, column = 1)
        months_widget(self, total_width).grid(row = 4, column = 1)

    def open_dayprofile(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Opening of an existing dayprofile_XXX.txt file is not yet implemented", icon = "warning")
    
    def all_hours(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Toggling all hours is not yet implemented", icon = "warning")
    
    def all_days(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Togging all days is not yet implemented", icon = "warning")

    def all_weeks(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Togging all weeks is not yet implemented", icon = "warning")

    def all_months(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Togging all months is not yet implemented", icon = "warning")

    def make_dayprofile(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Creating a new dayprofile_XXX.txt file is not yet implemented", icon = "warning")

if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode(COLOR_MODE)
    root.geometry("200x50")
    create_dayprofile(root)
    root.mainloop()