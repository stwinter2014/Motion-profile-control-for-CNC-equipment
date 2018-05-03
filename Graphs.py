import matplotlib.pyplot as plt
import matplotlib as mpl
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
Функция построения графиков.
На вход принимается:
1. Значения оси x: время.
2. Значения оси y: ускорение, скорость, перемещение или толчок.
3. Название оси x.
4. Название оси y.
5. Название графика.
6. 
"""
def Plotting_1 (x, y, name_x, name_y, name_graph, label, time_per):
    time_sum = 0
    time_sum_hole = 0
    alph = 0.2
    plt.plot(x,y,label=label)
    currentAxis = plt.gca()
    for i in range (len(time_per)):
        for j in range (len(time_per[i])-1):
            time_sum += time_per[i][j]
        currentAxis.add_patch(mpl.patches.Rectangle((time_sum_hole, -10), time_sum, 100, alpha=alph, color='#D5D0CF'))
        time_sum_hole += time_sum
        time_sum = 0
        if i%2 == 0:
            alph += 0.2
        else:
            alph -= 0.2
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(name_graph)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'w')
    plt.show()

def Plotting_01 (x, y, name_x, name_y, name_graph, label):
    plt.plot(x,y,label=label)
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(name_graph)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'w')
    plt.show()

def Plotting_2 (x, y, x2, y2, name_x, name_y1, name_y2, name_graph1, name_graph2):
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

def Timing_1 (displacement_1, displacement_2, feedrate, acc_max):
    time_const1 = (displacement_1 - (feedrate*feedrate)/(2*acc_max))/feedrate
    time_const2 = (displacement_1 - (feedrate*feedrate)/(2*acc_max))/feedrate
    time_acc = feedrate/acc_max
    time_dec = feedrate/acc_max
    return time_const1, time_const2, time_acc, time_dec

"""
acceleration_max = 5
feedrate = 10
time_1 = Timing_1(20, 14, feedrate, acceleration_max)[2]
time_2 = Timing_1(20, 14, feedrate, acceleration_max)[0]+Timing_1(20, 14, feedrate, acceleration_max)[1]
time_3 = Timing_1(20, 14,10, acceleration_max)[3]
time_start = 0
Plotting_1(Jerk(acceleration_max, time_1, time_2, time_3, time_start)[1], Jerk(acceleration_max, time_1, time_2, time_3, time_start)[0],
         'Time', 'Jerk', 'Jerk Profile')
Plotting_2 (Acceleration_profile(acceleration_max, time_1, time_2, time_3, time_start)[1],
          Acceleration_profile(acceleration_max, time_1, time_2, time_3, time_start)[0],
          Velocity_profile(acceleration_max, time_1, time_2, time_3, time_start)[1],
          Velocity_profile(acceleration_max, time_1, time_2, time_3, time_start)[0],
          'Time', 'Acceleration', 'Velocity', 'Acceleration Profile', 'Velocity Profile')
"""
