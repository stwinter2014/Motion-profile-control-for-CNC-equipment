import Spline
import Profile_generation
import Path_length_calculator
import Block_type
import Graphs

"""Тело программы для расчета индивидуального сплайна и профиля скорости в угле"""
"Точки траектории"
start_p_1 = [0, 0, 0]
finish_p_1 = [11, 60, 0]
start_p_2 = [11, 60, 0]
finish_p_2 = [22, 0, 0]
"Степень точности обхода угла"
tolerance = 3
"Построение сплайна"
Axes_spline_list = Spline.Spline_3(start_p_1, finish_p_1, start_p_2, finish_p_2, tolerance)
"Построение графиков со сплайном и теоретической траекторией"
Graphs.Plotting_02(Axes_spline_list[0], Axes_spline_list[1], Axes_spline_list[3], Axes_spline_list[4],
                   "x", "y", "Bézier curve", "Spline", "Theoretic trajectory")

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

time = Block_type.Time_Generator_n_la(feedrate, 0, length_spline, acc, dec, vel)

time_list = []
time_list.append(time)
vel_profile = Profile_generation.Velocity_profile(acc, time[0], time[1], time[2], 0.05, vel, feedrate)
Graphs.Plotting_1(vel_profile[1], vel_profile[0], "Время", "Скорость", "Профиль скорости", "Скорость", time_list)

feedrate_spline = Spline.Corner_feedrate(feedrate[0], feedrate_nextblock, length_1, length_2, start_p_1, finish_p_1, start_p_2, finish_p_2, acc_axis)

print("Максимально возможная скорость на сплайне: " + str(feedrate_spline) + " мм/с.")
