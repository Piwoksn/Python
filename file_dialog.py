from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(
    title= 'My Files',
    filetypes= (('text files', '*.txt'), ('all files', '*.*'))
    )
    file = open(filepath, 'r')
    print(file.read())
    file.close()


window = Tk()
window.geometry('50x50')

button= Button(window,
text= 'open file',
command= openfile
)
button.pack()




window.mainloop()