import os
import pandas as pd

def load_excel(file_path):
    return pd.read_excel(file_path)

def get_files_from_directory(directory):
    return [f for f in os.listdir(directory) if f.endswith('.xlsx')]
