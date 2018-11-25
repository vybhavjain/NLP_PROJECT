# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:21:23 2018

@author: VYBHAV JAIN
"""

import turtle 

def flatoval(r):               # Horizontal Oval
    turtle.right(45)
    #turtle.write("Start")
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
        
def start():
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,60)
    turtle.pendown()
    turtle.write("Start")
    flatoval(25)

def stop():
   turtle.setpos(0,-162.5)
   turtle.penup()   
   turtle.setpos(0,-180)
   turtle.pendown()   
   flatoval(25)
   turtle.write("Stop")

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
        
def rhombus(x):
    turtle.right(45)
    for i in range(4):
        turtle.forward(x)
        turtle.right(90)
    turtle.penup()   
    turtle.setpos(-25,-80)
    turtle.pendown()
    turtle.write('is a>b?')
    
    
def flowchart1():

    start()   # function to print the start inside the oval

    turtle.left(45)
    turtle.setpos(0,20)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,0)
    turtle.pendown()
    #turtle.setpos(-60,0)
    parallelogram("  Get a and b",40)
    turtle.setpos(0,-40)
    rhombus(60)
    turtle.penup()   
    turtle.setpos(0,-40)
    turtle.pendown()
    turtle.forward(60)
    #turtle.right(90) 
    turtle.left(45)
    turtle.forward(70)
    turtle.write('yes')
    turtle.right(90)
    turtle.forward(60)
    turtle.penup()   
    #turtle.setpos(0,-180)
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    parallelogram("  display a ",30)

    '''
    turtle.setpos(0,-100)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,-120)
    turtle.pendown()
    #turtle.setpos(0,-120)
    parallelogram("  Display the result",50)
    
    stop()  # function to print inside oval stop
    '''
    turtle.done()

#print('enter one of the following operations to perform on two numbers')
#print(' Add , subtract ,multiply , divide')
#x = input('Add, subtract ,multiply,divide')
flowchart1()
