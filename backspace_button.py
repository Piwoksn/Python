from tkinter import *
#function
def backspace():
    entry.delete(len(entry.get()) - 1, END)


#window
window = Tk()
window.config(padx= 50)
window.config(pady = 50)

#entry
entry = Entry(window,
font = ('Arial', 15),
fg = 'blue'


)
entry.pack()

#entry.pack(anchor= W) #positions the label using east north west n south

#entry.pack(side = LEFT) #positions the label using right left top or bottom

#entry.place(x= 0, y = 0)# positionning too

#----------------------

#backspace button
backspacebutton = Button(window,
text = 'backspace',
font = ('Comic Sans', 15),
bg = 'yellow',
command = backspace,#button function
activeforeground= 'black',# text too
activebackground = 'lightgreen'#prevents the background from changing color when pressed

)

backspacebutton.pack()




window.mainloop()
