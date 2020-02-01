import librosa as lr
import turtle as tle
import random

dst = 'sherlockr.wav'
random = dst

y , sr = lr.load(dst)
p = lr.beat.beat_track(y=y)

#harmonics
har = lr.effects.harmonic(y=y)
har1 = tle.Turtle()
#har1.speed(0)
har1.color('red')

#percussions
per = lr.effects.percussive
per1 = tle.Turtle()
#per1.speed(0)
per1.color('orange')

#drawing 
for item in p[1]:
    har1.forward(item)
    har1.left(10)
    per1.forward(10)
    tle.left(10)
    tle.backward(item)
    tle.left(10)
    tle.forward(10)
    tle.left(10)
    tle.circle(item, 30)