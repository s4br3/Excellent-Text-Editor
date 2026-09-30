from tkinter import *
from random import randint,uniform

keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!£$%^&*()_+=-{}[]@~'#?<>;:/?"+'"'
keys = list(keys)

def read_input(event): # reads what characters are being read from the user
	randDouble = uniform(0,1)

	if (randomDouble < 0.5):
		pass
	else:
		if (event.char in keys):
			newChar = map_input_to_new_char(event.char)
			event.char = newChar

def map_input_to_new_char(char): # takes a user character and gives out a new character
	randNum = randint(0,keys.len)
	return keys[randNum]
