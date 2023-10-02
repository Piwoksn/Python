from tkinter import *

def send():
    message = text.get('1.0', END)
    print(message)

window = Tk()
#window.config(padx= 50)
#window.config(pady = 50)

text = Text(window,
bg= 'light yellow',
font = ('Ink Free', 25),
padx= 50,
pady= 50,
height= 8,
width= 24,
fg= 'purple'
)
text.pack()

button= Button(window,
text = 'Submit',
command = send
)
button.pack()


window.mainloop()