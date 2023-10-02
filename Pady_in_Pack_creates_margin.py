from tkinter import *


def add():
    message = entry.get()
    list.insert(len(list.get(0, END)), message)
    
    list.config(height= list.size())
    entry.delete(0, END)


def buy():
    food = []
    for index in list.curselection():
        food.append(list.get(index))
        
    print('Your Order:')
    for i in food:
        print(i)


def delett():
    for index in reversed(list.curselection()):
        list.delete(index)
        list.config(height= list.size())


def bs():
    entry.delete(len(entry.get()) -1)


window = Tk()
window.config(padx= 50)
window.config(pady= 50)


list= Listbox(window,
font= ('Arial', 15),
selectmode = MULTIPLE,
)
list.insert(1, 'Apple')
list.insert(2, 'Banana')
list.insert(3, 'Pear')


list.pack(pady=10)
list.config(height= list.size())


button = Button(window,
text= 'Buy',
font= ('Arial', 13),
command = buy,
)
button.pack(pady= 10)


delete= Button(window,
text= 'Delete',
font= ('Arial', 13),
command = delett,
)
delete.pack(pady = 10)


entry = Entry(window,
font= ('Arial', 15),
)
entry.pack(pady= 10)


add = Button(window,
text= 'Add to List',
font= ('Arial', 13),
command = add,
)
add.pack(pady= 10)


bs = delete= Button(window,
text= 'Backspace',
font= ('Arial', 13),
command = bs,
)
bs.pack(pady= 10)


window.mainloop()