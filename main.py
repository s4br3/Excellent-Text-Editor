from tkinter import *
from tkinter import ttk
import input as inp
import file as f

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


fileMenu.add_command(
    label = 'Save',
    command = dummy
)

menuBar.add_cascade(
    label = 'File',
    menu=fileMenu
)

textbox = Text(root,width=16,height=5)
textbox.pack(side=LEFT,fill=BOTH,expand=YES)
textbox.bind('<Key>',inp.read_input)

root.mainloop()
