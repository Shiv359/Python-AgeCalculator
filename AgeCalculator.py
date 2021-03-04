from tkinter import *
from datetime import date
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("655x433")
root.title("AGE CALCULATOR")
def Calcage():
    today=date.today()
    birthdate=date(int(yearentry.get()),int(monthentry.get()),int(dayentry.get()))
    age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    print(age)
    tmsg.showinfo("Age Calculator",f"{nameentry.get()} is  {age}  years old.")
l1=Label(root,text="Age Calculator",font="lucida 20 bold",bg="grey",fg="White").grid()

#f1=Frame(root,bg="grey",borderwidth=12,relief=SUNKEN).grid()

#l2=Label(f1,text="Name").grid(row=0,column=0)

name=Label(root,text="Name")
year=Label(root,text="Year")
month=Label(root,text="Month")
day=Label(root,text="Day")
name.grid(row=1)
year.grid(row=2)
month.grid(row=3)
day.grid(row=4)


namevalue=StringVar()
yearvalue=StringVar()
monthvalue=StringVar()
dayvalue=StringVar()

nameentry=Entry(root,textvariable=namevalue)
yearentry=Entry(root,textvariable=yearvalue)
monthentry=Entry(root,textvariable=monthvalue)
dayentry=Entry(root,textvariable=dayvalue)

nameentry.grid(row=1,column=1)
yearentry.grid(row=2,column=1)
monthentry.grid(row=3,column=1)
dayentry.grid(row=4,column=1)

b1=Button(root,text="Calculate Age",command=Calcage)
b1.grid(row=5,column=1)


root.mainloop()