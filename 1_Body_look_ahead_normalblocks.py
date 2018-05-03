import Path_length_calculator
import Block_type
import Profile_generation
import Graphs
import Work_with_files
import math

"""Коды типов G-инструкций:
001 - G00;
010 - G01;
011 - G02 + радиус;
100 - G03 + радиус;
101 - G02 + координаты центра;
110 - G03 + координаты центра.
"""

"""Тело программы"""
path_code = ["010", "010", "010"]

"""Данные об обработке"""
feedrate = [10, 8, 12, 13]
max_acceleration = 5
max_deceleration = 5
time_periods = []

"""Данные о перемещении"""
path_l_list = []
path_l = 0
st_point = [[8.956, 0, 26.437],
            [65, 0, 0],
            [39, 0, 0]]
fn_point = [[79.616,0,90.494],
            [65, 72, 0],
            [39, 80, 0]]
cn_point = [[79.616,0,19.494],
            [79.616,0,90.494],
            [79.616,0,90.494]]
rad = [71, 0, 71]
way_move = [1, 0, 1]

feedr_n = 0

f_acc = 0
l_dec = 0
vel_start = 0
hole_temp_time = []
hole_temp_time_1 = []
hole_temp_vel = []
hole_temp_acc = []
hole_profile = []
Work_with_files.Clear_log()
for i in range (len(path_code)):
    print(Work_with_files.Write_log("Подсчет длины пути блока " + str(i+1) + "."))
    type_path = Path_length_calculator.path_type(path_code[i])
    """Подсчет длины пути"""
    if type_path == 1:
        print(Work_with_files.Write_log("Тип интерполяции - линейный."))
        path_l = Path_length_calculator.path_linear(st_point[i], fn_point[i])
        path_l_list.append(path_l)
        path_l = 0
        print(Work_with_files.Write_log("Длина пути: " + str(path_l_list[i]) + " мм."))
    elif type_path == 2:
        print(Work_with_files.Write_log("Тип интерполяции - круговой. Задание окружности с помощью радиуса."))
        path_l = Path_length_calculator.path_circular_r (st_point[i], fn_point[i], rad[i], way_move[i])
        path_l_list.append(path_l)
        path_l = 0
        print(Work_with_files.Write_log("Длина пути: " + str(path_l_list[i]) + " мм."))
    elif type_path == 3:
        print(Work_with_files.Write_log("Тип интерполяции - круговой. Задание окружности с помощью координат центра."))
        path_l = Path_length_calculator.path_circular_p (st_point[i], fn_point[i], cn_point[i], way_move[i])
        path_l_list.append(path_l)
        path_l = 0
        print(Work_with_files.Write_log("Длина пути: " + str(path_l_list[i]) + " мм."))
    else:
        print(Work_with_files.Write_log("Тип пути не определен."))

path_l_list[0] = 90
path_l_list[1] = 100
path_l_list[2] = 60
path_l_list.append(70)
"Генерация профиля ускорения и скорости."
print(Work_with_files.Write_log("Генерирование профиля скорости."))
times = []
for i in range (0,4):
    if feedr_n == len(feedrate)-1:
        print(Work_with_files.Write_log("Блок " + str(i+1) + ", последний."))
    else:
        print(Work_with_files.Write_log("Блок " + str(i+1) + "."))
    feedr_n = i
    time_periods = Block_type.Time_Generator_n_la(feedrate, feedr_n, path_l_list[i], max_acceleration, max_deceleration, vel_start)
    print(time_periods)
    times.append(time_periods)
    print(Work_with_files.Write_log("Время разгона: " + str(time_periods[0]) + " с."))
    print(Work_with_files.Write_log("Время постоянной скорости: " + str(time_periods[1]) + " с."))
    print(Work_with_files.Write_log("Время торможения: " + str(time_periods[2]) + " с."))
    #acc_profile = Profile_generation.Acceleration_profile(max_acceleration, time_periods[0], time_periods[1], time_periods[2], 0.05)
    #hole_temp_time_1.append(acc_profile[1])
    #hole_temp_acc.append(acc_profile[0])
    vel_profile = Profile_generation.Velocity_profile(max_acceleration, time_periods[0], time_periods[1], time_periods[2], 0.05, vel_start, feedrate[i])
    vel_start = vel_profile[2]
    print(Work_with_files.Write_log("Максимальная скорость на блоке: " + str(vel_profile[3]) + " мм/с."))
    hole_temp_time.append(vel_profile[1])
    hole_temp_vel.append(vel_profile[0])

hole_profile = Profile_generation.Generation_hole_profile(hole_temp_vel, hole_temp_time)
Graphs.Plotting_1(hole_profile[0], hole_profile[1], "Время", "Скорость", "Профиль скорости", "Скорость", times)
#hole_profile = Profile_generation.Generation_hole_profile(hole_temp_acc, hole_temp_time_1)
#Graphs.Plotting_1(hole_profile[0], hole_profile[1], "Время", "Ускорение", "Профиль ускорения", "Ускорение")
