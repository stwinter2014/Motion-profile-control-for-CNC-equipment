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
