import math
from numpy import cos, sin
import Graphs

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

#print(corner_speed_angle (feedrate[0], feedrate[1], acc, angle, time))

def circular_motion (feedrate, radius, max_acc, time_instant):
    time = 40
    w = feedrate/radius
    feedr_list = []
    time_list = []
    for i in range (0, time):
        Vx = feedrate*math.cos(math.radians(time_instant*w))
        Vy = feedrate*sin(time_instant*w)
        V = math.sqrt(Vx*Vx+Vy*Vy)
        Ax = -feedrate*w*sin(time_instant*w)
        Ay = feedrate*w*cos(time_instant*w)
        temp = math.fabs(radius*(Ax+Ay))
        F = math.sqrt(temp)
        feedr_list.append(F)
        time_instant += time_instant
        time_list.append(time_instant)
    Graphs.Plotting_2(time_list, feedr_list, time_list, feedr_list, "da", "da", "da", "da", "da")

circular_motion(feedrate[0], 71, acc, time)






