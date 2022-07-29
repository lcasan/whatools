import tkinter as tk
from .import window_position
from tkinter import ttk
from ..database import cursor
import sqlite3

class Form(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Form")
        self.resizable(False, False)
        self.geometry(window_position(self, 300, 250))

        #Entry
        ttk.Label(self, text='Group\'s name:').pack(pady=(10, 5))
        self.name = ttk.Entry(self)
        self.name.pack(fill='both', padx=15, pady=10)

        #Combobox for tags
        ttk.Label(self, text='Group\'s tag:').pack(pady=(10, 5))
        self.tag = ttk.Combobox(self)
        self.tag.pack(fill='both', padx=15, pady=10)

        ttk.Button(self, text='Add', command=self.create_group, style='Accent.TButton').pack(fill='both', padx=15, pady=(30, 5))
    
    '''
        Function for add new group to database
    '''
    def create_group(self):
        name = self.name.get()
        tag = self.tag.get()

        with sqlite3.connect('src/database/model.db') as db:
            cursor = db.cursor()
            cursor.execute("insert into grupo(name, tag, number_of_users) values (?, ?, ?)", (name, tag, 0))
            db.commit()

        self.destroy()
