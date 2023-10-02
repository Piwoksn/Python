from tkinter import *

def play():
    for i in range(11):
        print(i)


window = Tk()
window.title("Nobles")
window.geometry("420x420")
icon = PhotoImage(file='')
window.iconphoto(True, icon)
window.config(background="skyblue")

#photo = PhotoImage(file='Pictures\\pin.jpg')

label = Label(window, text='Hello World',
 font = ('Times New Roman', 25, 'bold'), 
 fg = '#00FF00', 
 bg = 'black',
 relief= RAISED,
 bd = 10,
 #image= photo
 )
label.pack()

count = 0
def click():
    global count
    print('Clicked button', count)
    count+=1

button = Button(window,
text='click me',
command= click,
font=('Comic Sans', 10),
fg='#00FF00',
bg='darkred',
activeforeground='#00FF00',
activebackground='darkred',
)

button.pack()


window.mainloop()