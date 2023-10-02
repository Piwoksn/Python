from tkinter import *

window = Tk()

#Create menu bar
menubar = Menu(window, bg= 'light blue')
window.config(menu= menubar)#Assign it to the window

fileMenu= Menu(menubar, tearoff= 0, bg= 'white', font=('Times New Roman', 15))#created first menu
menubar.add_cascade(label='File',
menu= fileMenu
)#Creates a dropdown

#lets asd menus to our cascade
fileMenu.add_command(label='Open'
#command= open
)
fileMenu.add_command(label='Save',
#command= save
)
fileMenu.add_separator()#adds a seperator
fileMenu.add_command(label='Exit', 
command= quit)



#second Menu (Edit Menu)
editmenu = Menu(menubar, tearoff= 0, bg='light yellow', font=('Times New Roman', 15))
menubar.add_cascade(label='Edit',
menu=editmenu)

editmenu.add_command(label='Cut',
#command= cut
)
editmenu.add_command(label='Copy',
#command= copy
)
editmenu.add_command(label='Paste',
#command=paste
)


window.mainloop()