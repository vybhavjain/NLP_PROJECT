# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:33:41 2018

@author: VYBHAV JAIN
"""

# shapes needed: oval,rectangle,rhombus
# logic to check: arrowmark 
# predefined sizes and fit words into correct sizes

import turtle 

def flatoval(r):               # Horizontal Oval
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
        
def rectangle():
    turtle.down()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    #turtle.right(20)
    #turtle.forward(20)

# def flowchart(x): # function that takes as input strong to display in the flowchart 
turtle.setpos(0,60)
flatoval(25)
turtle.write("Start")

turtle.left(45)
turtle.setpos(0,0)
#turtle.setpos(-60,0)
rectangle()
turtle.write("1.Receive 2 numbers from the user")
turtle.setpos(0,-20)


turtle.setpos(0,-60)
rectangle()
turtle.write("2.Add both the numbers")

turtle.setpos(0,-120)
rectangle()
turtle.write("3.Display the result")

turtle.setpos(0,-180)
flatoval(25)
turtle.write("Stop")



