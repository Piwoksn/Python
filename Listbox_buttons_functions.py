from tkinter import *

#function
def order():
    item = list.get(list.curselection())
    output.config(text = f'order: {item}')

def add():
    list.insert(len(list.get(0, END)), entry.get())
    list.config(height = list.size())
    
    entry.delete(0, END)
 
 
def delete():
 list.delete(list.curselection())
 list.config(height = list.size())
 
 
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
#list.config(selectmode= MULTIPLE)


#purchase
purchase = Button(window,
text = 'buy',
font = ('Comic Sans', 10),
bg = 'lightblue',
command = order,

)
purchase.pack()


#label
output = Label(window,
font = ('Times New Roman', 10),
text = ''
)
output.pack()

#entry
entry = Entry(window,
font = ('Times New Roman', 20),
width= 50,

)
entry.pack()



#Add button
button = Button(window,
text= 'add',
font = ('Comic Sans', 10),
command = add
)
button.pack(anchor = 'w')


button = Button(window,
text = 'delete',
font = ('Comic Sans', 10),
command = delete,

)
button.pack(anchor = 'w')


window.mainloop()