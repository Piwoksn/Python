from tkinter import *

#function
def showp():
    
    if x.get() == 1:
        entry.config(show= '')
    elif x.get() == 0:
        entry.config(show = '*')
    else:
        pass



#window
window = Tk()
window.config(padx= 50)
window.config(pady = 50)

#variables
x = IntVar()

#entry
entry = Entry(window,
font = ('Times New Roman', 15),
show = '*',

)
entry.pack()

#Check button
check = Checkbutton(window,
text = 'Show Password',
font = ('Comic Sans', 10),
variable = x,
onvalue = 1,
offvalue = 0,
command = showp,
)
check.pack()




window.mainloop()