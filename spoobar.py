import turtle
import random

# Hard coded values

pitches = [
        0.709,
        0.092,
        0.196,
        0.084,
        0.352,
        0.134,
        0.161,
        1,
        0.17,
        0.161,
        0.211,
        0.15
      ]

for x in range(1000):
    pitches.append(random.randint(0,100)/100)

tempo = 98.253

dance = 0.735

benny = turtle.Turtle()
benny.speed(2)
benny._pensize = 5
for p in pitches:
   # num = p*2
    benny.pencolor(random.randint(0,255)/255, random.randint(0,255)/255, random.randint(0,255)/255)
    benny.forward(p*100)
    benny.penup()
    benny.backward(p*100)
    benny.left(10)
    benny.pendown()
    



