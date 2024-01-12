"""
Checkboxes for create_dayprofile
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import CTkMessagebox as CTkMessagebox
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

class hours_widget(ctk.CTkFrame):
    def __init__(self, parent, total_width):
        super().__init__(master = parent, fg_color = FG_COLOR)
        # grid layout
        element_width = total_width/24
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23), weight = 1)
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # Checkboxes for hours
        hours = [f"{i:02d}:00" for i in range(24)]
        hour_var = [ctk.BooleanVar(self) for _ in range(len(hours))]
        hour_checkboxes = [ctk.CTkCheckBox(self, text="", variable=hour_var[i], width = element_width) for i, hour in enumerate(hours)]
        for i, checkbox in enumerate(hour_checkboxes):
            checkbox.grid(row=2, column=i+1, sticky="s")
        hour_label = [ctk.CTkLabel(self, text = hour, font = text_font, width = element_width) for hour in hours]
        for i, hour_label in enumerate(hour_label):
            hour_label.grid(row=1, column=i+1, sticky="s")

class days_widget(ctk.CTkFrame):
    def __init__(self, parent, total_width):
        super().__init__(master = parent, fg_color = FG_COLOR)
        # grid layout
        element_width = total_width/7  
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1)
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # Checkboxes for days
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_var = [ctk.BooleanVar(self) for _ in range(len(days))]
        day_checkboxes = [ctk.CTkCheckBox(self, text="", variable=day_var[i], width = element_width) for i, day in enumerate(days)]
        for i, checkbox in enumerate(day_checkboxes):
            checkbox.grid(row=4, column=i+1, sticky="s")
        day_label = [ctk.CTkLabel(self, text = day, font = text_font, width = element_width) for day in days]
        for i, day_label in enumerate(day_label):
            day_label.grid(row=3, column=i+1, sticky="s")

class weeks_widget(ctk.CTkFrame):
    def __init__(self, parent, total_width):
        super().__init__(master = parent, fg_color = FG_COLOR)
        # grid layout
        element_width = total_width/27
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26), weight = 1)
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # Checkboxes for weeks
        weeks_first_half = [str(i) for i in range(1, 27)]
        weeks_var_first_half = [ctk.BooleanVar(self) for _ in range(len(weeks_first_half))]
        weeks_checkboxes_first_half = [ctk.CTkCheckBox(self, text="", variable=weeks_var_first_half[i], width = element_width) for i, week in enumerate(weeks_first_half)]
        for i, checkbox in enumerate(weeks_checkboxes_first_half):
            checkbox.grid(row=2, column=i+1, sticky="s")
        weeks_label_first_half = [ctk.CTkLabel(self, text = week, font = text_font, width = element_width) for week in weeks_first_half]
        for i, week_label in enumerate(weeks_label_first_half):
            week_label.grid(row=1, column=i+1, sticky="s")

        weeks_second_half = [str(i) for i in range(27, 53)]
        weeks_var_second_half = [ctk.BooleanVar(self) for _ in range(len(weeks_second_half))]
        weeks_checkboxes_second_half = [ctk.CTkCheckBox(self, text="", variable=weeks_var_second_half[i], width = element_width) for i, week in enumerate(weeks_second_half)]
        for i, checkbox in enumerate(weeks_checkboxes_second_half):
            checkbox.grid(row=4, column=i+1, sticky="s")
        weeks_label_second_half = [ctk.CTkLabel(self, text = week, font = text_font, width = element_width) for week in weeks_second_half]
        for i, week_label in enumerate(weeks_label_second_half):
            week_label.grid(row=3, column=i+1, sticky="s")

class months_widget(ctk.CTkFrame):
    def __init__(self, parent, total_width):
        super().__init__(master = parent, fg_color = FG_COLOR)
        # grid layout
        element_width = total_width/12
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight = 1)
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # Checkboxes for days
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month_var = [ctk.BooleanVar(self) for _ in range(len(months))]
        month_checkboxes = [ctk.CTkCheckBox(self, text="", variable=month_var[i], width = element_width) for i, month in enumerate(months)]
        for i, checkbox in enumerate(month_checkboxes):
            checkbox.grid(row=2, column=i+1, sticky="s")
        month_label = [ctk.CTkLabel(self, text = month, font = text_font, width = element_width) for month in months]
        for i, month_label in enumerate(month_label):
            month_label.grid(row=1, column=i+1, sticky="s")

if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode(COLOR_MODE)
    root.geometry("200x50")
    total_width = 1000
    hours_widget(root, total_width).pack()
    days_widget(root, total_width).pack()
    weeks_widget(root, total_width).pack()
    months_widget(root, total_width).pack()
    root.mainloop()