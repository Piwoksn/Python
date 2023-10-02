from tkinter import *

#function



#window
window = Tk()
window.config(padx= 50)
window.config(pady= 50)


#checklist
list = Listbox(window,
font = ('Comic Sans', 15),
width= 20,
)
list.pack()


list.insert(1, "Orange")
list.insert(2, "Apple")
list.insert(3, "Grape")
list.insert(4, "Cucumber")

list.config(height= list.size())









window.mainloop()