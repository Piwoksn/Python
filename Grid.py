from tkinter import *


window = Tk()


firstname= Label(window,
text='Firstname'
).grid(row=0, column=0)

firstnameEntry= Entry(window,).grid(row= 0, column= 1)

email= Label(window,
text='Email'
).grid(row=1, column=0)

emailEntry= Entry(window,).grid(row= 1, column= 1)

password= Label(window,
text='Password'
).grid(row=2, column=0)

passwordEntry= Entry(window, show= '*').grid(row= 2, column= 1)

Button(window, text='submit').grid(row=3, column= 0, columnspan= 2)





window.mainloop()