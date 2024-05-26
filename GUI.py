import tkinter as tk
 
root = tk.Tk()
root.geometry('400x200')
root.title('First App')
count = 0
def action():
    global count
    count+=1
    disp.config(bg='skyblue',text=f'You cliked{count}times')

disp = tk.Label(root,text='Hello World')
disp.pack()

bt = tk.Button(root,text='Click Me',command=action)
bt.pack()

root.mainloop()