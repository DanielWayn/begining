from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="1",  fg='black', bg='red', command=lambda: print("1"), height=1, width=7)
button2 = Button(topFrame, text="2",  fg='black', bg='red', command=lambda: print("2"), height=1, width=7)
button3 = Button(topFrame, text="3",  fg='black', bg='red', command=lambda: print("3"), height=1, width=7)
button4 = Button(bottomFrame, text="4",  fg='black', bg='red', command=lambda: print("4"), height=1, width=7)
button5 = Button(bottomFrame, text="5",  fg='black', bg='red', command=lambda: print("5"), height=1, width=7)
button6 = Button(bottomFrame, text="6",  fg='black', bg='red', command=lambda: print("6"), height=1, width=7)
button7 = Button(bottomFrame, text="7", fg='black', bg='red', command=lambda: print("7"), height=1, width=7)
button8 = Button(bottomFrame, text="8", fg='black', bg='red', command=lambda: print("8"), height=1, width=7)
button9 = Button(bottomFrame,  text=' 9 ', fg='black', bg='red', command=lambda: print("9"), height=1, width=7)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()

root.mainloop()
