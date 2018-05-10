from numpy import pi, cos, sin
import math
import Graphs

def Jerk_profile (acc_max, dec_max, time_acc, time_const, time_dec, time_inst, jerk_st):
    time_interpolation = time_inst
    time_instant = 0
    jerk_list = []
    time_jerklist = []
    jerk_acc = jerk_st
    jerk_dec = 0
    jerk_out = 0
    check = 0
    while time_instant < time_acc:
        jerk_acc = (acc_max*pi)/time_acc*sin((2*pi)/time_acc*time_instant)
        jerk_list += [jerk_acc]
        time_jerklist += [time_instant]
        time_instant = time_instant + time_interpolation
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        jerk_const = 0
        jerk_list += [jerk_const]
        time_jerklist += [time_instant]
        time_instant = time_instant + time_interpolation
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        check = 1
        jerk_dec = -(dec_max*pi)/time_acc*sin((2*pi)/time_acc*(time_instant-(time_acc+time_const)))
        jerk_list += [jerk_dec]
        time_jerklist += [time_instant]
        time_instant = time_instant + time_interpolation
    if jerk_dec == 0 and check == 0:
        jerk_out = jerk_acc
    elif jerk_dec == 0 and check == 1:
        jerk_out = jerk_dec
    else:
        jerk_out = jerk_dec
    return jerk_list, time_jerklist, jerk_out

"""Функция генерации профиля ускорения.
На вход подается:
1. Максимально возможное ускорение, мм/с^2.
2. Время разгона, с.
3. Время постоянной скорости, с.
4. Время торможения, с.
5. Время итерации, с.
6. Конечное ускорение предыдущего блока, мм/с^2.
На выход подается:
1. Список ускорений, мм/с^2.
2. Список временных промежутков, с.
3. Конечное ускорение на блоке, мм/с^2.
"""
def Acceleration_profile (acc_max, dec_max, time_acc, time_const, time_dec, time_instant, acc_st):
    time_interpolation = time_instant
    acc_list = []
    time_acclist = []
    acc = acc_st
    dec = 0
    acc_out = 0
    check = 0
    while time_instant < time_acc:
        acc = acc_st + acc_max/2*(1-math.cos((2*pi)/time_acc*time_instant))
        acc_list += [acc]
        time_acclist += [time_instant]
        time_instant = time_instant + time_interpolation
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        acc = 0
        acc_list += [acc]
        time_acclist += [time_instant]
        time_instant = time_instant + time_interpolation
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        check = 1
        dec = -dec_max/2*(1-math.cos((2*pi)/time_dec*(time_instant-(time_acc+time_const))))
        acc_list += [dec]
        time_acclist += [time_instant]
        time_instant = time_instant + time_interpolation
    if dec == 0 and check == 0:
        acc_out = acc
    elif dec == 0 and check == 1:
        acc_out = dec
    else:
        acc_out = dec
    return acc_list, time_acclist, acc_out

"""Функция генерации профиля скорости.
На вход подается:
1. Максимально возможное ускорение, мм/с2.
2. Время разгона, с.
3. Время торможения, с.
4. Время торможения, с.
5. Время итерации, с.
6. Конечная скорость предыдущего блока, мм/с.
7. Величина подачи, мм/с.
На выход подается:
1. Список скоростей, мм/с.
2. Список временных промежутков, с.
3. Конечная скорость в блоке, мм/с.
4. Максимальная достигнутая скорость инструмента, мм/с.
"""
def Velocity_profile (acc_max, dec_max, time_acc, time_const, time_dec, time_instant, vel_st, feedrate):
    time_interpolation = time_instant
    vel_list = []
    time_vellist = []
    vel_acc = vel_st
    vel_dec = 0
    vel_const = 0
    vel_out = 0
    check = 0
    vel_max = 0
    while time_instant < time_acc:
        vel_acc = vel_st + acc_max/2*(time_acc/(2*pi))*((2*pi)/time_acc*time_instant-sin((2*pi)/time_acc*time_instant))
        vel_list += [vel_acc]
        time_vellist += [time_instant]
        time_instant = time_instant + time_interpolation
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        vel_const = feedrate
        vel_list += [vel_const]
        time_vellist += [time_instant]
        time_instant = time_instant + time_interpolation
    if time_const == 0 and time_acc != 0:
        vel_max = vel_acc
    elif time_const == 0 and time_acc == 0:
        vel_max = vel_st
    elif time_const != 0:
        vel_max = vel_const
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        check = 1
        time_2 = time_acc+time_const
        vel_dec = dec_max/2*(-(time_instant-time_2)-(time_dec/(2*pi))*sin((2*pi)/time_dec*(-(time_instant-time_2))))+vel_max
        vel_list += [vel_dec]
        time_vellist += [time_instant]
        time_instant = time_instant + time_interpolation
    if vel_dec == 0 and check == 0:
        vel_out = vel_max
    elif vel_dec == 0 and check == 1:
        vel_out = vel_dec
    else:
        vel_out = vel_dec
    return vel_list, time_vellist, vel_out, vel_max

def Displacement_profile (acc_max, dec_max, time_acc, time_const, time_dec, time_inst, dis_start):
    dis_list = []
    dis_list_temp = []
    time_dislist = []
    check = 0
    check_1 = 0
    dis_dec_max = 0
    time_interpolation = time_inst
    time_instant = 0
    while time_instant < time_acc:
        dis_acc = (acc_max/2)*math.pow((time_acc/(2*math.pi)),2)*(1/2*math.pow((2*math.pi)/time_acc*time_instant, 2)-
                                                                (1-math.cos((2*math.pi)/time_acc*time_instant)))
        dis_list += [dis_acc]
        time_dislist += [time_instant]
        time_instant = time_instant + time_interpolation
        dis_plus = dis_start
    while time_instant >= time_acc and time_instant < time_const+time_acc:
        check_1 = 1
        dis = 1/4*acc_max*math.pow(time_acc, 2) + 1/2*acc_max*time_acc*(time_instant-time_acc)
        dis_list += [dis]
        time_dislist += [time_instant]
        time_instant = time_instant + time_interpolation
    while time_instant >= time_acc+time_const and time_instant <= time_acc+time_const+time_dec:
        check = 1
        t2 = time_acc-(time_instant-(time_acc+time_const))
        dis_dec = -(dec_max/2)*math.pow((time_acc/(2*math.pi)),2)*(1/2*math.pow((2*math.pi)/time_acc*t2, 2)-(1-math.cos((2*math.pi)/time_acc*t2)))
        #dis_dec = 1/4*acc_max*math.pow(time_acc, 2)+1/2*acc_max*time_const*time_acc+acc_max/2*math.pow(time_acc/(math.pi*2),2)*(
            #(math.pow(2*math.pi,2)*t2)/time_acc-1/2*math.pow((2*math.pi*math.pow(t2,2)/time_acc),2)+(1-math.cos(2*math.pi/time_acc*t2)))
        dis_list_temp += [dis_dec]
        time_dislist += [time_instant]
        time_instant = time_instant + time_interpolation
    dis_dec_max = dis_list_temp[0]
    if check_1 == 0:
        dis_plus = dis_acc
    elif check_1 == 1:
        dis_plus = dis - dis_dec_max
    for i in range (len(dis_list_temp)):
        dis_list.append(dis_list_temp[i]+dis_plus)
    return dis_list, time_dislist

"""Объединяет полученные значения времени и скоростей/ускорений в одиные списки
для построения графиков.
На вход подается:
1. Список значений скоротей/ускорений по блокам
2. Список индивидуальных временных промежутков для каждого блока.
На выход подается:
1. Список скорострей/ускорений.
2. Общий список временных промежутков для профиля."""
def Generation_hole_profile (acc_vel_list, time_list):
    result_time = []
    result_acc_vel = []
    for i in range (len(acc_vel_list)):
        for j in range (len(acc_vel_list[i])):
            result_acc_vel.append(acc_vel_list[i][j])
    for i in range (len(time_list)):
        if i > 0:
            temp = time_list[i-1][len(time_list[i-1])-1]
            for j in range (len(time_list[i])):
                time_list[i][j] = time_list[i][j] + temp
                result_time.append(time_list[i][j])
        else:
            for j in range (len(time_list[i])):
                result_time.append(time_list[i][j])
    return result_time, result_acc_vel
