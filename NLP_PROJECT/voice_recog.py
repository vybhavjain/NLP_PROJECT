# -*- coding: utf-8 -*-
import turtle
import speech_recognition as sr
import re
import shapes
from flowchart_addsubmuldiv import flowchart
#import comparator
import color_shape

def findmatches(pattern, phrase):

    for p in patterns:
        match= re.findall(p, phrase)
        return match




r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say Something')
    audio=r.listen(source)
    
try:
    print('Google thinks you said:\n' + r.recognize_ibm(audio))
    
except:
    pass

n=r.recognize_ibm(audio)
patterns= [r'\d+']
radd=findmatches(patterns, n)

if len(radd)==0:
    int22=int('1')
else:
    str1 = ''.join(radd)
    int22 = int(str1)
    
wordList = re.sub("[^\w]", " ",  n).split()



if 'circle' in wordList:
    #if 'color' in wordList:
    color_shape.circle(20*int22,"red","blue")
   # else:
      #  shapes.circle(20*int22)
       # print('finished')
        #turtle.done()
        
elif 'square' in wordList:
    shapes.square1(20*int22)
    print('finished')
    turtle.done()
    
elif 'rectangle' in wordList:
    if 'color' in wordList:
        color_shape.rectangle1(20*int22,(20*int22)/2,"red","blue")
    else:
        shapes.rectangle1(20*int22)
        print('finished')
        turtle.done()
    
elif 'flowchart' in wordList:
    if 'add' in wordList:
        flowchart('add')
    elif 'subtract' in wordList:
        flowchart('subtract')
    elif 'multiply' in wordList:
        flowchart('multiply')
    elif 'division' in wordList:
        flowchart('division')
    else:
        import comparator
        comparator.flowchart1()
        print("OK")
        
        
elif 'star' in wordList:
    color_shape.star("red","blue",20*int22)
    
else:
    print("INVALID")
        

        
        
        
        



