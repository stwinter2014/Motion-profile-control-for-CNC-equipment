import math
step = 0.0125
acc = 5
feedrate = 10
l = math.pow(feedrate, 2)/acc
t = 2*feedrate/acc
print("Время " + str(t))
lstep = l/step
tstep = t/lstep
print(lstep, tstep)
