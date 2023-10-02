from tkinter import *
#function
def submit():
    variable = entry.get()
    label.config(text = variable)


#window
window = Tk()
window.config(padx= 50)
window.config(pady = 50)

#entry
entry = Entry(window,
font = ('Arial', 15),
fg = 'red'


)
entry.pack()

#entry.pack(anchor= W) #positions the label using east north west n south

#entry.pack(side = LEFT) #positions the label using right left top or bottom

#entry.place(x= 0, y = 0)# positionning too

#----------------------

#submit button
submitbutton = Button(window,
text = 'submit',
font = ('Comic Sans', 15),
bg = 'lightgreen',
command = submit,#button function
activeforeground= 'black',# text too
activebackground = 'lightgreen'#prevents the background from changing color when pressed

)
submitbutton.pack()


#Label
label = Label(window,
text = "",
font = ("Arial", 13),
bg = 'yellow'
)
label.pack()

window.mainloop()