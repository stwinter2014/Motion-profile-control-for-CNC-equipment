import Path_length_calculator
import Trajectory_mapping
import Spline
import Graphs

"""Тело программы для расчета индивидуального сплайна и профиля скорости в угле"""
"Точки траектории"
start_p_1 = [20, 10, 0]
finish_p_1 = [42.361, 30, 0]
start_p_2 = [42.361, 30, 0]
finish_p_2 = [64.721, 10, 0]

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
feedrate = [25, 30]
"Степень точности обхода угла"
Lt = 2
n = 0.3
d = Lt/(2*n+1)
c = n*d
e = ((7*n+16))/32*d
print("с = " + str(c))
print("d = " + str(d))
print("e = " + str(e))

"Построение графиков со сплайном и теоретической траекторией"
Axes_spline = Spline.Spline_6(Lt, n, start_p_1, finish_p_1, start_p_2, finish_p_2)
cord_x = []
cord_y = []
#Расчет ошибки обработки напрямую.
cord_05 = []
cord_05.append(Axes_spline[6])
cord_05.append(Axes_spline[7])
cord_05.append(Axes_spline[8])
epsilon = Path_length_calculator.Path_linear(cord_05, finish_p_1)
LEN = len(Axes_spline[0])
print('LEN = ', LEN)
cord_x.append(Axes_spline[6])
cord_x.append(finish_p_1[0])
cord_y.append(Axes_spline[7])
cord_y.append(finish_p_1[1])
print("e = " + str(epsilon))
spline_x = []
spline_y = []
spline_x.append(start_p_1[0])
for i in range (len(Axes_spline[0])):
    spline_x.append(Axes_spline[0][i])
spline_x.append(finish_p_2[0])
spline_y.append(start_p_1[1])
for i in range (len(Axes_spline[1])):
    spline_y.append(Axes_spline[1][i])
spline_y.append(finish_p_2[1])

Graphs.Plotting_02(spline_x, spline_y, x_p, y_p,
                   "Ось x, мм", "Ось y, мм", "Кривая Безье", "Истинная траектория", "Запрограммированная траектория")
"""Русский язык"""
#Graphs.Plotting_02(Axes_spline[0], Axes_spline[1], Axes_spline[3], Axes_spline[4],
                   #"Ось x, мм", "Ось y, мм", "Кривая Безье", "Истинная траектория", "Запрограммированная траектория")

"""English language"""
Graphs.Plotting_02(Axes_spline[0], Axes_spline[1], Axes_spline[3], Axes_spline[4],
                   "X, mm", "Y, mm", "Bezier Curve", "Final trajectory", "Programmed trajectory")


#Graphs.Plotting_03(Axes_spline[0], Axes_spline[1], Axes_spline[3], Axes_spline[4], cord_x, cord_y,
                   #"Ось x", "Ось y", "Кривая Безье", "Истинная траектория", "Запрограммированная траектория", "da")
#Graphs.Plotting_22(spline_x, spline_y, x_p, y_p, Axes_spline[0], Axes_spline[1], Axes_spline[3], Axes_spline[4],
                   #"Ось x, мм", "Ось y, мм", "Траектория инструмента с кривой Безье", "Кривая Безье", "Истинная траектория",
                   #"Запрограммированная траектория")


l_1 = Path_length_calculator.Path_linear(start_p_1, finish_p_1)
l_2 = Path_length_calculator.Path_linear(start_p_2, finish_p_2)
#print(l_1, l_2)
point_1 = Spline.Point_find(start_p_1, finish_p_1, Lt, 0)
point_2 = Spline.Point_find(start_p_2, finish_p_2, Lt, 1)
len_1 = Path_length_calculator.Path_linear(point_1, finish_p_1)
len_2 = Path_length_calculator.Path_linear(start_p_2, point_2)
#print(len_1, len_2)
#print(Spline.Corner_feedrate(feedrate[0], feedrate[1], Lt, Lt, point_1, finish_p_1, start_p_2, point_2, [25, 25, 25]))
corner_feedrate = Spline.Corner_feedrate(feedrate[0], feedrate[1], l_1, l_2, start_p_1, finish_p_1, start_p_2, finish_p_2, [25, 25, 25])
print("Участок 1.")
print("Подача на участке 1 равна " + str(feedrate[0]) + " мм/с.")
print("Длина участка 1 равна " + str(round(l_1, 3)) + " мм.")
print("Участок 2.")
print("Подача на участке 2 равна " + str(feedrate[1]) + " мм/с.")
print("Длина участка 1 равна " + str(round(l_2, 2)) + " мм.")
print("Угол между участками равен " + str(round(Trajectory_mapping.Angle_calculator(start_p_1, finish_p_1, start_p_2, finish_p_2)[0], 3)) + " град.")
print("Максимально допустимая скорость на углу равна " + str(corner_feedrate) + " мм/с.")
