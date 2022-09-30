import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200") # sets size of window
        self.main_window.title("Label Demo") # names window

        self.Label1 = tkinter.Label(self.main_window,text="Hello World") # puts text in window
        self.Label2 = tkinter.Label(self.main_window,text="This is my GUI program") # puts text in window

        self.Label1.pack()
        self.Label2.pack()

        tkinter.mainloop()

myGUI = MyGUI() # allows window to be active on your screen until you close it

print("Hi there!") # won't print until the loop above ends (but it won't so you have to end it)