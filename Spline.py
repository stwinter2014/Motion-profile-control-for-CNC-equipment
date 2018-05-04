import math
import Path_length_calculator
import Graphs

"""Функция определяет координаты точки на заданой линии.
На вход подается:
1. Начальная точка пути в формате [x, y, z];
2. Конечная точка пути в формате [x, y, z];
3. Длина участка в мм;
4. Код направления откладывания отрезка (0 - от конечной точки, 1 - от начальной точки).
На выход подается:
1. Координаты искомой точки в формате [x, y, z].
"""
def Point_find (start_point, finish_point, length_part, way_to_search):
    length = Path_length_calculator.path_linear(start_point, finish_point)
    k = length_part/length
    z_p = 0
    if way_to_search == 0:
        x_p = finish_point[0] - (finish_point[0]- start_point[0])*k
        y_p = finish_point[1] - (finish_point[1]- start_point[1])*k
    elif way_to_search == 1:
        x_p = start_point[0] + (finish_point[0]- start_point[0])*k
        y_p = start_point[1] + (finish_point[1]- start_point[1])*k
    return x_p, y_p, z_p

"""Функция построения кривой Безье.
На вход подается:
1. Начальная точка построения сплайна в формате [x, y, z];
2. Транзитная точка (точка пересечения двух отрезков траектории) в формате [x, y, z];
2. Конечная точка построения сплайна в формате [x, y, z];
На выход подается:
1. Список точек кривой Безье в формате [x, y, z];
"""
def Spline_generator(start_point, transition_point, end_point):
    frst_length = Path_length_calculator.path_linear(start_point, transition_point)
    scnd_length = Path_length_calculator.path_linear(transition_point, end_point)
    spline_coord = []
    spline_coord_temp = []
    t = 0
    while t >= 0 and t <= 1:
        x = math.pow((1-t), 2)*start_point[0] + 2*(1-t)*t*transition_point[0] + math.pow(t, 2)*end_point[0]
        spline_coord_temp.append(x)
        y = math.pow((1-t), 2)*start_point[1] + 2*(1-t)*t*transition_point[1] + math.pow(t, 2)*end_point[1]
        spline_coord_temp.append(y)
        spline_coord_temp.append(0)
        spline_coord.append(spline_coord_temp)
        spline_coord_temp = []
        t += 0.05
        t = round(t,2)
    return spline_coord

"""
Функция создания кривой Безье.
На вход подается:
1. Начальная точка первого участка траектории в формате [x, y, z];
2. Конечная точка первого участка траектории в формате [x, y, z];
3. Начальная точка второго участка траектории в формате [x, y, z];
4. Конечная точка второго участка траектории в формате [x, y, z];
5. Степень точности обхода угла (Расстояние от начала сплайна до общей точки траектории) в мм.
На выход подается:
1. Список координат x кривой Безье;
2. Список координат y кривой Безье;
3. Список координат x теоретической траектории;
4. Список координат y теоретической траектории."""
def Spline (start_point_1, finish_point_1, start_point_2, finish_point_2, spline_tolerance):
    if finish_point_1 != start_point_2:
        print("Участки траеткории не соединены.")
        return 0,0,0,0
    else:
        spline_x = []
        spline_y = []
        x_coord = []
        y_coord = []
        trans_p = finish_point_1
        line_x = []
        line_y = []
        line_x.append(start_point_1[0])
        line_x.append(trans_p[0])
        line_x.append(finish_point_2[0])
        line_y.append(start_point_1[1])
        line_y.append(trans_p[1])
        line_y.append(finish_point_2[1])
        start_spline = Point_find(start_point_1, trans_p, spline_tolerance, 0)
        finish_spline = Point_find(trans_p, finish_point_2, spline_tolerance, 1)
        spline_x.append(start_spline[0])
        spline_x.append(trans_p[0])
        spline_x.append(finish_spline[0])
        spline_y.append(start_spline[1])
        spline_y.append(trans_p[1])
        spline_y.append(finish_spline[1])
        coord = Spline_generator(start_spline, trans_p, finish_spline)
        for i in range (len(coord)):
            x_coord.append(coord[i][0])
            y_coord.append(coord[i][1])
        return x_coord, y_coord, spline_x, spline_y

"""Тело программы"""
"Точки траеткории"
start_p_1 = [0, 0, 0]
finish_p_1 = [11, 60, 0]
start_p_2 = [11, 61, 0]
finish_p_2 = [22, 0, 0]
"Степень точности обхода угла"
tolerance = 3
"Построение сплайна"
Axes_spline_list = Spline(start_p_1, finish_p_1, start_p_2, finish_p_2, tolerance)
"Построение графиков со сплайном и теоретической траекторией"
Graphs.Plotting_02(Axes_spline_list[0], Axes_spline_list[1], Axes_spline_list[2], Axes_spline_list[3],
                   "x", "y", "Bézier curve", "Spline", "Theoretic trajectory")
