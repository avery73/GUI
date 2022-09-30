import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200") # sets size of window
        self.main_window.title("Label Demo") # names window

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)
        #self.[name] - thats us naming the attrubute so top and bottom frame are things we made

        self.Label1 = tkinter.Label(self.topframe,text="John") # puts text in window
        self.Label2 = tkinter.Label(self.topframe,text="Jim") # puts text in window
        self.Label3 = tkinter.Label(self.topframe,text="Jerry") # puts these three names on the top line

        self.Label1.pack(side="left") # specifies the side it goes on, this gets packed frist
        self.Label2.pack(side="left") # every element on the window needs to be packed, packed second so right below
        self.Label3.pack(side="left") # packed third so below the second

        self.Label4 = tkinter.Label(self.bottomframe,text="Jill") # puts text in window
        self.Label5 = tkinter.Label(self.bottomframe,text="Janie") # puts text in window
        self.Label6 = tkinter.Label(self.bottomframe,text="Jen") # puts these three names on the bottom line

        self.Label4.pack(side="left")
        self.Label5.pack(side="left")
        self.Label6.pack(side="left")

        self.topframe.pack()
        self.bottomframe.pack()

        self.mybutton = tkinter.Button(self.main_window,text="Click Me!",command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window,text="Quit",command=self.main_window.destroy) # destroy closes method for us

        self.mybutton.pack(side="left")
        self.quitbutton.pack(side="right")    
 
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Response","Thanks for clicking me!")

myGUI = MyGUI() # allows window to be active on your screen until you close it

print("Hi there!") # won't print until the loop above ends (but it won't so you have to end it)