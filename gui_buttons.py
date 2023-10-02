from tkinter import *




#Functions
def submit():
    email = entry1.get()
    password = entry2.get()
    print('Logged in as', email, 'your password is', password)
    


def backspace():
    if entry1.get():
        entry1.delete(len(entry1.get()) -1, END)
    elif entry2.get():
        entry2.delete(len(entry2.get()) -1, END)
    
    


def delete():
    entry1.delete(0, END)
    entry2.delete(0, END)


def showp():
    entry2.config(show = '')


def hide():
    entry2.config(show='*')
    
    

def checkit():
    if (x.get() == 1):
        entry2.config(show='')
    else:
        entry2.config(show='*')








#Window
window = Tk()
window.config(background='lightblue')

#variable
x = IntVar()


#Label
label = Label(window,
text = 'Login',
font = ('Arial', 15, 'bold'),
bg = 'lightblue'
)
label.pack()

#entry
entry1 = Entry(window,
placeholder = 'Email',
font = ('Times New Roman', 15)
)
entry1.pack()

entry2 = Entry(window,
placeholder = 'Password',
font = ('Times New Roman', 15),
show = "*"
)
#entry2.insert(0, 'Pass')
entry2.pack()


#buttons
submit = Button(window,
text= 'Sign in',
command=submit,
bg= 'green',
fg= 'white'
)
submit.pack()

#backspace button
backspace_b = Button(window,
text= 'Backspace',
command=backspace,
bg= 'orange',
fg= 'white'
)
backspace_b.pack()

#delete button
delete_b = Button(window,
text= 'Delete',
command=delete,
bg= 'red',
fg= 'white'
)
delete_b.pack()

#show button
show = Button(window,
text='Show Password',
bg = 'white',
fg = 'blue',
command = showp
)
show.pack()

#hide button
hiden = Button(window,
text = 'Hide Password',
bg= 'white',
fg= 'red',
command= hide,
)
hiden.pack()

#checkbutton
checker = Checkbutton(window,
text= 'Show Password',
variable= x,
onvalue=1,
offvalue=0,
command= checkit
)
checker.pack()



#Radio button

food = ["Pizza", "Meat Pie", "Egg Roll"]
y = IntVar()

for index in range(len(food)):
    radio = Radiobutton(window,
    text = food[index],
    variable = y,
    value = index,
    padx = 5,
    pady = 5,
    bg= "lightblue",
    indicator = 0,
    width = 100
    )
    radio.pack(anchor = W)


#Scale


scale = Scale(window,
from_ = 100,
to = 0,
width= 30,
length = 300,
tickinterval = 10,
resolution = 5,
troughcolor = 'blue',
bg = 'black',
fg = 'white',
showvalue = 0,
orient= HORIZONTAL,
)
scale.pack()


#List Box
list_box = Listbox(window,
width = 30,

)
list_box.pack()

list_box.insert(1, 'Pizza')
list_box.insert(2, 'Salad')
list_box.insert(3, 'Burger')
list_box.insert(4, 'Shrimps')
list_box.insert(5, 'Sandwich')

list_box.config(height = list_box.size())

window.mainloop()