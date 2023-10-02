from tkinter import *

window = Tk()
window.config(padx= 50)
window.config(pady = 50)

entry = Entry(window,
font = ('Arial', 15),
fg = 'red'


)
entry.pack()

#entry.pack(anchor= W) #positions the label using east north west n south

#entry.pack(side = LEFT) #positions the label using right left top or bottom

#entry.place(x= 0, y = 0)# positionning too




window.mainloop()