import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JSON and JS to Python Converter")
        self.geometry("400x200")
