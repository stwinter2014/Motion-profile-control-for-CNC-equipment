import math
from numpy import cos

feedrate = [10, 10]
acc = 5
angle = 5
time = 0.05

def corner_speed_angle (feedrate_1, feedrate_2, max_acc, angle, time_int):
    speed_list = []
    Ac = feedrate[0]-feedrate[1]*cos(math.radians(angle))
    Fc = max_acc*time_int/(1-cos(math.radians(angle)))
    speed_list.append(Ac)
    speed_list.append(Fc)
    """if Ac > max_acc:
        speed_list[0] = 0
    else:
        speed_list[1] = 0"""
    return speed_list

print (corner_speed_angle (feedrate[0], feedrate[1], acc, angle, time))
