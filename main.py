from tkinter import *
from tkinter import ttk,filedialog
import input as inp
import file as f

def readFile():
    file = filedialog.askopenfile(parent=root,title='Open File')

    text,name = f.readFile(file)

    textbox.replace('1.0','end+1c',text)
    root.title(name)

def dummy():
    pass

def saveToFile(text):
    file = filedialog.asksaveasfilename(defaultextension="*.txt",filetypes=[("TextFiles","*.txt"),("All Files","*.*")])
    if file:
        f.writeFile(file,text)

root = Tk()
root.title('New File')
root.geometry('960x600')

menuBar = Menu(root)
root.config(menu=menuBar)

fileMenu = Menu(menuBar)
fileMenu.add_command(
    label='Open',
    command=readFile
)

menuBar.add_cascade(
    label='File',
    menu=fileMenu,
    underline=0
)


fileMenu.add_command(
    label = 'Save',
    command = lambda: saveToFile(textbox.get("1.0", "end-1c"))
)

textbox = Text(root,width=16,height=5)
textbox.pack(side=LEFT,fill=BOTH,expand=YES)
textbox.bind('<Key>',inp.read_input)

root.mainloop()
