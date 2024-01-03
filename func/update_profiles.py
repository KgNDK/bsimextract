"""
Function for updating dayprofiles from dayprofiles folder
"""

import os

def update_profiles():
    profiles = [f for f in os.listdir() if f.startswith("dayprofile") and f.endswith(".txt")]
    if __name__ == "__main__":
        print("Retrieved dayprofiles:", profiles)
    
    for combobox in profile_comboboxes.values():
        combobox['values'] = profiles

        if __name__ == "__main__":
            print("Updated combobox values:", combobox['values'])