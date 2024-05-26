import tkinter as tk
class counter:
    def __init__(self,win):
        self.win = win
        win.geometry('400x300')
        self.var = tk.IntVar(value = 0)
        self.disp = tk.Label(win,textvariable=self.var,font = ('bold',20))
        self.disp.pack()
        tk.Button(win, text='Increement', command=self.action1).pack(side = tk.LEFT)
        tk.Button(win, text='Decreement', command=self.action2).pack(side = tk.RIGHT)

    def action1(self):
        data = self.var.get()+1
        self.var.set(data)
    def action2(self):
        data = self.var.get()-1
        self.var.set(data)

root = tk.Tk()
exc = counter(root)
root.mainloop()