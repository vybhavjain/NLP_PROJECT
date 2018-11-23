# try if condition , rhombus for an example
# make neater
# try arranging in centre

import turtle 

def flatoval(r):               # Horizontal Oval
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
        
def start():
    turtle.setpos(0,60)
    flatoval(25)
    turtle.write("Start")

def stop():
   turtle.setpos(0,-180)
   flatoval(25)
   turtle.write("Stop")

def rectangle(): 
   turtle.down()    
   for i in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
    
def flowchart(x):

    start()   # function to print the start inside the oval

    turtle.left(45)
    turtle.setpos(0,0)
    #turtle.setpos(-60,0)
    rectangle()
    turtle.write("1.Receive 2 numbers from the user")
    turtle.setpos(0,-20)
    turtle.setpos(0,-60)
    rectangle()
    y = "2." + x + " both the numbers" # need to check if this working 
    turtle.write(y)
    turtle.setpos(0,-120)
    rectangle()
    turtle.write("3.Display the result")

    stop()  # function to print inside oval stop

print('enter one of the following operations to perform on two numbers')
#print(“ Add , subtract ,multiply , divide”)
x = input('Add, subtract ,multiply,divide')
flowchart(x)


