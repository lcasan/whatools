import tkinter as tk
import sv_ttk
import src


if __name__ == "__main__":
    src.create_db() #Create database if not exist
    
    root = tk.Tk()
    sv_ttk.set_theme("light") #Define theme for GUI 
    
    app = src.App(parent=root)
    app.pack(fill="both", expand=False)
    app.mainloop()