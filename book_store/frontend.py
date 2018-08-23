"""
Frontend program for a read books catalogue
Title, Authour
Year, ISBN

User can:
    view all records
    search an Entry
    add an entry
    update an Entry
    close

"""

from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title=title_var.get(),author=author_var.get(),year=year_var.get(),isbn=isbn_var.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title=title_var.get(),author=author_var.get(),year=year_var.get(),isbn=isbn_var.get())
    list1.delete(0,END)
    list1.insert(END,(title_var.get(),author_var.get(),year_var.get(),isbn_var.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()
        selected_tuple = list1.get(index)
        title.delete(0,END)
        title.insert(END,selected_tuple[1])
        author.delete(0,END)
        author.insert(END,selected_tuple[2])
        year.delete(0,END)
        year.insert(END,selected_tuple[3])
        isbn.delete(0,END)
        isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_var.get(),author_var.get(),year_var.get(),isbn_var.get())

def close_command():
    window.destroy()


window = Tk()

window.wm_title("Book Store")

e1 = Label(window,text='Title')
e1.grid(row=0,column=0)

e2 = Label(window,text='Author')
e2.grid(row=0,column=1)

e3 = Label(window,text='Year')
e3.grid(row=2,column=0)

e4 = Label(window,text='ISBN')
e4.grid(row=2,column=1)


# Text Boxes

# Title
title_var = StringVar()
title = Entry(window,textvariable=title_var)
title.grid(row=1,column=0)
# Author
author_var = StringVar()
author = Entry(window,textvariable=author_var)
author.grid(row=1,column=1)
# Year
year_var = StringVar()
year = Entry(window,textvariable=year_var)
year.grid(row=3,column=0)
# ISBN
isbn_var = StringVar()
isbn = Entry(window,textvariable=isbn_var)
isbn.grid(row=3,column=1)


# Screen
list1 = Listbox(window,height=6,width=35)
list1.grid(row=4,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=5,column=2,rowspan=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

# Buttons

b1 = Button(window,text="View All",command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text='Search Entry',command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text='Add Entry',command=add_command)
b3.grid(row=4,column=3)

b7 = Button(window,text='Attach Doc')
b7.grid(row=7,column=3)

b4 = Button(window,text='Update Selected',command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text='Delete Selected',command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text='Close',command=close_command)
b6.grid(row=8,column=3)

b7 = Button(window,text='Attach Doc')
b7.grid(row=7,column=3)



window.mainloop()
