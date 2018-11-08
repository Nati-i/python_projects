from tkinter import *
from backend_immunity import Database
import datetime

'''
Program to log the kinds of food consumed in a day to track what might be causing
allergic infllamatory reactions'''

database = Database("logs.db")

class Window(object):

        def __init__(self, window):
                
                self.window = window
                #window.configure(background='blue')

                self.food_list = []
                self.symptom_list = []

                self.foods = ''
                self.symptoms = ''

                self.date = datetime.date.today()

                self.window.wm_title("Food Logs")

                # Header (date)
                l3 = Label(window,text=self.date,fg="blue")
                l3.grid(row=0,column=2)

                # Items + Entry
                l1=Label(window,text="Items")
                l1.grid(row=2,column=0)

                self.title_text=StringVar()
                self.e1=Entry(window)
                self.e1.bind('<Return>', self.log_command)
                self.e1.grid(row=3, column=0)

                self.todays_list = Button(window,text="Today's List",width=14,
                command=self.todays_log)
                self.todays_list.grid(row=7,column=0)

                self.yesterday_list = Button(window,text="Yesterday's List",width=14,
                command=self.yesterdays_log)
                self.yesterday_list.grid(row=8,column=0)

                # List on a given day
                self.show_list = Button(window,text='Enter a Date to See List(MM/DD/YYYY)',width=30,command=self.show_list_on_date)
                self.show_list.grid(row=10,column=0)

                self.show_list_text = StringVar()
                self.e3 = Entry(window)
                self.e3.bind('<Return>', self.log_command)
                self.e3.grid(row=11,column=0)

                # Symptoms + Entry

                l2=Label(window,text="Symptoms")
                l2.grid(row=2,column=3)

                self.title_text=StringVar()
                self.e2=Entry(window)
                self.e2.bind('<Return>', self.log_command2)
                self.e2.grid(row=3, column=3)
                
                # Log button

                b1=Button(window,text="LOG",width=12,command=self.send_to_database)
                b1.grid(row=5,column=2)

                # List box 1

                l4 = Label(window,text="Items Included")
                l4.grid(row=0,column=7)

                self.list1=Listbox(window, height=24,width=35)
                self.list1.grid(row=2,column=6,rowspan=24,columnspan=3)

                # List box 2

                l5 = Label(window,text="Symptoms Included")
                l5.grid(row=0,column=43)

                self.list2 = Listbox(window,height=24,width=35)
                self.list2.grid(row=2,column=42,rowspan=24,columnspan=3)

                # List box 3 Notifications

                l6 = Label(window,text="Pannel Box")
                l6.grid(row=7,column=3)

                self.list3 = Listbox(window,height=20,width=20)
                self.list3.grid(row=8,column=3)

        def log_command(self,event):

                self.food_list.append(str(self.e1.get()))
                self.e1.delete(0,END)
                self.list1.delete(0,END)
                for item in self.food_list:
                        self.list1.insert(END,item)
        
        def log_command2(self,event):

                self.symptom_list.append(str(self.e2.get()))
                self.e2.delete(0,END)
                self.list2.delete(0,END)
                for item in self.symptom_list:
                        self.list2.insert(END,item)

        def send_to_database(self):

                self.foods = ' \n'.join(self.food_list)
                self.symptom = ' \n'.join(self.symptom_list)

                database.insert_food(self.date, self.foods)
                database.insert_symptoms(self.date, self.symptom)

                self.list1.delete(0,END)
                self.list1.insert(0,'Sent')

                self.list2.delete(0,END)
                self.list2.insert(0,'Sent')
                
        def todays_log(self):

                items = database.view_item_on_date(self.date)
                self.list1.delete(0,END)

                for i in range(len(items)):
                        for food in items[i][2].split(' \n'):
                                self.list1.insert(END,food)
        
        def yesterdays_log(self):

                items = database.view_item_on_date(self.date - datetime.timedelta(days=1))

                self.list1.delete(0,END)
                for i in range(len(items)):
                        for food in items[i][2].split(' \n'):
                                self.list1.insert(END,food)        
        
        def show_list_on_date(self):

                date_requested = str(self.e3.get())

                if date_requested == '':
                        self.list3.delete(0,END)
                        self.list3.insert(END,"Please Enter an Appropriate Date")

                try:
                        date_requested = datetime.datetime.strptime(date_requested, '%d/%m/%Y').date()
                except ValueError:
                        self.list3.delete(0,END)
                        self.list3.insert(END,"Please Enter an Appropriate Date")
                self.e3.delete(0,END)
                items = database.view_item_on_date(date_requested)
                print(date_requested)
                for i in range(len(items)):
                        for food in items[i][2].split(' \n'):
                                self.list1.insert(END,food)



window = Tk()
Window(window)
window.mainloop()


        