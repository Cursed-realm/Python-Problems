import tkinter as tk
from tkinter import messagebox as mb

class MessagePopUp:
    def __init__(self,win):
        self.win = win 

        self.entry = tk.Entry(win)
        self.entry.pack()

        self.bt1 = tk.Button(win,text = 'show data', command=self.action)
        self.bt1.pack()

    def action(self):
        mb.showinfo('Greeting',self.entry.get())

if __name__ =='__main__':
    root = tk.Tk()
    exc = MessagePopUp(root)
    root.mainloop()
-----------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox as mb

class MessagePopUp:
    def __init__(self,win):
        self.win = win 

        self.entry = tk.Entry(win)
        self.entry.pack()

        self.bt1 = tk.Button(win,text = 'show data', command=self.action)
        self.bt1.pack()

    def action(self):
        # mb.showerror('Greeting',self.entry.get())
        var = mb.askquestion('Exit','Do you want to exit?')
        if var.casefold()=='yes':
            self.win.destroy()


if __name__ =='__main__':
    root = tk.Tk()
    exc = MessagePopUp(root)
    root.mainloop()
