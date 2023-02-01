from tkinter import *
from tkinter import messagebox

def button_1():
    messagebox.showinfo('Результат', int(a.get()) + int(b.get()))

def button_2():
    messagebox.showinfo('Результат', int(a.get()) - int(b.get()))

def button_3():
    messagebox.showinfo('Результат', int(a.get()) * int(b.get()))

def button_4():
    messagebox.showinfo('Результат', int(a.get()) / int(b.get()))

def button_5():
    messagebox.showinfo('Результат', int(a.get()) // int(b.get()))

def button_6():
    messagebox.showinfo('Результат', int(a.get()) % int(b.get()))

root = Tk()
root.title('калькулятор')
root.geometry('600x400')
a = Entry(root, width=15, bg='yellow', fg='black', font='consolas')
a.pack()
b = Entry(root, width=15, bg='yellow', fg='black', font='consolas')
b.pack()
Button(root, text='+', width=10, height=2, bg='white', command=button_1).pack()
Button(root, text='-', width=10, height=2, bg='white', command=button_2).pack()
Button(root, text='*', width=10, height=2, bg='white', command=button_3).pack()
Button(root, text='/', width=10, height=2, bg='white', command=button_4).pack()
Button(root, text='//', width=10, height=2, bg='white', command=button_5).pack()
Button(root, text='%', width=10, height=2, bg='white', command=button_6).pack()
root.mainloop()
