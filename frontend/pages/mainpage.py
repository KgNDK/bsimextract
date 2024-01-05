"""
Mainpage where the data is displayed in the frontend
"""

import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, font
from functools import partial
from CTkMenuBar import *

"""
Initial program
"""
program_name = "BSimExtract"
program_version = "0.0.1"

"""
Prepping application
"""
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title(f"{program_name} - {program_version}")
app.geometry("1600x1000")

"""
Prepping fonts
"""
title_font = ctk.CTkFont(family="montserrat", size=20, weight="bold")
text_font = ctk.CTkFont(family="montserrat", size=12)
menu1_font = ctk.CTkFont(family="montserrat", size=12)
menu2_font = ctk.CTkFont(family="montserrat", size=14, weight="bold")

"""
First menubar
"""
menu = CTkMenuBar(app)
menu.configure(bg_color="#2f3d4c")

menu_button_1 = menu.add_cascade("File", font=menu1_font)
menu_button_2 = menu.add_cascade("Settings", font=menu1_font)
menu_button_3 = menu.add_cascade("Documentation", command=lambda: print("Open GitHub Wiki"), font=menu1_font)
menu_button_4 = menu.add_cascade("Report an Issue", command=lambda: print("Open Github Issues"), font=menu1_font)

menu_dropdown_1 = CustomDropdownMenu(widget=menu_button_1)
menu_dropdown_1.add_option(option="Open", command=lambda: print("Open"), font=menu1_font)
menu_dropdown_1.add_option(option="Save As", command=lambda: print("Save As"), font=menu1_font)
menu_dropdown_1.add_option(option="Save Report", command=lambda: print("Save Report"), font=menu1_font)

menu_dropdown_2 = CustomDropdownMenu(widget=menu_button_2)
menu_dropdown_2.add_option(option="Initial Setup", command=lambda: print("Initial Setup"), font=menu1_font)

"""
Second menubar
"""
menu_1 = CTkMenuBar(app)
menu_1.configure(bg_color="#696f73")

menu_button_a = menu_1.add_cascade("Co2", command=lambda: print("Show Co2 Frame"), font=menu2_font)
menu_button_b = menu_1.add_cascade("Temperature", command=lambda: print("Show Temperature Frame"), font=menu2_font)
menu_button_d = menu_1.add_cascade("RelHumid", command=lambda: print("Show RelHumid Frame"), font=menu2_font)
menu_button_e = menu_1.add_cascade("AirChange", command=lambda: print("Show AirChange Frame"), font=menu2_font)

"""
Different frames for co2, temperature, relhumid, airchange
"""



app.mainloop()

