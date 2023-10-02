from tkinter import *

#functions
def order():
    item = food[x.get()]
    label1.config(text = 'Your order: ')
    label.config(text = item)



#window
window = Tk()
window.config(padx = 50)
window.config(pady = 50)
#window.config(bg = 'lightblue')

#radio
food = ['Pizza', 'Burger', 'Samosa', 'Meat Pie']

count = 0
x = IntVar()

for item in food:
    radio = Radiobutton(window,
    text = food[count],
    variable = x,
    value = count,
    indicator = 0,
    width = 20
    )
    radio.pack(anchor = 'w')
    radio.size()
    count +=1


#submit
submit = Button(window,
text = 'order',
command = order,

)
submit.pack(anchor = 'e')


#label

label1 = Label(window,
text = "",

)
label1.pack()




label = Label(window,
text = "",

)
label.pack()



window.mainloop()