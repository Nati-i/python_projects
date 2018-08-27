"""
Frontend program for a read books catalogue
self.title, Authour
self.year, self.isbn

User can:
    view all records
    search an Entry
    add an entry
    update an Entry
    close

"""

from tkinter import *
from backend import Database



class Application:

    def __init__(self,master):

        self.master = master
        self.database = Database("books.db")
        master.wm_self.title("Book Store")


        self.e1 = Label(master,text='self.title')
        self.e1.grid(row=0,column=0)

        self.e2 = Label(master,text='self.author')
        self.e2.grid(row=0,column=1)

        self.e3 = Label(master,text='self.year')
        self.e3.grid(row=2,column=0)

        self.e4 = Label(master,text='self.isbn')
        self.e4.grid(row=2,column=1)


        # Text Boxes

        # self.title
        self.title_var = StringVar()
        self.title = Entry(master,textvariable=self.title_var)
        self.title.grid(row=1,column=0)
        # self.author
        self.author_var = StringVar()
        self.author = Entry(master,textvariable=self.author_var)
        self.author.grid(row=1,column=1)
        # self.year
        self.year_var = StringVar()
        self.year = Entry(master,textvariable=self.year_var)
        self.year.grid(row=3,column=0)
        # self.isbn
        self.isbn_var = StringVar()
        self.isbn = Entry(master,textvariable=self.isbn_var)
        self.isbn.grid(row=3,column=1)


        # Screen
        self.list1 = Listbox(master,height=6,width=35)
        self.list1.grid(row=4,column=0,rowspan=6,columnspan=2)

        sself.b1 = Scrollbar(master)
        sself.b1.grid(row=5,column=2,rowspan=2)

        self.list1.configure(yscrollcommand=sself.b1.set)
        sself.b1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        # Buttons

        self.b1 = Button(master,text="View All",command=self.view_command)
        self.b1.grid(row=2,column=3)

        self.b2 = Button(master,text='Search Entry',command=self.search_command)
        self.b2.grid(row=3,column=3)

        self.b3 = Button(master,text='Add Entry',command=self.add_command)
        self.b3.grid(row=4,column=3)

        self.b4 = Button(master,text='Update Selected',command=self.update_command)
        self.b4.grid(row=5,column=3)

        self.b5 = Button(master,text='Delete Selected',command=self.delete_command)
        self.b5.grid(row=6,column=3)

        self.b6 = Button(master,text='Close',command=self.close_command)
        self.b6.grid(row=8,column=3)

        self.b7 = Button(master,text='Attach Doc')
        self.b7.grid(row=7,column=3)

    def get_selected_row(self,event):
        try:
            global selected_tuple
            index=self.list1.curselection()
            selected_tuple = self.list1.get(index)
            self.title.delete(0,END)
            self.title.insert(END,selected_tuple[1])
            self.author.delete(0,END)
            self.author.insert(END,selected_tuple[2])
            self.year.delete(0,END)
            self.year.insert(END,selected_tuple[3])
            self.isbn.delete(0,END)
            self.isbn.insert(END,selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for row in self.database.view():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in self.database.search(self.title=self.title_var.get(),self.author=self.author_var.get(),self.year=self.year_var.get(),self.isbn=self.isbn_var.get()):
            self.list1.insert(END,row)

    def add_command(self):
        self.database.insert(self.title=self.title_var.get(),self.author=self.author_var.get(),self.year=self.year_var.get(),self.isbn=self.isbn_var.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_var.get(),self.author_var.get(),self.year_var.get(),self.isbn_var.get()))



    def delete_command(self):
        self.database.delete(selected_tuple[0])

    def update_command(self):
        self.database.update(selected_tuple[0],self.title_var.get(),self.author_var.get(),self.year_var.get(),self.isbn_var.get())

    def close_command(self):
        self.database.close()
        master.destroy()











root = Tk()
app = Application(root)
root.mainloop()
