from tkinter import *
from tkinter.ttk import *
import feedparser
import requests

class currConv:
    def convertCurr(self,event):
        toConvert = self.inputField.get()
        try:
            x=float(toConvert)
            if x <= 0:
                raise ValueError
                # API Request
            response = requests.get(url="https://goo.gl/PbAhsZ")

            # converts the response
            jsonResponse = response.json()

            # fetches list of currency
            priceList = jsonResponse["quotes"]

            # fetches User Input
            currency = self.var2.get()

            # UseCases
            if(currency[0]=='E'):
                value = priceList["USDEUR"]

            if(currency[0]=='I'):
                value = priceList["USDINR"]

            if(currency[0]=='J'):
                value = priceList["USDJPY"]

            # Output
            strVal.set(str(float(toConvert) * value))
                

        except ValueError:
            strVal.set("Enter a number and try again")


    def __init__(self,master):

        #element init
        note=Notebook(master)
        tab1 = Frame(note)
        tab2 = Frame(note)
        note.add(tab1,text="Currency convert")
        note.add(tab2,text="News Feed")

        #First tab
        head=Label(tab1,text="Currency Convertor",font=("palatino", 30))
        self.inputField=Entry(tab1,width=30,font=("garamond",20))
        options = ["","EUR €","IND ₹","JAP ¥"]
        self.var1=StringVar(tab1)
        self.var1.set("US $")
        list1=OptionMenu(tab1,self.var1)
        list1.config(width=10)
        self.var2=StringVar(tab1)
        self.var2.set("IND ₹")
        list2=OptionMenu(tab1,self.var2,*options)
        list2.config(width=10)
        but=Button(tab1,text="convert")
        but.bind("<Button-1>",self.convertCurr)
        result=Label(tab1,textvariable=strVal,font=("garamond",20))
        strVal.set("(▀̿Ĺ̯▀̿ ̿)")

        #Second tab
        link = "https://www.reddit.com/r/CURRENCY/.rss"  # rss link
        d = feedparser.parse(link)
        text = Text(tab2,font=("Georgia", "10"))
        scroll = Scrollbar(tab2,command = text.yview)
        text.insert(INSERT,'NEWS\n\n')
        for post in d.entries:
            to_print = post.title + "\nLINK :  " + post.link
            text.insert('end',to_print + "\n\n",)
            text.grid()
        text.tag_add("here", "1.0",'end')
        #setting the text color in tab2
        text.tag_config("here", foreground="blue")

        #grid declarations
        note.grid()
        head.grid(row=0,columnspan=2,padx=15,pady=15)
        self.inputField.grid(row=1,columnspan=2,sticky=N+S+E+W,padx=5,pady=5)
        list1.grid(row=2,columnspan=1,sticky=N+S+W,padx=70,pady=10)
        list2.grid(row=2,column=1,columnspan=1,sticky=N+S+E,padx=70,pady=10)
        but.grid(row=3,columnspan=2,padx=20,pady=20)
        result.grid(row=4,columnspan=2,padx=20,pady=20)
        scroll.grid(row=0, column=1, sticky='nsew')
        text['yscrollcommand'] = scroll.set
        text.grid()

root =Tk()
strVal= StringVar()
root.resizable(0,0)
x = currConv(root)
root.mainloop()