from tkinter import *

window = Tk()

label = Label(window,
text = 'Welcome',
font = ('Times New Roman', 30, 'bold'),
fg = 'white',
bg = 'black',
relief = RAISED,#border type
bd = 10,#border width
)
label.pack()
#label.pack(anchor= W) #positions the label using east north west n south

#label.pack(side = LEFT) #positions the label using right left top or bottom

#label.place(x= 0, y = 0)# positionning too


window.mainloop()