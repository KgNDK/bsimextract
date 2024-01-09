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
    def __init__(self, parent, label_text):
        super().__init__(master = parent, fg_color = FG_COLOR)

        # grid layout
        self.columnconfigure((0), weight=1)
        self.columnconfigure((1), weight=2)

        # text widget
        ctk.CTkLabel(self, text = label_text).grid(row = 0, column = 0, sticky = "nsew", padx = 10, pady = 5)

        # combobox widget
        self.combobox = ctk.CTkComboBox(self, state="readonly")
        self.combobox.grid(row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
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

    dayprofile(root, "test_label").pack(fill = "x", expand = True, padx = 10, pady = 5)

    root.mainloop()