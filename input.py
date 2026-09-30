from tkinter import *
from random import randint,uniform

keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!£$%^&*()_+=-{}[]@~'#?<>;:/?"+'"'
keys = list(keys)

def read_input(event): # reads what characters are being read from the user
    textbox = event.widget
    randDouble = uniform(0,1)
    
    if event.keycode == 36 and randDouble < 0.5:
        event.widget.delete('insert-1c','insert')

    if (randDouble < 0.1):
        event.widget.delete(INSERT)
    elif (randDouble < 0.5):
        if (event.char in keys):
            newChar = map_input_to_new_char(event.char)
            event.widget.delete('insert-1c')
            event.widget.insert(INSERT,newChar)

def map_input_to_new_char(char): # takes a user character and gives out a new character
    randNum = randint(0,len(keys)-1)
    return keys[randNum]
