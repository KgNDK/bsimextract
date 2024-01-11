"""
Co2 formatting of data widget where the user can choose max values and color formatting
"""

"""
# TODO LIST

# TODO: Make an error box appear when apply is pressed and the max value is not a int, nothing has been entered and max value is a float
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

class co2_format_widget(ctk.CTkFrame):
    def __init__(self, parent,
                 text_title = "Co2 hours above:",
                 text_button = "Apply",
                 text_max = "Max Co2 value:",
                 text_color = "Formatting color:"):
        super().__init__(master = parent, fg_color = FG_COLOR)

        # grid layout
        self.rowconfigure((0, 1, 2), weight = 1, uniform = "a")
        self.columnconfigure((0, 1, 2, 3), weight = 1, uniform = "a")

        # text widget
        ctk.CTkLabel(self, text = text_title).grid(row = 0, column = 0, columnspan = 3, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = text_max).grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = text_color).grid(row = 2, column = 0, sticky = "nsew", padx = 5, pady = 5)

        # button
        ctk.CTkButton(self, text = text_button, command = self.apply_formatting).grid(row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)

        # max value entry widget
        self.entry_1 = ctk.CTkEntry(self, width = 50)
        self.entry_1.grid(row = 1, column = 1, sticky = "nsew", padx = 5, pady = 5)
        self.entry_1.insert(0, "1000")
        
        self.entry_2 = ctk.CTkEntry(self, width = 50)
        self.entry_2.grid(row = 1, column = 2, sticky = "nsew", padx = 5, pady = 5)
        self.entry_2.insert(0, "1250")

        self.entry_3 = ctk.CTkEntry(self, width = 50)
        self.entry_3.grid(row = 1, column = 3, sticky = "nsew", padx = 5, pady = 5)
        self.entry_3.insert(0, "1500")

        # formatting color dropdown widget
        self.dropdown_1 = ctk.CTkComboBox(self, values = list(zip(*COLORS))[0])
        self.dropdown_1.grid(row = 2, column = 1, sticky = "nsew", padx = 5, pady = 5)
        self.dropdown_1.set("Yellow")
        
        self.dropdown_2 = ctk.CTkComboBox(self, values = list(zip(*COLORS))[0])
        self.dropdown_2.grid(row = 2, column = 2, sticky = "nsew", padx = 5, pady = 5)
        self.dropdown_2.set("Orange")
        
        self.dropdown_3 = ctk.CTkComboBox(self, values = list(zip(*COLORS))[0])
        self.dropdown_3.grid(row = 2, column = 3, sticky = "nsew", padx = 5, pady = 5)
        self.dropdown_3.set("Red")


    def apply_formatting(self):
        print("Applying formatting")


if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: co2_format_widget")
    root.geometry("600x150")

    co2_format_widget(root).pack()

    root.mainloop()