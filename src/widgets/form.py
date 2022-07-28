import tkinter as tk
from .import window_position
from tkinter import ttk

class Form(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Form")
        self.resizable(False, False)
        self.geometry(window_position(self, 300, 250))


        ttk.Label(self, text='Group\'s name:').pack(pady=(10, 5))
        self.name = ttk.Entry(self,)
        self.name.pack(fill='both', padx=15, pady=10)

        ttk.Label(self, text='Group\'s tag:').pack(pady=(10, 5))
        self.name = ttk.Entry(self,)
        self.name.pack(fill='both', padx=15, pady=10)


        ttk.Button(self, text='Add', command=self.create_group, style='Accent.TButton').pack(fill='both', padx=15, pady=(30, 5))

    def create_group(self):
        pass