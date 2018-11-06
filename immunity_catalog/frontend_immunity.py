from tkinter import *
from backend_immunity import Database
import datetime

database = Database("books.db")

class Window(object):

        def __init__(self, window):
                
                self.window = window
                self.food_list = []

                self.date = datetime.date.today()

                self.window.wm_title("Food Logs")

                l1=Label(window,text="Items")
                l1.grid(row=0,column=0)


                l2=Label(window,text="Symptoms")
                l2.grid(row=0,column=2)


                self.title_text=StringVar()
                self.e1=Entry(window)
                self.e1.bind('<Return>', self.log_command)
                self.e1.grid(row=1, column=0)

                b1=Button(window,text="LOG",width=12,command=self.send_to_database)
                b1.grid(row=3,column=0)

                self.list1=Listbox(window, height=6,width=35)
                self.list1.grid(row=2,column=2,rowspan=10,columnspan=2)


                sb1 = Scrollbar(window)
                sb1.grid(row=2,column=4,rowspan=10)

                self.list1.bind('<<ListboxSelect>>',self.print_items)

        def log_command(self,event):

                self.food_list.append(str(self.e1.get()))
                self.e1.delete(0,END)

        def send_to_database(self):
                foods = '\n'.join(self.food_list)
                database.insert_food(self.date, foods)
                # print(foods + '\nDone')
                
        def print_items(self):
                for item in self.food_list:
                        print(item)

        

window = Tk()
Window(window)
window.mainloop()


        