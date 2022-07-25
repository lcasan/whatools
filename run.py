import tkinter as tk
import sv_ttk
import src


if __name__ == "__main__":
    root = tk.Tk()
    sv_ttk.set_theme("dark")

    app = src.App(parent=root)
    app.pack(fill="both", expand=False)
    app.mainloop()