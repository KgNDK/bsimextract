"""
Importing file widgets with header text
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *
from frontend.widgets.import_file import import_file


class import_file_widget(ctk.CTkFrame):
    def __init__(self, parent, path_var, new_data_var):
        super().__init__(master = parent, fg_color = FG_COLOR)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # Import file widget
        import_file(self, path_var, new_data_var).pack(fill = "x", expand = True)
        


if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: import_file_widget")
    root.geometry("400x100")

    import_file_widget(root, "test_button", "test_title").pack()

    root.mainloop()