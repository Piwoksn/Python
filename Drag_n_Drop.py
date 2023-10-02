from tkinter import *
window = Tk()

#function
def drag_start(event):
    label.startX = event.x
    label.startY = event.y
    
def drag_motion(event):
    x = label.winfo_x() - label.startX + event.x
    y = label.winfo_y() - label.startY + event.y
    label.place(x=x, y=y)


#label
label = Label(window, width= 5, height= 5, bg= 'red')
label.place(x=0, y=0)

#bind
label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)



window.mainloop()