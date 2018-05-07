import Work_with_files
import Path_length_calculator
import Trajectory_mapping
import Spline
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
feedrate_input = [10, 12, 8, 10]
"Допустимое ускорение"
max_acceleration = 5
max_deceleration = 5
"Степень точности обработки углов"
tolerance_angle = [3, 3, 3]
ratio = [0.9, 0.8, 0.8]

"""Тело программы"""
Work_with_files.Clear_log()
"""Анализ траектории"""
print(Work_with_files.Write_log("Анализ величин подачи участков траектории"))
for i in range (len(feedrate_input)):
    print(Work_with_files.Write_log("Заданная величина подачи для блока " + str(i+1) + " равна " + str(feedrate_input[i]) + " мм/с."))
print("_________________")
"Подсчет длины участков траектории"
path_l_list = []
print(Work_with_files.Write_log("Анализ длины участков траектории"))
for i in range (len(st_point)):
    print(Work_with_files.Write_log("Подсчет длины пути блока " + str(i+1) + "."))
    print(Work_with_files.Write_log("Тип интерполяции - линейный."))
    path_l = Path_length_calculator.Path_linear(st_point[i], fn_point[i])
    path_l_list.append(path_l)
    path_l = 0
    print(Work_with_files.Write_log("Длина пути: " + str(round(path_l_list[i], 4)) + " мм."))
print("_________________")
"Определение углов между участками траектории"
print(Work_with_files.Write_log("Анализ углов участков траектории"))
angles = Trajectory_mapping.Trajectory_analisys(st_point, fn_point)
for i in range (len(angles)):
    print(Work_with_files.Write_log(
        "Между участками " + str(i+1) + " и " + str (i+2) + " имеется угол в " + str(angles[i]) + " град."))
"Построение траектории запрограммированной и истинной с учетом скругления углов"
spline_coord = Trajectory_mapping.Trajectory_mapping(st_point, fn_point, tolerance_angle, ratio)
print("_________________")
print(Work_with_files.Write_log("Анализ допустимой скорости в углах"))
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
print("_________________")
