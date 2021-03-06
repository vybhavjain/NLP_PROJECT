# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:45:39 2018

@author: VYBHAV JAIN
"""

import turtle 

def flatoval(r):               # Horizontal Oval
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-(r/1.414),60+(r/1.414))
    turtle.pendown()
    turtle.write("  Start")
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
    turtle.circle(r,45)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    '''
    turtle.right(180)
    turtle.forward(40)
    turtle.left
    turtle.circle(r,45)
    turtle.circle(r/2,90)
    turtle.circle(r,90)
    turtle.circle(r/2,90)
    '''
        
def flatoval1(r):               # Horizontal Oval
    turtle.right(45)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-(r/1.414),-(162.5+(r/1.414)))
    turtle.pendown()

    #turtle.write("Start")
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)    
        
def start():
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,60)
    turtle.pendown()
    #turtle.write("Start")
    flatoval(25)

def stop():
   turtle.setpos(0,-155)
   arrow()
   turtle.penup()   
   turtle.setpos(0,-180)
   turtle.pendown()   
   flatoval1(25)
   turtle.write("  Stop")


def arrow():
    turtle.left(135)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.right(45)
    turtle.right(180)


def rectangle(x,y): 
        turtle.forward(y)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(2*y)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.write(x)
        turtle.forward(y)
        
def parallelogram(x,y): 
        turtle.forward(y+5)
        turtle.left(70)
        turtle.forward(20)
        turtle.left(110)
        turtle.forward(2*y)
        turtle.left(70)
        turtle.forward(20)
        turtle.left(110)
        turtle.write(x)
        turtle.forward(y-5)
    
def flowchart(x):

    start()   # function to print the start inside the oval
   # turtle.left(45)
    turtle.setpos(0,20)
    arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,0)
    turtle.pendown()
    #turtle.setpos(-60,0)
    parallelogram("     Get a and b",40)
    turtle.setpos(0,-40)
    arrow()    
    turtle.penup()   
    turtle.setpos(0,-60)
    turtle.pendown()
    #turtle.setpos(0,-60)
    #rectangle()
    y = '  ' + x + " a and b "
    
    #turtle.write(y)
    rectangle(y,45)
    turtle.setpos(0,-100)
    arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,-120)
    turtle.pendown()
    #turtle.setpos(0,-120)
    parallelogram("    Display the result",50)
    #turtle.write("3.Display the result")

    stop()  # function to print inside oval stop
    turtle.hideturtle()
    turtle.done()

#print('enter one of the following operations to perform on two numbers')
#print(' Add , subtract ,multiply , divide')
#x = input('Add, subtract ,multiply,divide')
flowchart('  Add')

