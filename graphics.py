from tkinter import *
from tkinter import ttk

def dummy():
    return

root = Tk()
root.title('New File')
root.geometry('960x600')

menuBar = Menu(root)
root.config(menu=menuBar)

fileMenu = Menu(menuBar)
fileMenu.add_command(
    label='Open',
    command=dummy
)

menuBar.add_cascade(
    label='File',
    menu=fileMenu,
    underline=0
)

textbox = Text(root,width=16,height=5)
textbox.pack(side=LEFT,fill=BOTH,expand=YES)

root.mainloop()
