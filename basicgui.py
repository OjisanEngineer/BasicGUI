from tkinter import *
from tkinter import messagebox

GUI = Tk()
GUI.title('Hello World')
GUI.geometry('500x500')

L1 = Label(GUI,text='Hello World',font=(None,20))
L1.pack()

def popup():
    messagebox.showinfo('Show popup','สวัสดีจ้าาา')


B1 = Button(GUI,text='Click me!',command=popup)
B1.pack()

GUI.mainloop()