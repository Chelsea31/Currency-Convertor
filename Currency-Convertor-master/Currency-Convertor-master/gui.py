from tkinter import *
from tkinter.ttk import *
import feedparser

class currConv:
    def __init__(self,mast):
        str="(▀̿Ĺ̯▀̿ ̿)"
        #element init
        note=Notebook(mast)
        master=Frame(note)
        tab2=Notebook(note)
        note.add(master,text="Currency convert")
        note.add(tab2,text="News Feed")
        link = "https://www.reddit.com/r/CURRENCY/.rss"  # rss link
        d = feedparser.parse(link)
        text = Text(tab2,font=("Georgia", "10"))
        text.insert(INSERT,'NEWS\n\n')
        text.pack()
        for post in d.entries:
            to_print = post.title + " " + post.link
            text.insert('end',to_print + "\n\n",)
            text.pack()
        text.tag_add("here", "1.0",'end')
        #setting the text color in tab2
        text.tag_config("here", foreground="blue")  
        head=Label(master,text="Currency Convertor",font=("palatino", 30))
        inputField=Entry(master,width=30,font=("garamond",20))
        options = ["US $","UK £","EUR €","IND ₹","JAP ¥"]
        var1=StringVar(master)
        var1.set("From")
        list1=OptionMenu(master,var1,*options)
        list1.config(width=10)
        var2=StringVar(master)
        var2.set("To")
        list2=OptionMenu(master,var2,*options)
        list2.config(width=10)
        but=Button(master,text="convert")
        result=Label(master,text=str,font=("garamond",20))
        #grid declarations
        note.grid()
        head.grid(row=0,columnspan=2,padx=15,pady=15)
        inputField.grid(row=1,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
        list1.grid(row=2,columnspan=1,sticky=N+S+W,padx=70,pady=10)
        list2.grid(row=2,column=1,columnspan=1,sticky=N+S+E,padx=70,pady=10)
        but.grid(row=3,columnspan=2,padx=20,pady=20)
        result.grid(row=4,columnspan=2,padx=20,pady=20)

root =Tk()
#root.columnconfigure(0,weight=1)
#root.rowconfigure(0,weight=1)
root.resizable(0,0)
x = currConv(root)
root.mainloop()
