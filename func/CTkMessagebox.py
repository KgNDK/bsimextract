"""
Modular CTkMessagebox module
"""

"""
# TODO LIST

# TODO: Make a modular CTkMessagebox module that can be called from the entire workspace/program
        #! ATM this is not possible
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

# def show_warning(text_message, text_title = "Warning Message!", image_icon = "warning", option_one = "Cancel", option_two = "Retry"):
#     msg = CTkMessagebox.CTkMessagebox(title = text_title, message = text_message, icon = image_icon, option_1 = option_one, option_2 = option_two)
#     response = msg.get()
        
# if __name__ == "__main__":  
#     root = ctk.CTk()

#     show_warning("test_message")

#     root.mainloop()

