import math
import Work_with_files
import Path_length_calculator
import Trajectory_mapping
import Spline
import Block_type
import Profile_generation
import Graphs

"""Исходные данные траектории"""
"Начальные и конечные точки"
st_point = [[20, 10, 0],
            [60, 40, 0],
            [160, 40, 0],
            [170, 20, 0]]
fn_point = [[60, 40, 0],
            [160, 40, 0],
            [170, 20, 0],
            [20, 10, 0]]
"Величины подачи для каждого участка траектории"
feedrate_input = [15, 10, 8, 10]
"Допустимое ускорение"
max_acceleration = 5
max_deceleration = 5
"Степень точности обработки углов"
tolerance_angle = [3, 3, 3]
ratio = [0.9, 0.8, 0.8]
optimal_ratio = []
optimal_agree_list = [0, 0, 0]

"""Тело программы"""
Work_with_files.Clear_log()
"""Анализ траектории"""
print(Work_with_files.Write_log("Анализ величин подачи участков траектории."))
for i in range (len(feedrate_input)):
    print(Work_with_files.Write_log("Заданная величина подачи для блока " + str(i+1) + " равна " + str(feedrate_input[i]) + " мм/с."))
print("_________________")
"Подсчет длины участков траектории"
path_l_list = []
print(Work_with_files.Write_log("Анализ длины участков траектории."))
for i in range (len(st_point)):
    print(Work_with_files.Write_log("Подсчет длины пути блока " + str(i+1) + "."))
    print(Work_with_files.Write_log("Тип интерполяции - линейный."))
    path_l = Path_length_calculator.Path_linear(st_point[i], fn_point[i])
    path_l_list.append(path_l)
    path_l = 0
    print(Work_with_files.Write_log("Длина пути: " + str(round(path_l_list[i], 4)) + " мм."))
print("_________________")
"Определение углов между участками траектории"
print(Work_with_files.Write_log("Анализ углов участков траектории."))
angles = Trajectory_mapping.Trajectory_analisys(st_point, fn_point)
for i in range (len(angles)):
    print(Work_with_files.Write_log(
        "Между участками " + str(i+1) + " и " + str (i+2) + " имеется угол в " + str(angles[i]) + " град."))
    
    optimal_ratio.append(round(1/(2.0769)*math.pow(math.radians(angles[i]), 0.9927), 2))
    print(Work_with_files.Write_log("Оптимальное отношение сторон c и d равно " + str(optimal_ratio[i]) + "."))
"Построение траектории запрограммированной и истинной с учетом скругления углов"
spline_coord = Trajectory_mapping.Trajectory_mapping(st_point, fn_point, tolerance_angle, ratio, optimal_ratio, optimal_agree_list)
print("_________________")
print(Work_with_files.Write_log("Анализ допустимой скорости в углах."))
length_angles_list = []
for i in range (len(spline_coord[0])):
    length_angles = Spline.Spline_length(spline_coord[0][i], spline_coord[1][i], spline_coord[2][i])
    length_angles_list.append(length_angles)
    print(Work_with_files.Write_log(
        "Длина пути на углу между " + str(i+1) + " и " + str(i+2) + " блоками равна " + str(round(length_angles, 4)) + " мм."))
"Подсчет допустимой скорости в углах."
feedrate_angles_list = []
for i in range (len(length_angles_list)):
    feedrate_angles = Spline.Corner_feedrate(feedrate_input[i], feedrate_input[i+1], path_l_list[i], path_l_list[i+1],
                                      st_point[i], fn_point[i], st_point[i+1], fn_point[i+1], [max_acceleration, max_acceleration, max_acceleration])
    feedrate_angles_list.append(feedrate_angles)
    print(Work_with_files.Write_log(
        "Максимальная допустимая скорость на углу между " + str(i+1) + " и " + str(i+2) + " блоками равна " + str(feedrate_angles) + " мм/с."))
print("_________________")
print(Work_with_files.Write_log("Анализ длины участков траектории с учетом сгругления углов."))
for i in range (len(path_l_list)):
    if i == 0:
        path_l_list[i] = path_l_list[i]- tolerance_angle[i]
    elif i == len(path_l_list)-1:
        path_l_list[i] = path_l_list[i]- tolerance_angle[i-1]
    else:
        path_l_list[i] = path_l_list[i]- tolerance_angle[i] - tolerance_angle[i-1]
    print(Work_with_files.Write_log("Длина пути с учетом скругления угла: " + str(round(path_l_list[i], 4)) + " мм."))
path_list = []
feedrate_list = []
for i in range (len(path_l_list)-1):
    path_list.append(path_l_list[i])
    path_list.append(length_angles_list[i])
    feedrate_list.append(feedrate_input[i])
    feedrate_list.append(feedrate_angles_list[i])
path_list.append(path_l_list[3])
feedrate_list.append(feedrate_input[3])
print("_________________")
"Генерация профилей ускорения и скорости"
print(Work_with_files.Write_log("Генерирование профиля скорости."))
times = []
feedrate_number = 0
vel_start = 0
acc_start = 0
jerk_start = 0
hole_temp_time = []
hole_temp_time_1 = []
hole_temp_time_2 = []
hole_temp_acc = []
hole_temp_vel = []
hole_temp_jerk = []
time_interpolation = 0.0025
for i in range (len(feedrate_list)):
    if  i == 0 and feedrate_number == len(feedrate_list)-1:
        print(Work_with_files.Write_log("Блок " + str(i+1) + ", единичный."))
    elif i != 0 and feedrate_number == len(feedrate_list)-1:
        print(Work_with_files.Write_log("Блок " + str(i+1) + ", последний."))
    elif i%2 == 0:
        print(Work_with_files.Write_log("Блок " + str(int(i/2+1)) + "."))
    elif i%2 != 0:
        print(Work_with_files.Write_log("Обработка угла между блоками " + str(int(i/2+1)) + " и " + str(int(i/2+2))))
    feedrate_number = i
    time_periods = Block_type.Time_Generator_la_withangles(feedrate_list, feedrate_number, path_list[i], max_acceleration, max_deceleration, vel_start)
    times.append(time_periods)
    print(Work_with_files.Write_log("Время разгона: " + str(round(time_periods[0], 3)) + " с."))
    print(Work_with_files.Write_log("Время постоянной скорости: " + str(round(time_periods[1], 3)) + " с."))
    print(Work_with_files.Write_log("Время торможения: " + str(round(time_periods[2], 3)) + " с."))
    "Профиль ускорения"
    acc_profile = Profile_generation.Acceleration_profile(max_acceleration, time_periods[0], time_periods[1], time_periods[2], time_interpolation, acc_start)
    acc_start = acc_profile[2]
    hole_temp_time_1.append(acc_profile[1])
    hole_temp_acc.append(acc_profile[0])
    "Профиль скорости"
    vel_profile = Profile_generation.Velocity_profile(max_acceleration, time_periods[0], time_periods[1],
                                                      time_periods[2], time_interpolation, vel_start, feedrate_list[i])
    vel_start = vel_profile[2]
    if i%2 == 0:
        print(Work_with_files.Write_log("Максимальная скорость на блоке: " + str(vel_profile[3]) + " мм/с."))
    elif i%2 != 0:
        print(Work_with_files.Write_log("Максимальная скорость на углу: " + str(vel_profile[3]) + " мм/с."))
    hole_temp_time.append(vel_profile[1])
    hole_temp_vel.append(vel_profile[0])
    "Профиль толчка"
    jerk_profile = Profile_generation.Jerk_profile(max_acceleration, time_periods[0], time_periods[1], time_periods[2], time_interpolation, jerk_start)
    jerk_start = jerk_profile[2]
    hole_temp_time_2.append(jerk_profile[1])
    hole_temp_jerk.append(jerk_profile[0])

"Построение графиков профиля скорости/ускорения"
hole_profile_1 = Profile_generation.Generation_hole_profile(hole_temp_vel, hole_temp_time)
Graphs.Plotting_1(hole_profile_1[0], hole_profile_1[1], "Время, с", "Скорость, мм/с", "Профиль скорости", "Скорость инструмента", times)
hole_profile_2 = Profile_generation.Generation_hole_profile(hole_temp_acc, hole_temp_time_1)
Graphs.Plotting_1(hole_profile_2[0], hole_profile_2[1], "Время, с", "Ускорение, мм/с2", "Профиль ускорения", "Ускорение инструмента", times)
#hole_profile_3 = Profile_generation.Generation_hole_profile(hole_temp_jerk, hole_temp_time_2)
#Graphs.Plotting_1(hole_profile_3[0], hole_profile_3[1], "Время", "Ускорение", "Профиль ускорения", "Ускорение", times)
Graphs.Plotting_2(hole_profile_1[0], hole_profile_1[1], hole_profile_2[0], hole_profile_2[1],
                  "Время, с", "Скорость, мм/с", "Ускорение, мм/с^2", "Профиль скорости", "Профиль ускорения")
