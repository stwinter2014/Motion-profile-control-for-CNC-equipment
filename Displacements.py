import math
import Graphs
def Displacement_profile (acc_max, time_acc, time_const, time_dec, time_instant):
    dis_list = []
    time_dislist = []
    while time_instant < time_acc:
        dis_acc = acc_max/2*math.pow((time_acc/(2*math.pi)),2)*(1/2*math.pow((2*math.pi)/time_acc*time_instant, 2)-
                                                                (1-math.cos((2*math.pi)/time_acc*time_instant)))
        dis_list += [dis_acc]
        time_dislist += [time_instant]
        time_instant = time_instant + 0.1
    while time_instant >= time_acc and time_instant < time_const:
        dis_acc = 1/4*
        dis_list += [dis_acc]
        time_dislist += [time_instant]
        time_instant = time_instant + 0.1
    return dis_list, time_dislist
x_axys = Displacement_profile (5, 5, 10, 5, 0.05)[0]
y_axys = Displacement_profile (5, 5, 10, 5, 0.05)[0]
print(x_axys)
print(y_axys)
Graphs.Plotting_1 (x_axys, y_axys, "da", "da", "da")
