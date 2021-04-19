import tkinter

def GetWindowPos():
    global X,Y
    X = win.winfo_geometry().split("+")[1]
    Y = win.winfo_geometry().split("+")[2]
    win.bind_all('<Configure>', HoldOn)

def HoldOn(event):
    win.geometry("+{}+{}".format(X,Y))

win = tkinter.Tk()
win.geometry("400x400+{}+{}".format(12,12))
tkinter.Label(win,text="Halo!").grid()
win.after(100,GetWindowPos)

win.mainloop()
