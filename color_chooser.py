from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    setcolor = color[1]
    window.config(bg= setcolor)
    #or written in oneline of code
    #window.config(bg= colorchooser.askcolor()[1])


window = Tk()
window.geometry('420x420')


button = Button(window,
text='Choose color',
command = click,
)
button.pack()




window.mainloop()