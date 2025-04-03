import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
from file_handler import load_excel, save_summary, get_files_from_directory
from data_processor import summarize_remarks

class RemarksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Свод замечаний DPTRA")
        self.root.geometry("800x600")
        self.directory = None

        self.tree = ttk.Treeview(root)
        self.tree.pack(expand=True, fill=tk.BOTH)

        button_add = tk.Button(root, text="Добавить файл", command=self.add_file)
        button_add.pack()

        button_admin = tk.Button(root, text="Войти как администратор", command=self.admin_login)
        button_admin.pack()

    def load_files(self):
        if not self.directory:
            messagebox.showwarning("Предупреждение", "Путь к папке не установлен. Войдите как администратор.")
            return

        files = get_files_from_directory(self.directory)
        for file in files:
            file_path = os.path.join(self.directory, file)
            df = load_excel(file_path)
            self.tree.insert('', 'end', text=file, values=('',))
            for index, row in df.iterrows():
                self.tree.insert(file, 'end', text=f"Замечание {index+1}", values=(row.tolist(),))

    def add_file(self):
        if not self.directory:
            messagebox.showwarning("Предупреждение", "Путь к папке не установлен. Войдите как администратор.")
            return

        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if not file_path:
            return

        try:
            df = load_excel(file_path)
            file_name = os.path.basename(file_path)
            save_path = os.path.join(self.directory, file_name)
            save_summary(df, save_path)
            self.tree.insert('', 'end', text=file_name, values=('',))
            for index, row in df.iterrows():
                self.tree.insert(file_name, 'end', text=f"Замечание {index+1}", values=(row.tolist(),))
            messagebox.showinfo("Успех", "Файл успешно добавлен!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

    def admin_login(self):
        login = simpledialog.askstring("Вход", "Логин:", show='*')
        password = simpledialog.askstring("Вход", "Пароль:", show='*')

        if login == "admin" and password == "admin":
            self.directory = filedialog.askdirectory()
            self.load_files()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль.")

def create_gui():
    root = tk.Tk()
    app = RemarksApp(root)
    root.mainloop()
