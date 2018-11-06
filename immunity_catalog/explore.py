# binding <Return> event

import tkinter as tk
import tkinter.messagebox as msg

def show(event=None): # handler
    msg.showinfo('name', 'Your name is ' + inp.get())

m = tk.Tk()

prompt = tk.Label(m, text='Name: ')
prompt.pack(fill='x', side='left')

inp = tk.Entry(m)
inp.bind('<Return>', show) # binding the Return event with an handler
inp.pack(fill='x', side='left')

ok = tk.Button(m, text='GO', command=show)
ok.pack(fill='x', side='left')

m.mainloop()