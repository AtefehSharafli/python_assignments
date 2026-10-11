from tkinter import *
from my_tools import *

window = Tk()
window.title("profile")
window.geometry("500x500")


Label(window, text="mobile number").place(x=20, y=20)
mobile  = StringVar()
Entry(window, textvariable=mobile).place(x=120, y=20)

Label(window, text="national id").place(x=20, y=60)
national = StringVar()
Entry(window, textvariable=national).place(x=120, y=60)

Label(window, text="card number").place(x=20, y=100)
card = StringVar()
Entry(window, textvariable=card).place(x=120, y=100)

Label(window, text="car plate").place(x=20, y=140)
plate = StringVar()
Entry(window, textvariable=plate).place(x=120, y=140)

Label(window, text="bill id").place(x=20, y=180)
bill = StringVar()
Entry(window, textvariable=bill).place(x=120, y=180)


Button(window,text="Save").place(x=200, y=250, width=100)

window.mainloop()