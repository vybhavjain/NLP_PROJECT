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
    #turtle.write("Start")
    #turtle.circle(25,90)
    #turtle.circle(25/2,90)

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
        turtle.forward(y+10)
        turtle.left(70)
        turtle.forward(20)
        turtle.left(110)
        turtle.forward(2*y)
        turtle.left(70)
        turtle.forward(20)
        turtle.left(110)
        turtle.write(x)
        turtle.forward(y-10)
    
def flowchart(x):

    start()   # function to print the start inside the oval

    import turtle
    turtle.left(45)
    turtle.setpos(0,20)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,0)
    turtle.pendown()
    #turtle.setpos(-60,0)
    parallelogram("  1.Get a and b",40)
    turtle.setpos(0,-40)
    turtle.penup()   
    turtle.setpos(0,-60)
    turtle.pendown()
    #turtle.setpos(0,-60)
    #rectangle()
    y = " 2." + x + " both the numbers"
    #turtle.write(y)
    rectangle(y,60)
    turtle.setpos(0,-100)
    turtle.penup()   # makes pen disappear in the current block only
    turtle.setpos(0,-120)
    turtle.pendown()
    #turtle.setpos(0,-120)
    parallelogram("  3.Display the result",50)
    #turtle.write("3.Display the result")

    stop()  # function to print inside oval stop
    turtle.done()

print('enter one of the following operations to perform on two numbers')
print(' Add , subtract ,multiply , divide')
x = input('Add, subtract ,multiply,divide')
flowchart(x)

