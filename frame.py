from tkinter import *

window = Tk()
window.config(padx= 50)
window.config(pady= 50)
frame = Frame(window, bg='light blue', bd= 5, relief= SUNKEN)
frame.pack(side= BOTTOM)


Button(frame, text='W', font=('Ink Free', 25), width= 3).pack(side='top')
Button(frame, text='A', font=('Ink Free', 25), width= 3).pack(side='left')
Button(frame, text='S', font=('Ink Free', 25), width= 3).pack(side='left')
Button(frame, text='D', font=('Ink Free', 25), width= 3).pack(side='left')






window.mainloop()