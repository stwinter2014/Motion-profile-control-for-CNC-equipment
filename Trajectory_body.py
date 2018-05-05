import Work_with_files
import Path_length_calculator
import Trajectory_mapping
import Spline

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
feedrate = [10, 12, 8]
"Степень точности обработки углов"
tolerance_angle = [3,4,3]

"""Тело программы"""
Work_with_files.Clear_log()
"""Анализ траектории"""
print(Work_with_files.Write_log("Анализ велчиин подачи участков траектории"))
for i in range (len(feedrate)):
    print(Work_with_files.Write_log("Заданная величина подачи для блока " + str(i+1) + " равна " + str(feedrate[i]) + " мм/с."))
print("_________________")
"Подсчет длины участков траектории"
path_l_list = []
print(Work_with_files. Write_log("Анализ длины участков траектории"))
for i in range (len(st_point)):
    print(Work_with_files.Write_log("Подсчет длины пути блока " + str(i+1) + "."))
    print(Work_with_files.Write_log("Тип интерполяции - линейный."))
    path_l = Path_length_calculator.Path_linear(st_point[i], fn_point[i])
    path_l_list.append(path_l)
    path_l = 0
    print(Work_with_files.Write_log("Длина пути: " + str(path_l_list[i]) + " мм."))
print("_________________")
"Определение углов между участками траектории"
print(Work_with_files. Write_log("Анализ углов участков траектории"))
angles = Trajectory_mapping.Trajectory_analisys(st_point, fn_point)
for i in range (len(angles)):
    print(Work_with_files. Write_log(
        "Между участками " + str(i+1) + " и " + str (i+2) + " имеется угол в " + str(angles[i]) + " град."))
print("_________________")
"Построение траектории запрограммированной и истинной с учетом скругления углов"
Trajectory_mapping.Trajectory_mapping(st_point, fn_point, tolerance_angle)

