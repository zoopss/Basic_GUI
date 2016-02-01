from Tkinter import *
root = Tk()
root.geometry('460x600')
root.title('Python GUI')
top = Frame(root , width = 100 , height = 200)
a = Button(top , text = "HELLO!!!")
a.pack()
top.pack()
bottom = Frame(root)
bottom.pack()
b= Button(bottom, text = "How Are you??")
b.pack()


root.mainloop()

