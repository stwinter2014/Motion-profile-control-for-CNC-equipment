import Spline
import Graphs

"""Тело программы для расчета индивидуального сплайна и профиля скорости в угле"""
"Точки траектории"
start_p_1 = [0, 0, 0]
finish_p_1 = [11, 60, 0]
start_p_2 = [11, 60, 0]
finish_p_2 = [22, 0, 0]
x_p = []
y_p = []
x_p.append(start_p_1[0])
x_p.append(finish_p_1[0])
x_p.append(finish_p_2[0])
y_p.append(start_p_1[1])
y_p.append(finish_p_1[1])
y_p.append(finish_p_2[1])

"Степень точности обхода угла"
Lt = 5
n = 0.3
"Построение графиков со сплайном и теоретической траекторией"
Axes_spline = Spline.Spline_6(Lt, n, start_p_1, finish_p_1, start_p_2, finish_p_2)
Graphs.Plotting_02(Axes_spline[0], Axes_spline[1], x_p, y_p,
                   "Ось x", "Ось y", "Кривая Безье", "Истинная траектория", "Запрограммированная траектория")
Graphs.Plotting_02(Axes_spline[0], Axes_spline[1], Axes_spline[3], Axes_spline[4],
                   "Ось x", "Ось y", "Кривая Безье", "Истинная траектория", "Запрограммированная траектория")
