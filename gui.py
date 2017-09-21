from tkinter import *

class currConv:
    def __init__(self,master):

        #element init
        head=Label(master,text="Currency Convertor",font=("", 30))
        inputField=Entry(master,width=50)
        options = ["US $","UK £","IND"]
        var1=StringVar(master)
        var1.set("From")
        list1=OptionMenu(master,var1,*options)
        var2=StringVar(master)
        var2.set("To")
        list2=OptionMenu(master,var2,*options)
        but=Button(master,text="Convert")
        result=Label(master,text="No Currency converted yet",font=("",20))

        #grid declarations
        head.grid(row=0,columnspan=2,padx=15,pady=15)
        inputField.grid(row=1,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
        list1.grid(row=2,columnspan=1,sticky=N+S+W,padx=70,pady=10)
        list2.grid(row=2,column=1,columnspan=1,sticky=N+S+E,padx=70,pady=10)
        but.grid(row=3,columnspan=2,padx=20,pady=20)
        result.grid(row=4,columnspan=2,padx=20,pady=20)

root =Tk()
x = currConv(root)
root.mainloop()
