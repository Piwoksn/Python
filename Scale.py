from tkinter import *

#function
def check():
    value = scale.get()    
    
    label.config(text = f'{value} deg. celsius')



def add():
    scale.set(scale.get() +5)
    
    value = scale.get()
    if value >= 25 and value <= 49:
        scale.config(troughcolor = 'blue')
        
    elif value >= 50 and value <= 69:
        scale.config(troughcolor = 'orange')
        
    elif value >= 70 and value <= 100:
        scale.config(troughcolor = 'red')
    else:
        scale.config(troughcolor = 'lightblue')
    


def minus():
    scale.set(scale.get() -5)
    
    value = scale.get()
    if value >= 25 and value <= 49:
        scale.config(troughcolor = 'blue')
        
    elif value >= 50 and value <= 69:
        scale.config(troughcolor = 'orange')
        
    elif value >= 70 and value <= 100:
        scale.config(troughcolor = 'red')
    else:
        scale.config(troughcolor = 'lightblue')
    



#window
window = Tk()
window.config(padx =50)
window.config(pady =50)



#add button
addb = Button(window,
text = '+',
font = ('Comic Sans', 15, 'bold'),
command = add,

)
addb.pack()


#scale

scale = Scale(window,
from_ = 100,
to = 0,
width = 50,
length = 500,
tickinterval = 10,
resolution = 5,
troughcolor = 'lightblue',
#orient = HORIZONTAL

)
scale.pack()


#add button
minusb = Button(window,
text = '-',
font = ('Comic Sans', 20, 'bold'),
command = minus,

)
minusb.pack()




#check button
button = Button(window,
text = 'check',
font = ('Comic Sans', 10),
command = check,

)
button.pack()

#label
label = Label(window,
text='',
font = ('Comic Sans', 15),


)
label.pack()



window.mainloop()