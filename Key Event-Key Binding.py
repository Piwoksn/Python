from tkinter import *
#function
def dosomething(event):
    label.config(text = event.keysym)

window = Tk()

#WORKS ON SYSTEM

label = Label(window, font=('Arial', 100))
label.pack()


window.bind("<Return>", dosomething)




window.mainloop()