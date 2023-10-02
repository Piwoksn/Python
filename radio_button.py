from tkinter import *

#functions


#window
window = Tk()
window.config(padx= 50)
window.config(pady= 50)


#Radio button with indicator
snack = ["Meat Pie", "Pizza", "Burger", "Egg Roll", "Puff Puff"]

num = 0
x = IntVar()

for index in snack:
    
    radio = Radiobutton(window,
    text = snack[num],
    variable = x,
    value = num,
    )
    num+=1
    
    radio.pack(anchor = 'w')


#radio button with no indicators
snack2 = ["Meat Pie", "Pizza", "Burger", "Egg Roll", "Puff Puff"]

nums = 0
y = IntVar()

for index in snack:
    
    radio2 = Radiobutton(window,
    text = snack2[nums],
    variable = y,
    value = nums,
    indicator = 0,
    width = 20,
    )
    nums+=1
    
    #radio2.pack(anchor = 'w')
    radio2.pack(side = LEFT)









window.mainloop()