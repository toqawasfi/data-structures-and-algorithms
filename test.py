import tkinter

root = tkinter.Tk()
frm = tkinter.Frame(root)
frm.grid()
tkinter.Label(frm, text="Hello World!").grid(column=0, row=0)
tkinter.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
root.mainloop()