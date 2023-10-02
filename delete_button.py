from tkinter import *
#function
def delete():
    entry.delete(0, END)


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

#delete button
deletebutton = Button(window,
text = 'delete',
font = ('Comic Sans', 15),
bg = 'red',
command = delete,#button function
activeforeground= 'black',# text too
activebackground = 'lightgreen'#prevents the background from changing color when pressed

)

deletebutton.pack()




window.mainloop()
