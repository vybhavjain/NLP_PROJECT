# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:55:12 2018

@author: VYBHAV JAIN
"""
import turtle 

def flatoval(r):               # Horizontal Oval
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
        
flatoval(20)
turtle.write("anything")
