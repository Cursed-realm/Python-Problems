import tkinter as tk
 
root = tk.Tk()
root.geometry('400x200')
root.title('First App')
count = 0
def increase():
    global count
    count+=1
    disp.config(bg='skyblue',text=f'{count}')

def decrease():
    global count
    count -=1
    disp.config(bg='skyblue',text=f'{count}')

disp = tk.Label(root,text='Hello World')
disp.pack()

bt = tk.Button(root,text='Increment',command=increase)
bt.pack()

bt = tk.Button(root,text='Decrement',command=decrease)
bt.pack()

root.mainloop()



import tkinter as tk
 
root = tk.Tk()
root.geometry('400x200')
root.title('First App')
count = 0
def increase():
    global count
    count+=1
    disp.config(bg='skyblue',text=f'{count}')

def decrease():
    global count
    count -=1
    disp.config(bg='skyblue',text=f'{count}')

disp = tk.Label(root,font=('bold',300))
disp.pack()

bt = tk.Button(root,text='Increment',command=increase)
bt.pack(side=tk.RIGHT)

bt = tk.Button(root,text='Decrement',command=decrease)
bt.pack(side=tk.LEFT)

root.mainloop()


-----------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk
 
root = tk.Tk()
root.geometry('400x200')
root.title('Counter App')
var = tk.IntVar(value=0)
def increase():
    a = var.get()+1
    var.set(a)
    if a>=10:
        disp.config(fg='red')
    else:
        disp.config(fg='green')

def decrease():
    a = var.get()-1
    if a>=0:
       var.set(a)
    if a>=10:
        disp.config(fg='red')
    else:
        disp.config(fg='green')

disp = tk.Label(root,textvariable=var,font=('bold',100),fg='green')
disp.pack()

bt = tk.Button(root,text='Increment',command=increase)
bt.pack(side=tk.RIGHT)

bt = tk.Button(root,text='Decrement',command=decrease)
bt.pack(side=tk.LEFT)

root.mainloop()
