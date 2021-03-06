# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:26:17 2018

@author: VYBHAV JAIN
"""

import turtle 

def flatoval(r):               # Horizontal Oval
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-(r/1.414),120+(r/1.414))
    turtle.pendown()
    turtle.write("  Start")
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
    turtle.circle(r,45)
    turtle.right(90)
    turtle.forward(40)
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
    turtle.setpos(-(r/1.414),-(210+(r/1.414)))
    turtle.pendown()

    #turtle.write("Start")
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)    
        
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

def start():
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,120)
    turtle.pendown()
    #turtle.write("Start")
    flatoval(25)

def stop():
   #turtle.setpos(0,-155)
   #arrow()
   turtle.penup()   
   turtle.setpos(0,-180)
   turtle.pendown()   
   flatoval1(25)
   turtle.write("  Stop")

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
    #turtle.penup()   
    #turtle.setpos(-25,-80)
    #turtle.pendown()
    #turtle.write('is a>b?')
    
    
def flowchart1():

    start()   # function to print the start inside the oval

    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,90)
    turtle.pendown()

    arrow()
    #turtle.left(90)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,70)
    turtle.pendown()
    rectangle("  Initialise sum = 0 ",50)
    turtle.setpos(0,40)
    #turtle.right(90)
    arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,20)
    turtle.pendown()
    parallelogram('  get a' ,20)
    turtle.setpos(0,-20)
    arrow()
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,-40)
    turtle.pendown()
    rectangle("  sum = sum + a ",50)
    turtle.setpos(0,-70)
    arrow()

    #turtle.left(90)
    rhombus(70)  # position here is 0,-70
    
    # loop back starts here
    
    turtle.right(90)
    turtle.forward(70)
    turtle.right(45)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward((100+(70/1.414)))
    turtle.write('yes')
    turtle.right(90)
    turtle.forward(50+(70/1.414))
    turtle.left(90)
    arrow()
    turtle.right(90)

    # loopback is over
   
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-25,-110)
    turtle.pendown()
    turtle.write('Any more')
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-35,-125)
    turtle.pendown()
    turtle.write('numbers left to')
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(-25,-140)
    turtle.pendown()
    turtle.write('     Add?')
    
    # end of rhombus condition
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,-70)
    turtle.pendown()
    
    # switch to new location with required arrow
    
    turtle.right(45)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(45)
    turtle.forward(25)
    turtle.write('  No')
    turtle.forward(10)
    turtle.left(90)
    arrow()
    
    
    stop()  # function to print inside oval stop
    turtle.hideturtle()
    turtle.done()

#print('enter one of the following operations to perform on two numbers')
#print(' Add , subtract ,multiply , divide')
#x = input('Add, subtract ,multiply,divide')
flowchart1()
