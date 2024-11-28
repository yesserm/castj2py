import tkinter as tk
import os
import sys
import logging
from tkinter import filedialog, messagebox
from src.core.converter import convert_json_to_py
from src.utils.conversion_dict import get_project_root, ConversionDict

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger('app_logger')


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.json_file_path = None
        self.convert_button = None
        self.load_button = None
        self.python_file_path = None
        self.title("JSON and JS to Python Converter")
        self.geometry("400x200")

        # Obtener el diccionario de conversión una sola vez
        db_path = os.path.join(get_project_root(), '..', 'conversion_dict.db')
        conversion_instance = ConversionDict(db_path)
        self.conversion_dict = conversion_instance.get_conversion_dict()

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self, text="Load JSON File", command=self.load_json_file)
        self.load_button.pack(pady=20)
        self.convert_button = tk.Button(self, text="Convert to Python", command=self.convert_to_python)
        self.convert_button.pack(pady=20)

    def load_json_file(self):
        self.json_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.json_file_path:
            messagebox.showinfo("File Loaded", f"Loaded {self.json_file_path}")

    def convert_to_python(self):
        if hasattr(self, 'json_file_path'):
            output_file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                            filetypes=[("Python files", "*.py")])
            if output_file_path:
                convert_json_to_py(self.json_file_path, output_file_path)
                messagebox.showinfo("Conversion Complete", f"Saved converted file to {output_file_path}")
            else:
                messagebox.showwarning("No File Loaded", "Please load a JSON file first.")

    def generate_python_code(self, pycode):
        # generate python file from pycode
        if hasattr(self, 'python_file_path'):
            output_file_path = filedialog.askdirectory(
                initialdir=os.path.dirname(self.python_file_path),
                title="Select Output Directory",
                mustexist=True
            )
            if output_file_path:
                with open(os.path.join(output_file_path, 'generated_code.py'), 'w') as file:
                    file.write(pycode)
                messagebox.showinfo("Conversion Complete", f"Saved converted file to {output_file_path}")