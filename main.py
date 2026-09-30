from tkinter import *
from tkinter import ttk,filedialog
from pynput import mouse
import pyautogui
import threading
import random
import input as inp
import file as f
def on_move(x, y):
    # Callback function triggered when mouse moves
    if random.random() < 0.25:
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        pyautogui.moveRel(x, y)

def readFile():
    file = filedialog.askopenfile(parent=root,title='Open File')

    text,name = f.readFile(file)

    textbox.replace('1.0','end+1c',text)
    root.title(name)

def dummy():
    pass

def saveToFile(text):
    print(text)




    #f.writeFile("filename",text)

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

listener = mouse.Listener(on_move=on_move)
listener.start()

textbox = Text(root,width=16,height=5)
textbox.pack(side=LEFT,fill=BOTH,expand=YES)
textbox.bind('<Key>',inp.read_input)

root.mainloop()
