from traceback import print_tb
from typing import Dict
from .import window_position
from ..drives import Browser
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from .form import Form
import sqlite3

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        #window config:
        self.parent = parent
        self.parent.title("Whatools")
        self.parent.tk.call('wm', 'iconphoto', self.parent._w, tk.PhotoImage(file='src/img/whatools.png'))
        self.parent.update_idletasks()  
        self.parent.geometry(window_position(self.parent, 850, 600))

        #Make the app responsive
        for index in (0, 1):
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)
        
        #Control variables
        self.selected_groups = {} #Set of selected groups
        self.start = True 


        #Create widgets
        self.setup_widgets()

    def setup_widgets(self):
        ####### SECTION MESSAGE #######

        # Create a Frame for the send msg
        send_frame = ttk.LabelFrame(self, text="Send message", padding=(20, 10))
        send_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        # Input text msg
        self.input_text = tk.Text(send_frame, width=51, height=22)
        self.input_text.pack(fill='both', expand=True)

        frm = ttk.Frame(send_frame)
        frm.pack(fill='x')

        # Button Send
        ttk.Button(
            frm, text="Send", style="Accent.TButton",command=self.send_msg
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 5), pady=5)
        
        #Button Load Image
        self.img_path = 'none'
        self.button_image = ttk.Button(send_frame, text="Image", command= self.load_img)
        self.button_image.pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 5), pady=5)

        # Button Load
        ttk.Button(
            send_frame, text="Load", command= self.load
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 5), pady=5)

        # Button Save
        ttk.Button(
            send_frame, text="Save", command=self.save
        ).pack(side=tk.LEFT, fill='both', expand=True, padx=(0, 5), pady=5)

        send_frame.columnconfigure(index=0, weight=1)

        ####### SECTION GROUPS #######
        # Create a Frame for the groups
        self.group_frame = ttk.LabelFrame(self, text="Groups", padding=(20, 10))
        self.group_frame.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")

        #Filter group by name
        self.var_search = tk.StringVar()
        self.search = ttk.Entry(self.group_frame, textvariable=self.var_search)
        self.search.pack(fill='both', pady=5, padx=(0,8))

        #Filter group by tag
        self.var_tag = tk.StringVar()        
        self.combobox_tag = ttk.Combobox(self.group_frame, textvariable=self.var_tag)      
        self.combobox_tag.pack(fill='both', pady=5, padx=(0,8))

        # Panedwindow
        self.paned = ttk.PanedWindow(self.group_frame)
        self.paned.pack(fill='both',expand=True)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.paned)
        self.scrollbar.pack(side="right", fill="y")

        #Temporal canvas
        self.canvas = tk.Canvas()
        
        #List of groups
        self.update()

        #Add new group
        frm_group = ttk.Frame(self.group_frame)
        frm_group.pack(fill='both', expand=True)
        ttk.Button(frm_group, text='Create', style='Accent.TButton', command=self.new_group).pack(side='top', fill='both', pady=5, padx=(0,8))

        #Delete group
        ttk.Button(self.group_frame, text='Delete', command=self.delete_group).pack(side='left', fill='both', expand=True, pady=5, padx=(0,8))

        #Button select all groups
        ttk.Button(self.group_frame, text='check all', command=self.check_all).pack(side='left', fill='both', expand=True, pady=5, padx=(0,8))

         #Button select all groups
        ttk.Button(self.group_frame, text='uncheck all', command=self.uncheck_all).pack(side='left', fill='both', expand=True, pady=5, padx=(0,8))

        #Tag for group
        ttk.Button(self.group_frame, text='Tag').pack(side='left', expand=True,fill='both', pady=5, padx=(0,8))

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

        self.var_search.trace_add('write', self.filter_by_name)
        self.var_tag.trace_add('write', self.filter_by_tag)        

    '''
        Function to send a message to all groups
    '''
    def send_msg(self):            
        #Msg
        msg = self.input_text.get('1.0', 'end')

        #List of groups selected
        groups = []
        for checkbutton in self.ls_checkbutton:
            if checkbutton[0] == True:
                print(checkbutton[1])
                #groups.append(checkbutton[1])
        
        browser = Browser()
        print('[Sending message]')
        if self.img_path != 'none':
            if self.input_text.edit_modified():
                print('True, True')
                browser.send_message(msg, groups, True, True, self.img_path)
            else:
                print('True, False')
                browser.send_message(msg, groups, True, False, self.img_path)
        else:
            print('False, True')
            browser.send_message(msg, groups, False, True, self.img_path)   
                    
    '''
        Function to load the templates saved in a custom directory
    '''
    def load(self): 
        try:
            path = filedialog.askopenfilename(initialdir = '/', 
                                          title = "Select a template", 
                                          filetypes = (("text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))  
            with open(path,'r', encoding='utf8') as file:
                msg = file.read()
            self.input_text.insert('1.0', msg)
        except:
            print('Operation not completed in filedialog')
    
    '''
        Function to load the image path
    '''
    def load_img(self):
        path = filedialog.askopenfilename(title = 'Select image', filetypes = (('jpeg files', '*.jpeg'), ('all files', '*.*')))
        
        #Change path for windows
        path = path.split('/')
        self.img_path = path[0]

        for i in range(1, len(path)):
            self.img_path += '\\'
            self.img_path += path[i] 

        #change style of button
        if self.img_path != '':         
            self.button_image.config(style='Accent.TButton')
        else:
            self.button_image.config(style='TButton')

    '''
        Function to save in a custom directory the templates created in the text field
    '''
    def save(self):
        if self.input_text.edit_modified():
            extensions = [('text document', '*.txt'), ('all files', '*.*'),]
            try:
                #Create file and save its path 
                path = filedialog.asksaveasfile(initialdir = "/", filetypes=extensions)
                
                #Write in created file
                with open(path.name, 'w', encoding='utf8') as file:
                    file.write(self.input_text.get('1.0', 'end'))
            except:
                print('Operation not completed in filedialog')
        else:
            tk.messagebox.showinfo(message='Not changes in the text field yet')

    '''
        Function to create new group
    '''
    def new_group(self):
        self.parent.wait_window(Form(parent=self.parent, tags=list(self.tags)))
        self.update()
        print('[updated groups]')
    
    '''
        Function to delete group
    '''
    def delete_group(self):
        #List of groups selected
        groups = []
        for checkbutton in self.ls_checkbutton:
            if checkbutton[0].get() == True:
                groups.append(checkbutton[1])
        
        #Query to database
        with sqlite3.connect('src/database/model.db') as db:
            cursor = db.cursor()
        
            for group in groups:
                cursor.execute('delete from grupo where name = \'' + group + '\'')
            
            db.commit()

        self.update()

    '''
        Function for update all elements in window
    '''
    def update(self):
        #Query to database
        with sqlite3.connect('src/database/model.db') as db:
            cursor = db.cursor()
            self.tags = set(cursor.execute('select tag from grupo').fetchall())
            self.groups = cursor.execute('select name, tag from grupo').fetchall()
        
        #update tags
        self.combobox_tag.config(values=list(self.tags))

        #Control variables for groups
        if self.start == True:
            self.start = False
            for group in self.groups:
                self.selected_groups[group[0]] = tk.BooleanVar()

        #update groups
        self.update_groups(self.groups)
    
    '''
        Function for update the groups
    '''
    def update_groups(self, groups):
        self.canvas.destroy()
        
        #Create canvas
        self.canvas = tk.Canvas(self.paned,width=10, height=340, scrollregion=(0,0,10,30*len(groups)))
        self.canvas.pack(fill='both')
        
        #Update list of groups
        posy = 3
        for group in groups:
            self.canvas.create_window(2, posy, anchor="nw", window=ttk.Checkbutton(self.canvas, text= group[0], variable=self.selected_groups[group[0]]))
            posy = posy + 30
            
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        
    '''
        Function for filter groups by name
    '''
    def filter_by_name(self, *arg):
        text = self.search.get()
        if text != '':
            #find substring in string
            ls_groups = []
            for group in self.groups:
                if text == group[0][0:len(text)]:
                    ls_groups.append(group)
                    continue

            self.update_groups(ls_groups)
        else:
            self.update() 

    '''
        Function for filter groups by tag
    '''
    def filter_by_tag(self,*arg):
        text = self.combobox_tag.get()
        if text != '':
            #find substring in string
            ls_groups = []
            for group in self.groups:
                if text == group[1]:
                    ls_groups.append((group))
                    continue

            self.groups = ls_groups
            self.update_groups(self.groups)
        else:
            self.update()
        
    '''
        Function for check all visible groups
    '''
    def check_all(self):
        for group in self.groups:
            self.selected_groups[group[0]] = True

    '''
        Function for uncheck all visible groups
    '''
    def uncheck_all(self):
        for group in self.groups:
            self.selected_groups[group[0]] = tk.BooleanVar()
        
        self.update_groups(self.groups)
            
 
       
        
            
  