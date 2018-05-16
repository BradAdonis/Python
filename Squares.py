from tkinter import *
import random

def drawLine():
	canvas.create_line(5, 5, 100, 100)

tk = Tk()
canvas = Canvas(tk, width=200, height=200)
canvas.pack()

canvas.create_text(150, 175, text='Hi Shannon! :D', font=('Verdana',15), fill='blue')

btn = Button(tk, text="draw a line", command=drawLine)
btn.pack()

for x in range(0, 5):

	j = random.randint(0, 175)
	canvas.create_rectangle(j, j, 25, 25, outline='purple', fill='red')

#input('slow your roll')
