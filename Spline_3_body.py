import Spline
import Profile_generation
import Path_length_calculator
import Block_type
import Graphs

"""Тело программы для расчета индивидуального сплайна и профиля скорости в угле"""
"Точки траектории"
start_p_1 = [20, 10, 0]
finish_p_1 = [42.361, 30, 0]
start_p_2 = [42.361, 30, 0]
finish_p_2 = [64.721, 10, 0]
"Степень точности обхода угла"
tolerance = 2
"Построение сплайна"
Axes_spline_list = Spline.Spline_3(start_p_1, finish_p_1, start_p_2, finish_p_2, tolerance)
"Построение графиков со сплайном и теоретической траекторией"
x_hole = []
x_hole.append(start_p_1[0])
x_hole.append(finish_p_1[0])
x_hole.append(finish_p_2[0])
y_hole = []
y_hole.append(start_p_1[1])
y_hole.append(finish_p_1[1])
y_hole.append(finish_p_2[1])
z_hole = []
z_hole.append(start_p_1[2])
z_hole.append(finish_p_1[2])
z_hole.append(finish_p_2[2])

"""Русский язык"""
Graphs.Plotting_02(Axes_spline_list[0], Axes_spline_list[1], Axes_spline_list[3], Axes_spline_list[4],
                   "Ось x, мм", "Ось y, мм", "a) Bezier curve with Lt = 2 mm, n = 0.9", "Реальная траектория", "Запрограммированная траектория", '51underline')
"""English language"""
Graphs.Plotting_02(Axes_spline_list[0], Axes_spline_list[1], Axes_spline_list[3], Axes_spline_list[4],
                   "X, mm", "Y, mm", "Bezier curve", "Final trajectory", "Programmed trajectory", '4spline3big2')

result_spline_x = []
result_spline_x.append(start_p_1[0])
for i in range (len(Axes_spline_list[0])):
    result_spline_x.append(Axes_spline_list[0][i])
result_spline_x.append(finish_p_2[0])

result_spline_y = []
result_spline_y.append(start_p_1[1])
for i in range (len(Axes_spline_list[1])):
    result_spline_y.append(Axes_spline_list[1][i])
result_spline_y.append(finish_p_2[1])

"""Русский язык"""
#Graphs.Plotting_02(result_spline_x, result_spline_y, x_hole, y_hole,
#                   "Ось x, мм", "Ось y, мм", "Кривая Безье", "Реальная траектория", "Запрограммированная траектория")
"""English language"""
Graphs.Plotting_02(result_spline_x, result_spline_y, x_hole, y_hole,
                   "X, mm", "Y, mm", "Bezier curve", "Final trajectory", "Programmed trajectory", '4spline3small2')

"Получение длины пути по траектории сплайна"
length_spline = Spline.Spline_length(Axes_spline_list[0], Axes_spline_list[1], Axes_spline_list[2])
print("Длина пути на сплайне: " + str(round(length_spline, 3)) + " мм.")
feedrate = [10]
feedrate_nextblock = 5
length_1 = 90
length_2 = 100
acc = 5
acc_axis = [5, 5, 5]
dec = 5
vel = 0
time = []
"""
time = Block_type.Time_Generator_n_la(feedrate, 0, length_spline, acc, dec, vel)

time_list = []
time_list.append(time)
vel_profile = Profile_generation.Velocity_profile(acc, time[0], time[1], time[2], 0.05, vel, feedrate)
Graphs.Plotting_1(vel_profile[1], vel_profile[0], "Время", "Скорость", "Профиль скорости", "Скорость", time_list)

feedrate_spline = Spline.Corner_feedrate(feedrate[0], feedrate_nextblock, length_1, length_2, start_p_1, finish_p_1, start_p_2, finish_p_2, acc_axis)

print("Максимально возможная скорость на сплайне: " + str(feedrate_spline) + " мм/с.")
"""
