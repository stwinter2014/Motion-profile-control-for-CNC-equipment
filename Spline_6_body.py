import Path_length_calculator
import Spline
import Graphs

"""Тело программы для расчета индивидуального сплайна и профиля скорости в угле"""
"Точки траектории"
start_p_1 = [0, 0, 0]
finish_p_1 = [11, 60, 0]
start_p_2 = [11, 60, 0]
finish_p_2 = [22, 0, 0]

#start_p_1 = [20, 10, 0]
#finish_p_1 = [60, 40, 0]
#start_p_2 = [60, 40, 0]
#finish_p_2 = [160, 40, 0]

x_p = []
y_p = []
x_p.append(start_p_1[0])
x_p.append(finish_p_1[0])
x_p.append(finish_p_2[0])
y_p.append(start_p_1[1])
y_p.append(finish_p_1[1])
y_p.append(finish_p_2[1])
feedrate = [5, 10]
"Степень точности обхода угла"
Lt = 3
n = 0.8
"Построение графиков со сплайном и теоретической траекторией"
Axes_spline = Spline.Spline_6(Lt, n, start_p_1, finish_p_1, start_p_2, finish_p_2)
Graphs.Plotting_02(Axes_spline[0], Axes_spline[1], x_p, y_p,
                   "Ось x", "Ось y", "Кривая Безье", "Истинная траектория", "Запрограммированная траектория")
Graphs.Plotting_02(Axes_spline[0], Axes_spline[1], Axes_spline[3], Axes_spline[4],
                   "Ось x", "Ось y", "Кривая Безье", "Истинная траектория", "Запрограммированная траектория")
"""l_1 = Path_length_calculator.Path_linear(start_p_1, finish_p_1)
l_2 = Path_length_calculator.Path_linear(start_p_2, finish_p_2)
print(l_1, l_2)
point_1 = Spline.Point_find(start_p_1, finish_p_1, Lt, 0)
point_2 = Spline.Point_find(start_p_2, finish_p_2, Lt, 1)
len_1 = Path_length_calculator.Path_linear(point_1, finish_p_1)
len_2 = Path_length_calculator.Path_linear(start_p_2, point_2)
print(len_1, len_2)
print(Spline.Corner_feedrate(feedrate[0], feedrate[1], Lt, Lt, point_1, finish_p_1, start_p_2, point_2, [5, 5, 5]))
print(Spline.Corner_feedrate(feedrate[0], feedrate[1], l_1, l_2, start_p_1, finish_p_1, start_p_2, finish_p_2, [5, 5, 5]))
"""
