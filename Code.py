import turtle
import math
import speech_recognition as sr
import re

def circle(radius):    
    turtle.up()
    # go to (0, radius)
    turtle.goto(0,radius)
    turtle.down()    
    turtle.color("red")
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




def square1(dim):
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    return

def rectangle1(dim):
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim/2)
    turtle.left(90)
    turtle.forward(dim)
    turtle.left(90)
    turtle.forward(dim/2)
    turtle.left(90)

def findmatches(pattern, phrase):

    for p in patterns:
        match= re.findall(p, phrase)
        return match




r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say Something')
    audio=r.listen(source)
    
try:
    print('Google thinks you said:\n' + r.recognize_google(audio))
    
except:
    pass

n=r.recognize_google(audio)
patterns= [r'\d+']
radd=findmatches(patterns, n)

if len(radd)==0:
    int22=int('1')
else:
    str1 = ''.join(radd)
    int22 = int(str1)
wordList = re.sub("[^\w]", " ",  n).split()

if 'circle' in wordList:
    circle(20*int22)
    print('finished')
    turtle.done()
    
elif 'square' in wordList:
    square1(20*int22)
    print('finished')
    turtle.done()
    
elif 'rectangle' in wordList:
    rectangle1(20*int22)
    print('finished')
    turtle.done()
    

