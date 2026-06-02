#Python File Detection

import os

file_path = "stuff/test.txt.py "

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesnt exist")