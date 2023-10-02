from tkinter import *
#func
def dosomething(event):
    print('You did something at', event.x, ' ', event.y)
    
window = Tk()

window.bind('<Button-1>', dosomething)#left mouse click

window.bind('<Button-2>', dosomething)#Scroll mouse click

window.bind('<Button-3>', dosomething)#right mouse click

window.bind('<ButtonReleased>', dosomething)#when you release the clicked button

window.bind('<Enter>', dosomething)#gives cordinate When you enter working area

window.bind('<Leave>', dosomething)#gives cordinate when you leave working area

window.bind('<Motion>', dosomething)#gives cordinate when you move around working area






window.mainloop()