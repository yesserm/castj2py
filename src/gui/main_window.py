import tkinter as tk
import os
import sys
import logging
from tkinter import filedialog, messagebox
from src.core.converter import convert_json_to_py, convert_js_file_to_py, convert_js_to_py_js2py
from src.utils.conversion_dict import get_project_root, ConversionDict

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger('app_logger')


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.json_file_path = None
        self.js_file_path = None
        self.convert_button = None
        self.load_js_button = None
        self.load_button = None
        self.convert_js_button = None
        self.python_file_path = None
        self.is_json_file_loaded = False
        self.is_js_file_loaded = False
        self.title("JSON and JS to Python Converter")
        self.geometry("400x400")

        # Obtener el diccionario de conversión una sola vez
        db_path = os.path.join(get_project_root(), '..', 'conversion_dict.db')
        conversion_instance = ConversionDict(db_path)
        self.conversion_dict = conversion_instance.get_conversion_dict()

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self, text="Load JSON File", command=self.load_json_file)
        self.load_button.pack(pady=20)
        self.load_js_button = tk.Button(self, text="Load JS File", command=self.load_js_file)
        self.load_js_button.pack(pady=20)
        self.convert_button = tk.Button(self, text="Convert to Python", command=self.convert_to_python)
        self.convert_button.pack(pady=20)
        self.convert_js_button = tk.Button(self, text="Convert JS to Python", command=self.convert_js_to_python)
        self.convert_js_button.pack(pady=20)

    def load_json_file(self):
        self.json_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.json_file_path:
            self.is_json_file_loaded = True
            self.is_js_file_loaded = False
            messagebox.showinfo("File Loaded", f"Loaded {self.json_file_path}")

    def load_js_file(self):
        self.js_file_path = filedialog.askopenfilename(filetypes=[("JavaScript files", "*.js")])
        if self.js_file_path:
            self.is_js_file_loaded = True
            self.is_json_file_loaded = False
            messagebox.showinfo("File Loaded", f"Loaded {self.js_file_path}")

    def convert_js_to_python(self):
        if hasattr(self, 'js_file_path'):
            output_file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                            filetypes=[("Python files", "*.py")])
            if self.is_json_file_loaded and output_file_path and self.js_file_path and self.conversion_dict:
                convert_js_file_to_py(self.js_file_path, output_file_path, self.conversion_dict)
                messagebox.showinfo("Conversion Complete", f"Saved converted file to {output_file_path}")
            elif self.is_js_file_loaded and output_file_path and self.js_file_path:
                convert_js_to_py_js2py(self.js_file_path, output_file_path)
                messagebox.showinfo("Conversion Complete", f"Saved converted file to {output_file_path}")
            else:
                messagebox.showwarning("No File Loaded", "Please load a JS file first.")

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