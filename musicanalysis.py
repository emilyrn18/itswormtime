import librosa as lr
import turtle as t


dst = 'sherlockr.wav'

y , sr = lr.load(dst)
p = lr.beat.beat_track(y=y)
for item in p[1]:
    t.forward(item)
    t.left(10)
    t.forward(10)
    t.left(10)
    t.backward(item)
    t.left(10)
    t.forward(10)
    t.left(10)