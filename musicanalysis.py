import librosa as lr
import turtle 
import random
import sklearn.preprocessing as sk
from playsound import playsound
import winsound

def draw_beats(tur, item ):
    tur.forward(item)
    tur.penup()
    tur.backward(item)
    tur.left(7)
    tur.pendown()
   

dst = 'sherlockr.wav'
#random = dst

y , sr = lr.load(dst)
tempo, beats = lr.beat.beat_track(y=y, sr=sr)
#print(len tempo)
#print(tempo)
#print(beats, len(beats))

#harmonics
b = lr.beat.plp(y=y)
#print("b = ", b)

har = lr.effects.harmonic(y=y)
#har1 = tle.Turtle()
#har1.speed(0)
#har1.color('red')

#percussions
#per = lr.effects.percussive
#per1 = tle.Turtle()
#per1.speed(0)
#per1.color('orange')
t = lr.feature.spectral_bandwidth(y=y, sr=sr)
t = list(map(lambda x: int(x), t[0]))
t = sk.scale(t)
print(t)
#drawing 
ben = turtle.Turtle()
ben.speed(10)
import pygame
pygame.mixer.init()
pygame.mixer.music.load("sherlockr.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
for item in t:
    draw_beats(ben, item*100)
    #print(item)

