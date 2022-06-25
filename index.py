from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    root = Tk()

    # =========================================== Getting Screen Width ==================================================================
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry = "%dx%d+%d+%d" % (w, h, 0, 0)

    root.geometry("500x300+320+200")
    root.title('Login Form')
  
    root.mainloop()
