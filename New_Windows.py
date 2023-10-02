from tkinter import *

def new_window():
    #new_win = Toplevel()#Creates another window ontop the old. that is dependent on the old window
    
    new_win = Tk()
    
    old_window.destroy()


old_window = Tk()


Button(old_window, text= 'New Window', command= new_window).pack(side= 'bottom')



old_window.mainloop()