from tkinter import *
from tkinter.ttk import *
import time


#function
def start():
    task= 10
    x= 0
    while (x < task):
        time.sleep(1)
        bar['value']+=10
        x+=1
        percent.set(str(int((x/task)*100))+ "%")
        tasks.set(f'{x}/{task} completed')
        window.update_idletasks()#shows progress by 10% every 1 second
    
    
window = Tk()

#Variables
percent = StringVar()
tasks = StringVar()


#Progress Bar
bar = Progressbar(window, orient= HORIZONTAL,
length= 300)#default length is 100
bar.pack(pady= 10)

#labels
percentlabel = Label(window,
textvariable= percent)#text variable enables us to update text fixed in a function
percentlabel.pack()


tasklabel= Label(window, textvariable= tasks).pack()



#Button
button= Button(window, text="download", command= start)
button.pack()



window.mainloop()