from tkinter import *
import time

master=Tk()
master.geometry('600x200+350+350')
master.title('DIGITAL CLOCK')

timenow= ' '
cframe=Frame(master,width=200,height=100,bg='black',relief=GROOVE)
cframe.pack()

clock=Label(cframe,padx=25,pady=40,bd=3,fg='white',font=('arial',48,'bold'),text=timenow,bg='black',relief=SUNKEN)
clock.pack()

def tick():
    global timenow
    newtime=time.strftime(' %H: %M: %S %p')
    if newtime!= timenow:
        timenow=newtime
        clock.config(text=timenow)
    clock.after(200,tick)    



tick()
master.mainloop()    