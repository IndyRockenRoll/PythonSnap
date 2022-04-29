# Write your code here :-)

import random
import time

from tkinter import Tk, Canvas, HIDDEN, NORMAL # tkinter is a standard python library for building windowed applications

# local function definitions
def next_shape():
    global shape
    global previous_color
    global current_color

    previous_color = current_color
    c.delete(shape)
    if len(shapes) > 0:
        shape = shapes.pop()
        c.itemconfigure(shape, state=NORMAL)
        current_color = c.itemcget(shape, 'fill')
        root.after(1000, next_shape)
    else:
        c.unbind('q')
        c.unbind('p')
        if player1_score > player2_score:
            c.create_text(200, 200, text='Winner: Player 1')
        elif player2_score > player1_score:
            c.create_text(200, 200, text='Winner: Player 2')
        else:
            c.create_text(200, 200, text='Draw')
        c.pack()

def snap(event):
    global shape
    global player1_score
    global player2_score
    valid = False

    c.delete(shape)

    if previous_color == current_color:
        valid = True

    if valid:
        if event.char == 'q':
            player1_score = player1_score + 1
        else:
            player2_score = player2_score + 1
        shape = c.create_text(200, 200, text='SNAP! You score 1 point!')
    else:
        if event.char == 'q':
            player1_score = player1_score - 1
        else:
            player2_score = player2_score - 1
        shape = c.create_text(200, 200, text='WRONG! You lose 1 point!')
    c.pack()
    root.update_idletasks()
    time.sleep(1)


########################################
## MAIN PROGRAM
########################################

root = Tk() # this generates a default unsized application window with an object reference name of "root"

root.title('Snap') # this puts a title on the window title bar of "Snap"

c = Canvas(root, width=400, height=400) # this creates a blank background "Canvas" 400 pixels by 400 and places it on the root window

shapes = [] # this list variable will store the shape objects

# the following creates 4 circles of different colours on the canvas, all HIDDEN to begin with
# and each circle object is stored in the shapes list as it is created so we can refer to it later
# the first 2 numbers in create_oval are the x y coords on the top left of the box around the oval
# where 0,0 is top left of the window. And 2nd two numbers are the x y coords of the bottom right.

circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(circle)

circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(circle)

circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(circle)

circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(circle)

c.pack() # this command actually puts the shape onto the canvas variable c

# now the same basic idea only this time with rectangle shapes, again all hidden for now
rectangle = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN)
shapes.append(rectangle)

rectangle = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN)
shapes.append(rectangle)

rectangle = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
shapes.append(rectangle)

rectangle = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
shapes.append(rectangle)

c.pack()

# again using the rectangle function but picking coords that actually produce a square
# we know this is a square because 365 - 35 = 330 (length on the x side) and 350 - 20 = 330 (length on the y side)
square = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(square)

square = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(square)

square = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(square)

square = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(square)

c.pack()

random.shuffle(shapes) # a super handy function from the random library that random shuffles our shapes list

# some initial setup - variables for use in the game
shape = None              # None is a special python keyword that means Null or No Value at all i.e. blank
previous_color = ''
current_color = ''
player1_score = 0
player2_score = 0

root.after(3000, next_shape) # After calls the "next_shape" function after 3000 milliseconds = 3 s, this creates a slight pause before starting
c.bind('q', snap)
c.bind('p', snap)
c.focus_set()

root.mainloop()
