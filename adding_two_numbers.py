#create a window

from tkinter import *

a = Tk()
a.title('window')
a.geometry('500x500+300+100')
b=StringVar()
def com():
    c=b.get()
    lab12=Label(text=c,font=20).pack()

lab11=Label(text='Functionality to a button',font=30).pack()

button1= Button(text='Press to print', command= com).pack()


text = Entry(textvariable=b).pack()


a.mainloop()
