# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:55:12 2018

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
        
flatoval(20)
turtle.write("anything")
