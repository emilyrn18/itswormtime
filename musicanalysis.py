import librosa as lr
import turtle as tle


dst = 'sherlockr.wav'

y , sr = lr.load(dst)
p = lr.beat.beat_track(y=y)
for item in p[1]:
    tle.forward(item)
    tle.left(10)
    tle.forward(10)
    tle.left(10)
    tle.backward(item)
    tle.left(10)
    tle.forward(10)
    tle.left(10)
    tle.circle(item)