from tkinter import *

window = Tk()

def kg_to_others():
    gram=float(kg_value.get())*1000
    pound=float(kg_value.get())*2.20462
    ounce=float(kg_value.get())*35.274

    t1.delete("1.0",END)
    t1.insert(END,gram)

    t2.delete("1.0",END)
    t2.insert(END,pound)

    t3.delete("1.0", END)
    t3.insert(END,ounce)

b1 = Button(window,text="Convert",command=kg_to_others)
b1.grid(row=0,column=2)

e1 = Label(window,text='Kg')
e1.grid(row=0,column=0)

kg_value = StringVar()
kg = Entry(window,textvariable=kg_value)
kg.grid(row=0,column=1)

# Grams

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=0)


# Pounds

t2 = Text(window,height=1,width=20)
t2.grid(row=1,column=1)

# Ounces

t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=2)



window.mainloop()
