# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 12:13:08 2018

@author: VYBHAV JAIN
"""

import turtle
import math

def circle(radius,color,color1):   
    x = color
    y = color1
    turtle.up()
    # go to (0, radius)
    turtle.goto(0,radius)
    turtle.down()    
    turtle.color(x,y)
    turtle.begin_fill()
    # number of times the y axis has been crossed
    times_crossed_y = 0
    x_sign = 1.0
    while times_crossed_y <= 1:
        # move by 1/360 circumference
        turtle.forward(2*math.pi*radius/360.0)
        # rotate by one degree (there will be
        # approx. 360 such rotations)
        turtle.right(1.0)
        # we use the copysign function to get the sign
        # of turtle's x coordinate
        x_sign_new = math.copysign(1, turtle.xcor())        
        if(x_sign_new != x_sign):
            times_crossed_y += 1
        x_sign = x_sign_new
    turtle.end_fill()
    return  



def square1(dim,color,color1):
    x = color
    y = color1    
    turtle.color(x,y)
    turtle.begin_fill()
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    turtle.end_fill()
    return

def rectangle1(dim1,dim2,color,color1): #color 1 is going to be filled inside
    x = color
    y = color1
    turtle.color(x,y)
    turtle.begin_fill()
    turtle.forward(dim1)
    turtle.left(90)
    turtle.forward(dim2)
    turtle.left(90)
    turtle.forward(dim1)
    turtle.left(90)
    turtle.forward(dim2)
    turtle.left(90)
    turtle.end_fill()

# for circle ,pass radius ,pen color and then filling color
# for square,pass side,pen color and then filling color
# for rectangle ,pass breadth,height ,pen color and then filling color
y = 'blue'    # color to be passed 
# circle (100,'orange','red')    ## verified that its working
#rectangle1(100,10,'orange','red')  ## verified that its working    
#square1(50,y)
print('finished')
turtle.done()

