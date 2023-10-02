from tkinter import *
from tkinter import ttk


window = Tk()

#create notebook
notebook = ttk.Notebook(window)

#create tabs
tab1 = Frame(notebook)
tab2= Frame(notebook)

#add tabs to notebook
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text= 'Tab 2')
notebook.pack(expand= True, fill= 'both')#expand makes it expand as you maximize your screensize while FILL fills it as you expand

#add elements or components to tabs
Label(tab1, text='I am Tab 1', font=('Times New Roman', 20), width= 50, height= 25).pack()

Label(tab2, text='I am Tab 2', font=('Arial', 20), width= 50, height= 25).pack()





window.mainloop()