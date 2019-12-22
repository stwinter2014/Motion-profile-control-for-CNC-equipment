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
#feedrate = [25, 20, 30]
feedrate = [30]
#max_acceleration = [25, 25, 20]
#max_deceleration = [15, 25, 25]
max_acceleration = [15]
max_deceleration = [15]
time_periods = []

"""Данные о перемещении"""
path_l_list = []
path_l = 0
'''st_point = [[60, 20, 0],
            [140, 80, 0],
            [220, 80, 0]]
fn_point = [[140, 80, 0],
            [220, 80, 0],
            [270, 20, 0]]'''
st_point = [[20, 10, 0]]
#[60, 40, 0],
#[160, 40, 0],
#[170, 20, 0]]
fn_point = [[60, 40, 0]]
#[160, 40, 0],
#[170, 20, 0],
#[20, 10, 0]]
"Данные для задания окружностей"
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
for i in range (len(feedrate)):
    print(Work_with_files.Write_log("Подсчет длины пути блока " + str(i+1) + "."))
    type_path = Path_length_calculator.path_type(path_code[i])
    """Подсчет длины пути"""
    if type_path == 1:
        print(Work_with_files.Write_log("Тип интерполяции - линейный."))
        path_l = Path_length_calculator.Path_linear(st_point[i], fn_point[i])
        path_l_list.append(path_l)
        path_l = 0
        print(Work_with_files.Write_log("Длина пути: " + str(round(path_l_list[i], 3)) + " мм."))
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

"Генерация профиля ускорения и скорости."
print(Work_with_files.Write_log("Генерирование профиля скорости."))
times = []
for i in range (len(feedrate)):
    if  i == 0 and feedr_n == len(feedrate)-1:
        #print(Work_with_files.Write_log("Блок " + str(i+1) + ", единичный."))
        pass
    elif i != 0 and feedr_n == len(feedrate)-1:
        print(Work_with_files.Write_log("Блок " + str(i+1) + ", последний."))
    else:
        print(Work_with_files.Write_log("Блок " + str(i+1) + "."))
    feedr_n = i
    if i == 0:
        time_periods = Block_type.Time_Generator_lookahead_1(feedrate, feedr_n, path_l_list[i], max_acceleration[i], max_deceleration[i], vel_start,
                                                             max_acceleration[i], max_deceleration[i], max_acceleration[i+1], max_deceleration[i+1])
    elif i == 1:
        time_periods = Block_type.Time_Generator_lookahead_1(feedrate, feedr_n, path_l_list[i], max_acceleration[i], max_deceleration[i], vel_start,
                                                             max_acceleration[i-1], max_deceleration[i-1], max_acceleration[i+1], max_deceleration[i+1])
    elif i == 2:
        time_periods = Block_type.Time_Generator_lookahead_1(feedrate, feedr_n, path_l_list[i], max_acceleration[i], max_deceleration[i], vel_start,
                                                             max_acceleration[i-1], max_deceleration[i-1], max_acceleration[i], max_deceleration[i])
    times.append(time_periods)
    print(Work_with_files.Write_log("Время разгона: " + str(round(time_periods[0], 3)) + " с."))
    print(Work_with_files.Write_log("Время постоянной скорости: " + str(round(time_periods[1], 3)) + " с."))
    print(Work_with_files.Write_log("Время торможения: " + str(round(time_periods[2], 3)) + " с."))

    vel_profile = Profile_generation.Velocity_profile(max_acceleration[i], max_deceleration[i], time_periods[0], time_periods[1], time_periods[2], 0.05, vel_start, feedrate[i])
    vel_start = vel_profile[2]
    print(Work_with_files.Write_log("Максимальная скорость на блоке: " + str(vel_profile[3]) + " мм/с."))
    hole_temp_time.append(vel_profile[1])
    hole_temp_vel.append(vel_profile[0])
    print("Обработка блока ", i+1, " закончена.")
    print("______________________________________")
hole_profile = Profile_generation.Generation_hole_profile(hole_temp_vel, hole_temp_time)

"""Вывод результатов"""
"""Профиль скорости"""
"""Русский язык"""
#Graphs.Plotting_1(hole_profile[0], hole_profile[1], "Время, с", "Скорость, мм/с", "Профиль скорости", "Скорость", times)
"""English language"""
Graphs.Plotting_1(hole_profile[0], hole_profile[1], "Time, sec", "Velocity, mm/sec", "Velocity profile", "Velocity", times, "2Velocity2")

"""Профиль ускорения"""
"""Русский язык"""
#hole_profile = Profile_generation.Generation_hole_profile(hole_temp_acc, hole_temp_time_1)
#Graphs.Plotting_1(hole_profile[0], hole_profile[1], "Время", "Ускорение", "Профиль ускорения", "Ускорение")
