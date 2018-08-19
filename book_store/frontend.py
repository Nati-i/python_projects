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

window = Tk()

e1 = Label(window,text='Title')
e1.grid(row=0,column=0)

e2 = Label(window,text='Author')
e2.grid(row=0,column=1)

e3 = Label(window,text='Year')
e3.grid(row=2,column=0)

e4 = Label(window,text='ISBN')
e4.grid(row=2,column=1)



b1 = Button(window,text="View All")
b1.grid(row=2,column=2)

b2 = Button(window,text='Search Entry')
b2.grid(row=3,column=2)

b3 = Button(window,text='Add Entry')
b3.grid(row=4,column=2)

b7 = Button(window,text='Attach Doc')
b7.grid(row=7,column=2)

b4 = Button(window,text='Update')
b4.grid(row=5,column=2)

b5 = Button(window,text='Delete')
b5.grid(row=6,column=2)

b6 = Button(window,text='Close')
b6.grid(row=7,column=2)

b7 = Button(window,text='Attach Doc')
b7.grid(row=7,column=2)






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


list1 = Listbox(window,height=6,width=35)
list1.grid(row=4,column=0,rowspan=6,columnspan=2)

# screen

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)





window.mainloop()
