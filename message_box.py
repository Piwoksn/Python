from tkinter import *
from tkinter import messagebox


#functions

def info():
    messagebox.showinfo(title='Info',
    message = 'Passed'
    )
    
def warning():
    messagebox.showwarning(title='WARNING',
    message = 'Scam Alert!'
    )

def error():
    messagebox.showerror(title='ERROR',
    message='something went wrong')
    
def ask_ok_cancel():
    #messagebox.askokcancel(title='RESPONSE', message='Agree or Not')
    
    #using a conditional statement
    
    if messagebox.askokcancel(title='RESPONSE', message='Agree or Not?'):
        print('Agreed : )')
    else:
        print('Disagreed :( ')
        

def askretrycancel():
    if messagebox.askretrycancel(title='TRY AGAIN', message='Do you want to try again?'):
        print('You Retried')
    else:
        print('You canceled')
        
        
def askyesno():
    if messagebox.askyesno(title='Ask', message='I am a boy'):
        print('Yes')
    else:
        print('No')


def askquestion():
    answer = messagebox.askquestion(title= 'Question', message='Do You Know Me?')
    
    if (answer == 'yes'):
        print('He knows me')
    else:
        print("He doesn't know me")


def askyesnocancel():
    answer = messagebox.askyesnocancel(title='yes no cancel', message= 'do you like to code?')
    
    if (answer == True):
        print('You like to code')
    elif (answer == False):
        print('You do not like to code')
    else:
        print('You are not sure')
    





window = Tk()
window.config(padx= 50)
window.config(pady= 50)


button = Button(window,
text = 'info',
font = ('Arial', 15),
command = info,
)
button.pack()


button = Button(window,
text = 'warning',
font = ('Arial', 15),
command = warning,
)
button.pack()


button = Button(window,
text = 'Error',
font = ('Arial', 15),
command = error,
)
button.pack()


button = Button(window,
text = 'Response',
font = ('Arial', 15),
command = ask_ok_cancel,
)
button.pack()


button = Button(window,
text = 'Retry',
font = ('Arial', 15),
command = askretrycancel,
)
button.pack()


button = Button(window,
text = 'Reply',
font = ('Arial', 15),
command = askyesno,
)
button.pack()


button = Button(window,
text = 'Quest',
font = ('Arial', 15),
command = askquestion,
)
button.pack()


button = Button(window,
text = 'YesNoCancel',
font = ('Arial', 15),
command = askyesnocancel,
)
button.pack()




window.mainloop()