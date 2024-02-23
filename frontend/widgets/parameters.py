"""
Parameters widget
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
from tkinter import ttk
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
from backend.clearup import clear_figure_output

class parameters(ctk.CTkFrame):
    def __init__(self, 
                 parent,
                 parameter_var_always,
                 parameter_var_summer,
                 parameter_var_transition,
                 parameter_var_winter,
                 title_text = "",
                 label_text_always = "Always",
                 label_text_summer = "Summer",
                 label_text_transition = "Transition",
                 label_text_winter = "Winter"
                 ):
        super().__init__(master = parent, fg_color = FG_COLOR)

        #* font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        parameters_title(self, title_text, parameter_var_always, parameter_var_summer, parameter_var_transition, parameter_var_winter,).pack(fill = "x", expand = True)

        parameters_main(self, label_text_always, parameter_var_always).pack(fill = "x", expand = True)
        parameters_main(self, label_text_summer, parameter_var_summer).pack(fill = "x", expand = True)
        parameters_main(self, label_text_transition, parameter_var_transition).pack(fill = "x", expand = True)
        parameters_main(self, label_text_winter, parameter_var_winter).pack(fill = "x", expand = True)

        


class parameters_title(ctk.CTkFrame):
    def __init__(self, 
                 parent,
                 title_text,
                 parameter_var_always,
                 parameter_var_summer,
                 parameter_var_transition,
                 parameter_var_winter,
                 ):
        super().__init__(master = parent, fg_color = FG_COLOR)

        #* font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # grid layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((0, 1, 2), weight = 1, uniform="a")

        # text widgets
        ctk.CTkLabel(self, text = f"{title_text} parameters:", width = STANDARD_COLUMN_WIDTH_2_3, font = title_font).grid(row = 0, column = 0, columnspan = 2, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # button widget
        ctk.CTkButton(self, text = "Apply", command = lambda: apply_parameters(parameter_var_always, parameter_var_summer, parameter_var_transition, parameter_var_winter, title_text), width = STANDARD_COLUMN_WIDTH_3, font = text_font).grid(row = 0, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

    # def apply_parameters(self):
    #     print("Applying parameters")
    #     clear_figure_output()
    #     # Needs to reload the selected page to generate new figures


def apply_parameters(parameter_var_always, parameter_var_summer, parameter_var_transition, parameter_var_winter, title_text):
    parameter_vars = [parameter_var_always, parameter_var_summer, parameter_var_transition, parameter_var_winter]
    parameter_names = {0: "always", 1: "summer", 2: "transition", 3: "winter"}
    format_error = False
    error_messages = []
    for i, parameter_var in enumerate(parameter_vars):
        parameter_start = parameter_var.get()
        if not parameter_start:
            continue
        parameter = parameter_start.strip('"')
        if parameter.startswith("-"):
            try:
                float(parameter[1:])
                continue
            except ValueError:
                print(f"Error in {title_text} parameter_var_{parameter_names[i]}: Parameter {parameter_start} does not match the expected format.")
                error_messages.append(f"Error in {title_text} parameter_var_{parameter_names[i]}: Parameter {parameter_start} does not match the expected format.")
                format_error = True
        elif "-" in parameter:
            parts = parameter.split("-")
            if len(parts) == 2:
                try:
                    float(parts[0])
                    float(parts[1])
                    continue
                except ValueError:
                    print(f"Error in {title_text} parameter_var_{parameter_names[i]}: Parameter {parameter_start} does not match the expected format.")
                    error_messages.append(f"Error in {title_text} parameter_var_{parameter_names[i]}: Parameter {parameter_start} does not match the expected format.")
                    format_error = True
        else:
            try:
                float(parameter)
                continue
            except ValueError:
                print(f"Error in {title_text} parameter_var_{parameter_names[i]}: Parameter {parameter_start} does not match the expected format.")
                error_messages.append(f"Error in {title_text} parameter_var_{parameter_names[i]}: Parameter {parameter_start} does not match the expected format.")
                format_error = True
    if format_error:
        CTkMessagebox.CTkMessagebox(message="\n".join(error_messages), title="Warning Message!", icon="warning")
    if not format_error:
        print("Applying parameters")


class parameters_main(ctk.CTkFrame):
    def __init__(self, 
                 parent,
                 label_text,
                 parameter_var
                 ):
        super().__init__(master = parent, fg_color = FG_COLOR)

        #* font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # grid layout
        self.columnconfigure((0), weight=1, uniform = "a")
        self.columnconfigure((1), weight=2, uniform = "a")

        # text widget
        ctk.CTkLabel(self, text = label_text, width = STANDARD_COLUMN_WIDTH_3, font = text_font).grid(row = 0, column = 0, sticky = "nsew", padx = 10, pady = STANDARD_PADY)

        # entry widget
        ctk.CTkEntry(self, textvariable = parameter_var, width = STANDARD_COLUMN_WIDTH_2_3).grid(row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)








if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: parameters")
    root.geometry("400x400")

    parameters(root, title_text = "Co2").pack()

    root.mainloop()