import math
def time_gen_normal (feedrate, length, max_acc, max_dec, len_ad):
    time_list = []
    time_acc = 0
    time_dec = 0
    time_con = 0
    time_acc = 2*feedrate/(len_ad/2)
    time_list.append(time_acc)
    time_list.append(time_con)
    time_dec = 2*feedrate/(len_ad/2)
    time_list.append(time_dec)
    len_ad = math.pow(feedrate, 2)/(2*max_acc)
    time_con = (length-len_ad)/feedrate
    time_list[1] = time_con
    return time_list

def time_gen_short (feedrate, length, max_acc, max_dec):
    time_list = []
    time_acc = 0
    time_dec = 0
    time_con = 0
    time_acc = feedrate/max_acc
    time_list.append(time_acc)
    time_list.append(time_con)
    time_dec = feedrate/max_dec
    time_list.append(time_dec)
    return time_list

def point_search (start_point, finish_point, length_part, way_to_search):
    length = Path_length_calculator.path_linear(start_point, finish_point)
    result_point = []
    y_angle = 0
    x_angle = 0
    x_distance = math.fabs(start_point[0] - finish_point[0])
    y_distance = math.fabs(start_point[1] - finish_point[1])
    print(x_distance)
    print(y_distance)
    z_distance = math.fabs(start_point[2] - finish_point[2])
    if x_distance != 0 and y_distance == 0:
        if way_to_search == 0:
            if finish_point[0] > start_point[0]:
                result_point = [finish_point[0] - length_part, finish_point[1], finish_point[2]]
            else:
                result_point = [finish_point[0] + length_part, finish_point[1], finish_point[2]]
        else:
            if finish_point[0] > start_point[0]:
                result_point = [start_point[0] + length_part, start_point[1], start_point[2]]
            else:
                result_point = [start_point[0] - length_part, start_point[1], start_point[2]]
    elif x_distance == 0 and y_distance != 0:
        if way_to_search == 0:
            if finish_point[0] > start_point[0]:
                result_point = [finish_point[0] - length_part, finish_point[1], finish_point[2]]
            else:
                result_point = [finish_point[0] + length_part, finish_point[1], finish_point[2]]
        else:
            if finish_point[0] > start_point[0]:
                result_point = [start_point[0] + length_part, start_point[1], start_point[2]]
            else:
                result_point = [start_point[0] - length_part, start_point[1], start_point[2]]
    elif x_distance != 0 and y_distance != 0:
        y_angle = math.asin(x_distance/length)
        x_angle = math.asin(y_distance/length)
        x_part = y_angle*length_part
        y_part = x_angle*length_part
        
    return y_angle, x_angle

"""
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
    if Ac > max_acc:
        speed_list[0] = 0
    else:
        speed_list[1] = 0
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
"""
