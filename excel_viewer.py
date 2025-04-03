import tkinter as tk
from tkinter import ttk
import pandas as pd

class ExcelViewer:
    def __init__(self, root):
        self.root = root
        self.tree = ttk.Treeview(root, show="headings")
        self.tree.pack(expand=True, fill=tk.BOTH)

    def display_data(self, df):
        # Clear previous data
        for col in self.tree.get_children():
            self.tree.delete(col)

        # Set column headings
        self.tree["columns"] = list(df.columns)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        # Insert data
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))
