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
import tkinter as tk
from tkinter import filedialog
import pandas as pd

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

"""
Variables
"""
toggle_months = False
toggle_weeks = False
toggle_days = False
toggle_hours = False

class create_dayprofile(ctk.CTkToplevel):
    def __init__(self, parent, text_top_title = "Create a new dayprofile:"):
        super().__init__(master = parent)

        # setup
        self.title(text_top_title)
        self.geometry("700x875")
        #* Looking the size of the top level window because of performance hit when resizing
        self.resizable(False, False)

        # grid layout
        self.columnconfigure((1, 2, 4), weight = 1)
        self.columnconfigure((0, 3), weight = 2)
        self.columnconfigure((5), weight = 3)
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # text
        ctk.CTkLabel(self, text = "Please mark all the boxes that the dayprofile should be active for", font = title_font).grid(row = 0, column = 0, columnspan = 5, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Hours:", font = text_font).grid(row = 1, rowspan = 1, column = 4, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Days:", font = text_font).grid(row = 1, rowspan = 1, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Weeks:", font = text_font).grid(row = 1, columnspan = 2, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Months:", font = text_font).grid(row = 1, rowspan = 1, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Please write suffixation here:", font = text_font).grid(row = 0, column = 5, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # button
        ctk.CTkButton(self, text = "Save", command = lambda: save(name_var.get()), font = text_font).grid(row = 2, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "Open", command = lambda: open_dayprofile(), font = text_font).grid(row = 3, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "Exit", command = lambda: create_dayprofile.destroy(self), font = text_font).grid(row = 4, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        
        ctk.CTkButton(self, text = "All hours", command = lambda: toggle_hours(), font = text_font).grid(row = 6, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "All days", command = lambda: toggle_days(), font = text_font).grid(row = 7, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "All weeks", command = lambda: toggle_week(), font = text_font).grid(row = 8, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "All months", command = lambda: toggle_month(), font = text_font).grid(row = 9, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        ctk.CTkButton(self, text = "Invert hours", command = lambda: invert_all(hour_var), font = text_font).grid(row = 11, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "Invert days", command = lambda: invert_all(day_var), font = text_font).grid(row = 12, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "Invert weeks", command = lambda: invert_week(week_var_first_half, week_var_second_half), font = text_font).grid(row = 13, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "Invert months", command = lambda: invert_all(month_var), font = text_font).grid(row = 14, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        # toggle buttons logic
        def toggle_all(variables: list, current_var: str):
            toggle_value = current_var
            for var in variables:
                var.set(toggle_value)
                
        def toggle_month():
            global toggle_months
            toggle_months = not toggle_months  
            toggle_all(month_var, toggle_months)

        def toggle_week():
            global toggle_weeks
            toggle_weeks = not toggle_weeks
            toggle_all(week_var_first_half, toggle_weeks)
            toggle_all(week_var_second_half, toggle_weeks)

        def toggle_days():
            global toggle_days
            toggle_days = not toggle_days
            toggle_all(day_var, toggle_days)

        def toggle_hours():
            global toggle_hours
            toggle_hours = not toggle_hours
            toggle_all(hour_var, toggle_hours)

        # invert button logic
        def invert_all(variables: list) -> None:
            for var in variables:
                var.set(not var.get())

        def invert_week(week_var_first_half: list, week_var_second_half: list) -> None:
            invert_all(week_var_first_half)
            invert_all(week_var_second_half)

        # textbox
        name_var = ctk.StringVar(self)
        ctk.CTkEntry(self, textvariable = name_var, font = text_font).grid(row = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        # checkboxes
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month_var = [ctk.BooleanVar(self) for _ in range(len(months))]
        month_checkboxes = [ctk.CTkCheckBox(self, text=month, variable=month_var[i]) for i, month in enumerate(months)]
        for i, month_checkboxes in enumerate(month_checkboxes):
            month_checkboxes.grid(row=i+2, column=0, sticky="ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        weeks_first_half = [str(i) for i in range(0, 27)]
        week_var_first_half = [ctk.BooleanVar(self) for _ in range(len(weeks_first_half))]
        weeks_checkboxes_first_half = [ctk.CTkCheckBox(self, text=week, variable=week_var_first_half[i]) for i, week in enumerate(weeks_first_half)]
        for i, week_checkboxes in enumerate(weeks_checkboxes_first_half):
            week_checkboxes.grid(row=i+2, column=1, sticky="ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        weeks_second_half = [str(i) for i in range(27, 53)]
        week_var_second_half = [ctk.BooleanVar(self) for _ in range(len(weeks_second_half))]
        weeks_checkboxes_second_half = [ctk.CTkCheckBox(self, text=week, variable=week_var_second_half[i]) for i, week in enumerate(weeks_second_half)]
        for i, week_checkboxes in enumerate(weeks_checkboxes_second_half):
            week_checkboxes.grid(row=i+2, column=2, sticky="ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_var = [ctk.BooleanVar(self) for _ in range(len(days))]
        day_checkboxes = [ctk.CTkCheckBox(self, text=day, variable=day_var[i]) for i, day in enumerate(days)]
        for i, day_checkboxes in enumerate(day_checkboxes):
            day_checkboxes.grid(row=i+2, column=3, sticky="ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        hours = [str(i) for i in range(0, 24)]
        hour_var = [ctk.BooleanVar(self) for _ in range(len(hours))]
        hour_checkboxes = [ctk.CTkCheckBox(self, text=hour, variable=hour_var[i]) for i, hour in enumerate(hours)]
        for i, hour_checkboxes in enumerate(hour_checkboxes):
            hour_checkboxes.grid(row=i+2, column=4, sticky="ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        
        def open_dayprofile():
                CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Opening of an existing dayprofile_XXX.txt file is not yet implemented", icon = "warning")
        
        def save(name_text = None):
            if len(name_text) == 0:
                CTkMessagebox.CTkMessagebox(title = "Error!", message = "You need to give a suffixation for your dayprofile to be able to save!. An example can be 'AlwaysOn'.", icon = "cancel")
                return
            
            selected_months_tuple = tuple(month_var[i].get() for i in range(len(months)))
            selected_weeks_first_tuple = tuple(week_var_first_half[i].get() for i in range(len(weeks_first_half)))
            selected_weeks_second_tuple = tuple(week_var_second_half[i].get() for i in range(len(weeks_second_half)))
            selected_days_tuple = tuple(day_var[i].get() for i in range(len(days)))
            selected_hours_tuple = tuple(hour_var[i].get() for i in range(len(hours)))

            #? Alternative way of formatting the dayprofile when save with 0 and 1 instead of True and False
            # selected_months_str = str(selected_months_tuple).replace("(", "").replace(")", "").replace(",", "").replace("True", "1").replace("False", "0")
            # selected_weeks_str = str(selected_weeks_first_tuple + selected_weeks_second_tuple).replace("(", "").replace(")", "").replace(",", "").replace("True", "1").replace("False", "0")
            # selected_days_str = str(selected_days_tuple).replace("(", "").replace(")", "").replace(",", "").replace("True", "1").replace("False", "0")
            # selected_hours_str = str(selected_hours_tuple).replace("(", "").replace(")", "").replace(",", "").replace("True", "1").replace("False", "0")

            selected_months_str = str(selected_months_tuple).replace("(", "").replace(")", "").replace(",", "")
            selected_weeks_str = str(selected_weeks_first_tuple + selected_weeks_second_tuple).replace("(", "").replace(")", "").replace(",", "")
            selected_days_str = str(selected_days_tuple).replace("(", "").replace(")", "").replace(",", "")
            selected_hours_str = str(selected_hours_tuple).replace("(", "").replace(")", "").replace(",", "")

            months_df = pd.DataFrame({'Months': selected_months_str.split()})
            weeks_df = pd.DataFrame({'Weeks': selected_weeks_str.split()})
            days_df = pd.DataFrame({'Days': selected_days_str.split()})
            hours_df = pd.DataFrame({'Hours': selected_hours_str.split()})

            dayprofile_df = pd.concat([months_df, weeks_df, days_df, hours_df], axis=1)

            dayprofile_df = dayprofile_df.transpose()

            suggested_filename = f"dayprofile_{name_text}.txt"

            script_directory = os.path.join(os.getcwd(), "dayprofiles")

            file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=suggested_filename, initialdir=script_directory, filetypes=[("Text files", "*.txt")])

            if file_path:
                with open(file_path, "w") as file:
                    dayprofile_df.to_csv(file, sep='\t', index=False)

                print(f'Dayprofile saved too: {file_path}')
            
                create_dayprofile.destroy(self)




if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode(COLOR_MODE)
    root.geometry("200x50")
    create_dayprofile(root)
    root.mainloop()