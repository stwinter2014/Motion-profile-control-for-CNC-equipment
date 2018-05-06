import math
import Path_length_calculator
import Graphs
import Block_type
import Profile_generation

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
    length = Path_length_calculator.Path_linear(start_point, finish_point)
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
def Spline_3_generator(start_point, transition_point, end_point):
    frst_length = Path_length_calculator.Path_linear(start_point, transition_point)
    scnd_length = Path_length_calculator.Path_linear(transition_point, end_point)
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

def Spline_6(spline_tolerance, ratio, start_point_1, finish_point_1, start_point_2, finish_point_2):
    x_coord = []
    y_coord = []
    z_coord = []
    x_trajectory = []
    y_trajectory = []
    z_trajectory = []
    d = spline_tolerance/(2*ratio+1)
    cd = d + ratio*d
    t = 0
    point_1 = Point_find(start_point_1, finish_point_1, spline_tolerance, 0)
    point_6 = Point_find(start_point_2, finish_point_2, spline_tolerance, 1)
    point_2 = Point_find(start_point_1, finish_point_1, cd, 0)
    point_3 = Point_find(start_point_1, finish_point_1, d, 0)
    point_4 = Point_find(start_point_2, finish_point_2, d, 1)
    point_5 = Point_find(start_point_2, finish_point_2, cd, 1)
    x_trajectory.append(point_1[0])
    x_trajectory.append(finish_point_1[0])
    x_trajectory.append(point_6[0])
    y_trajectory.append(point_1[1])
    y_trajectory.append(finish_point_1[1])
    y_trajectory.append(point_6[1])
    z_trajectory.append(point_1[2])
    z_trajectory.append(finish_point_1[2])
    z_trajectory.append(point_6[2])
    while t >= 0 and t <= 1:
        x = math.pow((1-t), 5)*point_1[0] + 5*t*math.pow((1-t), 4)*point_2[0] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[0] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[0] + 5*math.pow(t, 4)*(1-t)*point_5[0] + math.pow(t, 5)*point_6[0]
        y = math.pow((1-t), 5)*point_1[1] + 5*t*math.pow((1-t), 4)*point_2[1] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[1] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[1] + 5*math.pow(t, 4)*(1-t)*point_5[1] + math.pow(t, 5)*point_6[1]
        z = math.pow((1-t), 5)*point_1[2] + 5*t*math.pow((1-t), 4)*point_2[2] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[2] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[2] + 5*math.pow(t, 4)*(1-t)*point_5[2] + math.pow(t, 5)*point_6[2]
        x_coord.append(x)
        y_coord.append(y)
        z_coord.append(z)
        t += 0.05
        t = round(t,2)
    return x_coord, y_coord, z_coord, x_trajectory, y_trajectory, z_trajectory

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
def Spline_3(start_point_1, finish_point_1, start_point_2, finish_point_2, spline_tolerance):
    if finish_point_1 != start_point_2:
        print("Участки траеткории не соединены.")
        return 0,0,0,0
    else:
        spline_x = []
        spline_y = []
        x_coord = []
        y_coord = []
        z_coord = []
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
        coord = Spline_3_generator(start_spline, trans_p, finish_spline)
        for i in range (len(coord)):
            x_coord.append(coord[i][0])
            y_coord.append(coord[i][1])
            z_coord.append(0)
        return x_coord, y_coord, z_coord, spline_x, spline_y

"""Функция для расчета максимальной скорости в углах.
На вход подается:
1. Величина подачи блока 1 в мм/с;
2. Величина подачи блока 2 в мм/с;
3. Длина пути блока 1 в мм;
4. Длина пути блока 2 в мм;
5. Начальная точка траектории блока 1 в формате [x, y, z] мм;
6. Конечная точка траектории блока 1 в формате [x, y, z] мм;
7. Начальная точка траектории блока 2 в формате [x, y, z] мм;
8. Конечная точка траектории блока 2 в формате [x, y, z] мм;
9. Список максимально возможных ускорений для каждой из осей x, y, z в мм/с^2.
На выход подается:
1. Максимально возможная скорость при обработке угла между блоками 1 и 2 в мм/с.
"""
def Corner_feedrate(feedrate_1, feedrate_2, length_1, length_2, start_point_1, finish_point_1, start_point_2, finish_point_2, acc):
    delta_list = []
    Vx1 = feedrate_1*((finish_point_1[0]-start_point_1[0])/length_1)
    Vy1 = feedrate_1*((finish_point_1[1]-start_point_1[1])/length_1)
    Vx2 = feedrate_2*((finish_point_2[0]-start_point_2[0])/length_2)
    Vy2 = feedrate_2*((finish_point_2[1]-start_point_2[1])/length_2)
    deltaVx = math.fabs(Vx2 - Vx1)
    deltaVy = math.fabs(Vy2 - Vy1)
    delta_list.append(acc[0]/deltaVx)
    delta_list.append(acc[1]/deltaVy)
    Q = min(delta_list)
    if Q >= 1:
        feedrate_angle = feedrate_1
    else:
        feedrate_angle = round(feedrate_1*Q, 3)
    return feedrate_angle

"""Функция подсчета длины траектории на сглаженном углу (сплайне).
На вход подается:
1. Список координат x сплайна в мм;
2. Список координат y сплайна в мм;
3. Список координат z сплайна в мм.
На выход подается:
1. Длина траектории на сглаженном углу (сплайне) в мм.
"""
def Spline_length(spline_coord_x, spline_coord_y, spline_coord_z):
    point_instant_1 = []
    point_instant_2 = []
    length_spline = 0
    for i in range (len(spline_coord_x)-1):
        point_instant_1.append(spline_coord_x[i])
        point_instant_1.append(spline_coord_y[i])
        point_instant_1.append(spline_coord_z[i])
        point_instant_2.append(spline_coord_x[i+1])
        point_instant_2.append(spline_coord_y[i+1])
        point_instant_2.append(spline_coord_z[i+1])
        length_spline += Path_length_calculator.Path_linear(point_instant_1, point_instant_2)
        point_instant_1 = []
        point_instant_2 = []
    return length_spline
