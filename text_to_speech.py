import turtle
import math

def circle(radius,color):   
    x = color
    turtle.up()
    # go to (0, radius)
    turtle.goto(0,radius)
    turtle.down()    
    turtle.color(x)
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
    return  



def square1(dim,color):
    x = color
    turtle.color(x)
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    return

def rectangle1(dim1,dim2,color):
    x = color
    turtle.color(x)
    turtle.forward(dim1)
    turtle.left(90)
    turtle.forward(dim2)
    turtle.left(90)
    turtle.forward(dim1)
    turtle.left(90)
    turtle.forward(dim2)
    turtle.left(90)
    
y = 'blue'    # color to be passed 
#circle (100)
#rectangle1(100,10)    
square1(50,y)
print('finished')
turtle.done()

