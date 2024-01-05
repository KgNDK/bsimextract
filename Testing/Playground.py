"""
Mainpage where the data is displayed in the frontend
"""

import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, font, messagebox
from functools import partial
from CTkMenuBar import *

"""
Making pages 
"""

class page_start(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)

        # grid layout
        self.rowconfigure((0, 1, 2, 3, 4), weight = 1)
        self.columnconfigure(0, weight = 1, uniform = "a")

        # widgets
        text_1 = "Welcome to BSimExtract"
        text_2 = "To run the program please go through the instructions below:"
        text_3 = "1. Coming soon"

        # labels
        ctk.CTkLabel(self, text = text_1, font = title_font).grid(row = 0, column = 0, sticky = "nsew")
        ctk.CTkLabel(self, text = text_2, font = text_font).grid(row = 1, column = 0, sticky = "nsew")
        ctk.CTkLabel(self, text = text_3, font = text_font).grid(row = 2, column = 0, sticky = "nsew")

class page_co2(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)

        # grid layout
        self.rowconfigure((0, 1, 2, 3, 4), weight = 1)
        self.columnconfigure(0, weight = 1, uniform = "a")

        # widgets
        text_1 = "Welcome to the page for Co2"

        # labels
        ctk.CTkLabel(self, text = text_1, font = title_font).grid(row = 0, column = 0, sticky = "nsew")


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
menu_dropdown_1.add_option(option="Import Data", command=lambda: print("Importing data"), font=menu1_font)
menu_dropdown_1.add_option(option="Open", command=lambda: print("Opening file"), font=menu1_font)
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
Different frames for start, co2, temperature, relhumid, airchange
"""
# page_start(app).pack(expand = True, fill = "both")
# page_co2(app).pack(expand = True, fill = "both")

def show_frame(frame):    
        page_start(app).pack_forget()
        page_co2(app).pack_forget()

        frame.pack(expand = True, fill = "both")  

app.mainloop()





        
        


# if __name__ == "__main__":  
#     root = tk.Tk()

#     root.title("TEST: page_start")
#     root.geometry("500x100")

#     page_start(root).pack(expand = True, fill = "both", padx = 10, pady = 10)

#     root.mainloop()
