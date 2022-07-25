from .import window_position
from tkinter import ttk
import tkinter as tk
import sv_ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
       
        #window config:
        self.parent = parent
        self.parent.title("Whatools")
        self.parent.tk.call('wm', 'iconphoto', self.parent._w, tk.PhotoImage(file='src/img/whatools.png'))
        self.parent.update_idletasks()  
        self.parent.geometry(window_position(self.parent, 800, 550))



        # Make the app responsive
        for index in (0, 1):
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        self.combo_list = ['label1', 'labe2', 'label3']
        # Create control variables

        # Create widgets
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for the send msg
        self.send_frame = ttk.LabelFrame(
            self, text="Send message", padding=(20, 10))
        self.send_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Entry for input text
        self.input_text = tk.Text(self.send_frame, width=98)
        self.input_text.pack(fill='both', expand=True)

        # Button Save
        ttk.Button(
            self.send_frame, text="Send", style="Accent.TButton",
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 5), pady=5)

        ttk.Button(
            self.send_frame, text="Load", #style="Accent.TButton"
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 5), pady=5)

        ttk.Button(
            self.send_frame, text="Save", #style="Accent.TButton"
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 0), pady=5)

        self.send_frame.columnconfigure(index=0, weight=1)

        #--------------------------------------------------------------------
        # Create a Frame for the groups
        self.group_frame = ttk.LabelFrame(
            self, text="Groups", padding=(20, 10))
        self.group_frame.grid(
            row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        #search group Combobox
        #self.combobox = ttk.Combobox(self.group_frame, values=self.combo_list)
        #self.combobox.current(0)
        #self.combobox.pack(side=tk.LEFT)

        #Add Group Button:
        


        # Panedwindow
        self.paned = ttk.PanedWindow(self.group_frame)
        self.paned.pack(fill='both',expand=True)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            columns=("1", "2"),
            height=10,
            selectmode="browse",
            show=("tree",),
            yscrollcommand=self.scrollbar.set,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Treeview columns
        self.treeview.column("#0", anchor="w", width=120)
        self.treeview.column(1, anchor="w", width=120)
        self.treeview.column(2, anchor="w", width=120)

        # Define treeview data
        treeview_data = [
            ("", 1, "Confituras", ("Usuarios", "Value 1")),
            (1, 2, "David Capo 🤬🤬Stgo compra y venta #1", ("135", "Value 1.1")),
            (1, 3, "David Capo 🤬🤬Stgo compra y venta #2", ("1587", "Value 1.2")),
            (1, 4, "David Capo 🤬🤬 Stgo compra y venta#4", ("45", "Value 1.3")),
            (1, 5, "David Capo 🤬🤬 Stgo compra y venta#6", ("478", "Value 1.4")),
            ("", 6, "Otros grupos", ("Usuarios", "Value 2")),
            (6, 7, "Compra y Venta Pochy 2", ("456", "Value 2.1")),
            (6, 8, "Ventas Baratillo Stgo No5", ("365", "Value 2.2")),
        ]

        # Insert treeview data
        for item in treeview_data:
            parent, iid, text, values = item
            self.treeview.insert(
                parent=parent, index="end", iid=iid, text=text, values=values
            )

            if not parent or iid in {8, 21}:
                self.treeview.item(iid, open=True)  # Open parents

        # Select and scroll
        self.treeview.selection_set("8")
        self.treeview.see("7")


        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))
