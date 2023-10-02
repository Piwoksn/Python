from tkinter import *
from tkinter import filedialog

def saveFile():
    file= filedialog.asksaveasfile(
    #defaultextension = ".txt",
    filetypes= [
    ('Text file', '.txt'),
    ('Html file', '.html'),
    ('All file', '.*')
    ]
    )
    
    if file is None:#to prevent error
        return
    #create a file to save
    filetext = str(text.get(1.0, END))#text to save
    file.write(filetext)#write text into file
    file.close()#close file


window = Tk()


button = Button(window,
text= 'save',
command= saveFile
)
button.pack()

text= Text(window)
text.pack()



window.mainloop()