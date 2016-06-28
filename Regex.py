from tkinter import *
import re

fontt=("Helvetica", 24)
elenr = 0
entrywidth = 80
defaultcount = 5
class GUI(Tk):
    
    def delete(self,i):
        self.buttondelete[i].grid_forget()
        self.entry[i].grid_forget()
        self.sq[i].grid_forget()

    def sqf(self,x):
        self.sql = Frame(self.topBar, bg="red")
        self.sql.grid(row=0, column=x, sticky='news')

    
    
    def call(self):
        global elenr
        ewidth = entrywidth
        if entrywidth != 80 :
            ewidth = entrywidth - 10  
        e = Text (self.topBar , width=ewidth, height=2, bd=2)
        e.grid(column=1, row =elenr+3)
        button = Button(self.topBar,text="remove", command=lambda i=elenr: self.delete(i))
        button.grid(column=2, row =elenr+3)
        lbl= Label(self.topBar, text="empty",bg="orange" , font=fontt)
        lbl.grid(column=0, row =elenr+3)
        self.entry[elenr]=e
        self.buttondelete[elenr]=button
        self.sq[elenr]=lbl
        elenr+=1
        
        #print(self.entry)
    def __init__(self):
        self.tk = Tk()
        self.timespend = 0
        self.tk.wm_title("Web Service")
        self.tk.configure(background='white')
        self.tk.wm_state('zoomed')
        #self.tk.attributes("-fullscreen",True)
        #Frames
        

        x=5
        self.wd=self.tk.winfo_width()
        self.topFrame = Frame(self.tk, bg="white", borderwidth=5)
        #self.topFrame.resizable(width=False, height=False)
        self.topFrame.grid(row=0, column=1, sticky='news', padx = ( self.wd/2, self.wd/2))
        self.topFrame.columnconfigure(0, weight=1)
        self.topFrame.grid_columnconfigure(0, weight=1)
        
        self.title = Frame(self.topFrame, bg="white" )
        self.title.grid (row = 0, pady= (0,50))
        self.titlelbl= Label(self.title, text="Regex Tester",bg="white", font=("Helvetica", 24))
        self.titlelbl.grid()

        self.textfield = Text(self.topFrame, width=100, height=2, bd=2)
        self.textfield.grid(row = 1,pady=5,sticky="e",columnspan=3)
        

        
        #self.topFrame.grid(sticky=(N, S, E, W))
        self.sq = {}

        self.button = Button(self.topFrame,text="add field", command = self.call)
        self.button.grid(column=0, row = 2)
        
        self.button2 = Button(self.topFrame,text="Expand", command = self.expand)
        self.button2.grid(column=1, row = 2, pady=5)
        self.button3 = Button(self.topFrame,text="Reduce", command = self.reduce)
        self.button3.grid(column=2, row = 2, pady=5)
        
        

        
        
        #self.topBar.config(background='blue')
        
        
        self.topBar = Frame(self.topFrame, border=2,  bg="white",  relief=RIDGE )
        self.topBar.grid(row=3, column=0, columnspan=3,sticky=W+E)
        self.topBar.columnconfigure(0, weight=1)
        self.entry = {}
        self.buttondelete = {}
        self.tk.after(0, self.task)
        #self.topFrame.pack(side=TOP, expand=True)
        #self.circle = Canvas(self.botFrame, width=50, height=50 , bg="white", borderwidth=0)
        #self.circle.pack()
	#Funcion which creates and updates frame

    def task(self):
        global defaultcount
        self.wd=self.tk.winfo_width()
        self.tf=self.topFrame.winfo_width()
        self.wd=self.wd - self.tf
        self.topFrame.grid(row=0, column=1, sticky='news', padx = ( self.wd/2, self.wd/2), pady = (40,100))
        if defaultcount != 0:
            while defaultcount !=0 :
                self.call()
                defaultcount -=1
        self.retrieve_input()       # auto update
        self.tk.after(1, self.task)#Program refresh main window 
    def retrieve_input(self):
        dict = {}
        string = ""
        w=self.textfield.get("1.0",END)

        if len(w) != 1:
            try :
                for ele in self.entry:
                    
                    value = self.entry[ele].get("1.0",END)

                    dict[ele]=value
                
                for ele in w:
                    string += ele


                p = re.compile(r''+ string.rstrip('\n')) ;

                for elem in dict:

                    if p.match(str(dict[elem])):

                        self.sq[elem].grid_forget()
                        self.sq[elem]= Label(self.topBar, text="True",bg="green" , font=fontt)
                        self.sq[elem].grid(column=0, row =elem+3)
                        
                    elif len(dict[elem]) ==0:
                        self.sq[elem].grid_forget()
                        self.sq[elem]= Label(self.topBar, text="empty",bg="orange" , font=fontt)
                        self.sq[elem].grid(column=0, row =elem+3)
                        

                    else:

                        self.sq[elem].grid_forget()
                        self.sq[elem]= Label(self.topBar, text="False",bg="red" , font=fontt)
                        self.sq[elem].grid(column=0, row =elem+3)
            except:
                print("fail")
    def expand(self):
        global entrywidth
        temp = {}
        for ele in self.entry:
            temp[ele]= self.entry[ele].get("1.0",END)

            self.entry[ele].grid_forget()
            
        self.entry = {}

        for elem in temp:
            e = Text (self.topBar , width=entrywidth, height=2, bd=2)

            e.insert(INSERT, temp[elem])
            e.grid(column=1, row =elem+3)
            self.entry[elem]=e
        entrywidth += 10
    def reduce(self):
        global entrywidth
        temp = {}
        for ele in self.entry:
            temp[ele]= self.entry[ele].get("1.0",END)

            self.entry[ele].grid_forget()
            
        self.entry = {}

        for elem in temp:
            e = Text (self.topBar , width=entrywidth, height=2, bd=2)

            e.insert(INSERT, temp[elem])
            e.grid(column=1, row =elem+3)
            self.entry[elem]=e
        entrywidth -= 10
    #def regextest(self,test)
        
            
        

	
#forever loop
Gui= GUI()
Gui.mainloop()

