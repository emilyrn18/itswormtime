import librosa as lr
import turtle 
import random

def draw_beats(tur, item ):
    tur.forward(item)
    tur.left(10)
    tur.forward(10)
    tur.left(10)
    tur.backward(item)
    tur.left(10)
    tur.forward(10)
    tur.left(10)
    tur.circle(item, 30)

dst = 'sherlockr.wav'
#random = dst

y , sr = lr.load(dst)
tempo, beats = lr.beat.beat_track(y=y)
#print(len(tempo[1]), tempo)
print(tempo)
#harmonics
har = lr.effects.harmonic(y=y)
#har1 = tle.Turtle()
#har1.speed(0)
#har1.color('red')

#percussions
#per = lr.effects.percussive
#per1 = tle.Turtle()
#per1.speed(0)
#per1.color('orange')

#drawing 
ben = turtle.Turtle()
ben.speed(tempo)
for item in beats:
    draw_beats(ben, item)
    #print(item)

