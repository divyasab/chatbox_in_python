# from subprocess import 
 
from tkinter import *
root = Tk()
def send():
    send="You :"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hello "):
        txt.insert(END,"\n"+"divya: hii ")
    elif (e.get()=="hii"):
        txt.insert(END,"\n"+"divya: How can i help you ?")
    elif (e.get()=="May I know the special menu of today"):
        txt.insert(END,"\n"+"divya: Non Veg OR Veg")
    elif (e.get()=="non veg"):
        txt.insert(END,"\n"+"divya : chicken biryani, mutton biryani")
    elif (e.get()=="please place order of chicken biryani"):
        txt.insert(END,"\n"+"divya: ok ma'am.... thank you for visiting")    
    else:
        txt.insert(END,"\n"+"divya: sorry i didn't get it ")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=50)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()