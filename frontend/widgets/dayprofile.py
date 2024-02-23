"""
Dayprofile widget label_text and combobox side by side
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
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *


class dayprofile(ctk.CTkFrame):
    def __init__(self, parent, label_text, dayprofile_var):
        super().__init__(master = parent, fg_color = FG_COLOR)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # grid layout
        self.columnconfigure((0), weight=1, uniform = "a")
        self.columnconfigure((1), weight=2, uniform = "a")

        # text widget
        ctk.CTkLabel(self, text = label_text, width = STANDARD_COLUMN_WIDTH_3, font = text_font).grid(row = 0, column = 0, sticky = "nsew", padx = 10, pady = STANDARD_PADY)

        # combobox widget
        self.combobox = ctk.CTkComboBox(self, state="readonly", width = STANDARD_COLUMN_WIDTH_2_3, variable = dayprofile_var)
        self.combobox.set(dayprofile_var.get())
        self.combobox.grid(row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        self.populate_combobox()

    def populate_combobox(self):
        current_dir = os.getcwd()
        directory = os.path.join(current_dir, "dayprofiles")
        files = [f for f in os.listdir(directory) if f.endswith('.txt') and f.startswith("dayprofile")]
        
        self.combobox.configure(values = files)

if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: dayprofile_single")
    root.geometry("400x100")

    dayprofile_value = ctk.StringVar()

    dayprofile(root, "test_label", dayprofile_value).pack(fill = "x", expand = True, padx = 10, pady = 5)

    root.mainloop()