import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
import os
from utils.file_handler import load_excel, get_files_from_directory
from utils.auth import authenticate_admin
from excel_viewer import ExcelViewer

class RemarksApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Свод замечаний DPTRA")
        self.root.geometry("1000x600")
        self.directory = None
        self.is_authenticated = False

        self.tree = ttk.Treeview(self.root)
        self.tree.pack(expand=True, fill=tk.BOTH)

        button_select_folder = tk.Button(self.root, text="Выбрать папку", command=self.select_folder)
        button_select_folder.pack()

        self.excel_viewer = ExcelViewer(self.root)

    def select_folder(self):
        if not self.is_authenticated:
            if not self.authenticate_user():
                return

        self.directory = filedialog.askdirectory()
        if self.directory:
            self.load_files()

    def load_files(self):
        if not self.directory:
            messagebox.showwarning("Предупреждение", "Путь к папке не установлен.")
            return

        for item in self.tree.get_children():
            self.tree.delete(item)

        files = get_files_from_directory(self.directory)
        for file in files:
            self.tree.insert('', 'end', text=file, values=('',))

    def view_file(self, event):
        selected_item = self.tree.selection()[0]
        file_name = self.tree.item(selected_item, 'text')
        file_path = os.path.join(self.directory, file_name)

        try:
            df = load_excel(file_path)
            self.excel_viewer.display_data(df)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при чтении файла: {e}")

    def authenticate_user(self):
        login = simpledialog.askstring("Вход", "Логин:", show='*')
        password = simpledialog.askstring("Вход", "Пароль:", show='*')

        if authenticate_admin(login, password):
            self.is_authenticated = True
            return True
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль.")
            return False

    def run(self):
        self.tree.bind('<Double-1>', self.view_file)
        self.root.mainloop()
