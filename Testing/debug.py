import os
normalized_path = os.path.normpath("C:/Users/Mikkel H. Lauridsen/OneDrive - Aalborg Universitet/Programmer/03 BSimExtract/Bsimdata.txt")
formatted_path = r"{}".format(normalized_path)
print(f"r'{formatted_path}'")