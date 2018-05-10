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

def Acceleration_profile (acc_max, time_acc, time_const, time_dec, time_instant):
    acc_list = []
    time_acclist = []
    while time_instant < time_acc:
        acc = acc_max/2*(1-math.cos((2*pi)/time_acc*time_instant))
        acc_list += [acc]
        time_acclist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        acc = 0
        acc_list += [acc]
        time_acclist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        dec = -acc_max/2*(1-math.cos((2*pi)/time_dec*(time_instant-(time_acc+time_const))))
        acc_list += [dec]
        time_acclist += [time_instant]
        time_instant = time_instant + 0.1
    return acc_list, time_acclist

def Velocity_profile (acc_max, time_acc, time_const, time_dec, time_instant):
    vel_list = []
    time_vellist = []
    while time_instant < time_acc:
        vel_acc = acc_max/2*(time_acc/(2*pi))*((2*pi)/time_acc*time_instant-math.sin((2*pi)/time_acc*time_instant))
        vel_list += [vel_acc]
        time_vellist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        vel_const = 1/2*acc_max*time_acc
        vel_list += [vel_const]
        time_vellist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        time_2 = time_acc+time_const
        vel_dec = acc_max/2*(-(time_instant-time_2)-(time_acc/(2*pi))*sin((2*pi)/time_acc*(-(time_instant-time_2))))+vel_acc
        vel_list += [vel_dec]
        time_vellist += [time_instant]
        time_instant = time_instant + 0.1
    return vel_list, time_vellist

def Jerk (acc_max, time_acc, time_const, time_dec, time_instant):
    jerk_list = []
    time_jerklist = []
    while time_instant < time_acc:
        jerk_acc = (acc_max*pi)/time_acc*sin((2*pi)/time_acc*time_instant)
        jerk_list += [jerk_acc]
        time_jerklist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        jerk_const = 0
        jerk_list += [jerk_const]
        time_jerklist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        jerk_dec = -(acc_max*pi)/time_acc*sin((2*pi)/time_acc*(time_instant-(time_acc+time_const)))
        jerk_list += [jerk_dec]
        time_jerklist += [time_instant]
        time_instant = time_instant + 0.1
    return jerk_list, time_jerklist
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
import matplotlib.pyplot as plt
from numpy import pi, cos, sin
import math

def Acceleration_profile (acc_max, time_acc, time_const, time_dec, time_instant):
    acc_list = []
    time_acclist = []
    while time_instant < time_acc:
        acc = acc_max/2*(1-math.cos((2*pi)/time_acc*time_instant))
        acc_list += [acc]
        time_acclist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        acc = 0
        acc_list += [acc]
        time_acclist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        dec = -acc_max/2*(1-math.cos((2*pi)/time_dec*(time_instant-(time_acc+time_const))))
        acc_list += [dec]
        time_acclist += [time_instant]
        time_instant = time_instant + 0.1
    return acc_list, time_acclist

def Velocity_profile (acc_max, time_acc, time_const, time_dec, time_instant):
    vel_list = []
    time_vellist = []
    while time_instant < time_acc:
        vel_acc = acc_max/2*(time_acc/(2*pi))*((2*pi)/time_acc*time_instant-math.sin((2*pi)/time_acc*time_instant))
        vel_list += [vel_acc]
        time_vellist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        vel_const = 1/2*acc_max*time_acc
        vel_list += [vel_const]
        time_vellist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        time_2 = time_acc+time_const
        vel_dec = acc_max/2*(-(time_instant-time_2)-(time_acc/(2*pi))*sin((2*pi)/time_acc*(-(time_instant-time_2))))+vel_acc
        vel_list += [vel_dec]
        time_vellist += [time_instant]
        time_instant = time_instant + 0.1
    return vel_list, time_vellist

def Plotting (x, y, x2, y2, name_x, name_y1, name_y2, name_graph1, name_graph2):
    fig = plt.figure()
    fig1 = fig.add_subplot(211)
    fig2 = fig.add_subplot(212)
    fig1.set_title(name_graph1)
    fig1.plot(x, y)
    fig2.set_title(name_graph2)
    fig2.plot(x2, y2)
    fig1.set_ylabel(name_y1)
    fig2.set_ylabel(name_y2)
    plt.xlabel(name_x)
    plt.show()


acceleration_max = 34
time_1 = 4
time_2 = 5
time_3 = 4
time_start = 0
Plotting (Acceleration_profile(acceleration_max, time_1, time_2, time_3, time_start)[1],
          Acceleration_profile(acceleration_max, time_1, time_2, time_3, time_start)[0],
          Velocity_profile(acceleration_max, time_1, time_2, time_3, time_start)[1],
          Velocity_profile(acceleration_max, time_1, time_2, time_3, time_start)[0],
          'Time', 'Acceleration', 'Velocity', 'Acceleration Profile', 'Velocity Profile')

