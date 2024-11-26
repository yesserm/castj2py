import tkinter as tk
from tkinter import filedialog, messagebox
from src.core.converter import convert_json_to_py


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.json_file_path = None
        self.convert_button = None
        self.load_button = None
        self.title("JSON and JS to Python Converter")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self, text="Load JSON File", command=self.load_json_file)
        self.load_button.pack(pady=20)
        self.convert_button = tk.Button(self, text="Convert to Python", command=self.convert_to_python)
        self.convert_button.pack(pady=20)

    def load_json_file(self): 
        self.json_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.json_file_path:
            messagebox.showinfo("File Loaded",f"Loaded {self.json_file_path}")

    def convert_to_python(self):
        if hasattr(self, 'json_file_path'):
            output_file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if output_file_path:
                convert_json_to_py(self.json_file_path, output_file_path)
                messagebox.showinfo("Conversion Complete",f"Saved converted file to {output_file_path}")
            else:
                messagebox.showwarning("No File Loaded", "Please load a JSON file first.")
