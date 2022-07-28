from .import window_position
from ..drives import Browser
from tkinter import ttk
import tkinter as tk
import sv_ttk
from tkinter import filedialog
from emoji import emojize

groups = ['#1']

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
       
        #window config:
        self.parent = parent
        self.parent.title("Whatools")
        self.parent.tk.call('wm', 'iconphoto', self.parent._w, tk.PhotoImage(file='src/img/whatools.png'))
        #self.parent.update_idletasks()  
        self.parent.geometry(window_position(self.parent, 770, 550))



        # Make the app responsive
        #for index in (0, 1):
        #    self.columnconfigure(index=index, weight=1)
        #    self.rowconfigure(index=index, weight=1)

        #self.combo_list = ['label1', 'labe2', 'label3']
        
        # Create control variables
        self.msg = ''
        # Create widgets
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for the send msg
        self.send_frame = ttk.LabelFrame(
            self, text="Send message", padding=(20, 10))
        self.send_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Input text msg
        self.input_text = tk.Text(self.send_frame, width=51)
        self.input_text.pack(fill='both', expand=True)

        # Button Send
        ttk.Button(
            self.send_frame, text="Send", style="Accent.TButton",command=self.send_msg
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 5), pady=5)
        
        # Button Load
        ttk.Button(
            self.send_frame, text="Load", command= self.load, #style="Accent.TButton"
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 5), pady=5)

        # Button Save
        ttk.Button(
            self.send_frame, text="Save", command=self.save,#style="Accent.TButton",
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 0), pady=5)
        
        self.send_frame.columnconfigure(index=0, weight=1)

        #--------------------------------------------------------------------
        # Create a Frame for the groups
        self.group_frame = ttk.LabelFrame(
            self, text="Groups", padding=(20, 10))
        self.group_frame.grid(
            row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        #Filter by group
        self.search = ttk.Entry(self.group_frame)
        self.search.pack(fill='both', pady=5, padx=(0,8))

        #Filter by tag
        self.tags = ttk.Combobox(self.group_frame)
        self.tags.pack(fill='both', pady=5, padx=(0,8))

        # Panedwindow
        self.paned = ttk.PanedWindow(self.group_frame)
        self.paned.pack(fill='both',expand=True)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        #List of groups
        self.groups = ttk.Frame(self.pane_1)
        self.groups.pack(side="left", fill="y")

        ttk.Label(self.groups, text='first').pack()

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

    '''
        Function to load the templates saved in a custom directory
    '''
    def load(self): 
        try:
            path = filedialog.askopenfilename(initialdir = '/', 
                                          title = "Select a template", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))  
            with open(path,'r', encoding='utf8') as file:
                msg = file.read()
            self.input_text.insert('1.0', msg)
        except:
            print('Operation not completed in filedialog')
    
    '''
        Function to save in a custom directory the templates created in the text field
    '''
    def save(self):
        if self.input_text.edit_modified():
            extensions = [('All Files', '*.*'),('Text Document', '*.txt')]
            try:
                #Create file and save its path 
                path = filedialog.asksaveasfile(initialdir = "/home/lcasan/Documents/", filetypes=extensions)
                
                #Write in created file
                with open(path.name, 'w', encoding='utf8') as file:
                    file.write(self.input_text.get('1.0', 'end'))
            except:
                print('Operation not completed in filedialog')
        else:
            tk.messagebox.showinfo(message='Not changes in the text field yet')

    def send_msg(self):
        browser = Browser()
        self.msg = self.input_text.get('1.0', 'end')
        print('[Sending message]')
        browser.send_message(self.msg, groups)
