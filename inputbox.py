import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200") # sets size of window
        self.main_window.title("InputBox Demo") # names window

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)
        #self.[name] - thats us naming the attrubute so top and bottom frame are things we made

        self.prompt_label = tkinter.Label(self.topframe,text="Please enter the distance in kilometers") # creates label
        self.kilo_entry = tkinter.Entry(self.topframe,width=10) # creates input box with width of 10 pixels
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.topframe.pack()
        self.bottomframe.pack()

        self.calc_button = tkinter.Button(self.main_window,text="Convert",command=self.convert)
        self.quitbutton = tkinter.Button(self.main_window,text="Quit",command=self.main_window.destroy) # destroy closes method for us

        self.calc_button.pack(side="left")
        self.quitbutton.pack(side="right")    
 
        tkinter.mainloop()

    def convert(self):

        kilo = float(self.kilo_entry.get()) # built in accessor method
        miles = round(kilo * 0.6214,2) # rounds to two decimal places
        tkinter.messagebox.showinfo("Results",str(kilo) + " kilometeres is equal to " + str(miles) + " miles")

myGUI = MyGUI() # allows window to be active on your screen until you close it

print("Hi there!") # won't print until the loop above ends (but it won't so you have to end it)