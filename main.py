from tkinter import *
from tkinter import ttk,filedialog
import input as inp
import file as f

def readFile():
    file = filedialog.askopenfile(parent=root,title='Open File')
    if not file: return

    text,nName = f.readFile(file)

    if not text:
        textbox.delete('1.0','end+1c')

    textbox.replace('1.0','end+1c',text)
    root.title(nName)
    global name
    name = nName

def dummy():
    pass

def saveToFile(text):
    file = filedialog.asksaveasfile(defaultextension="*.txt",filetypes=[("TextFiles","*.txt"),("All Files","*.*")])
    if file:
        f.writeFile(file,text)

def renderTitle():
    root.title(f'{name}{" *" if delta else ""}')
    root.after(1000,renderTitle)

    #f.writeFile("filename",text)

delta = False
name = 'New File'

root = Tk()
root.title(name)
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

renderTitle()
root.mainloop()
