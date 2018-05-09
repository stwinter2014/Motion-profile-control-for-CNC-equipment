import math
import Graphs
import Spline
import Path_length_calculator

"""Функция подсчета угла между участками траектории а и б.
На вход подается:
1. Стартовая точка траектории а в формате [x, y, z];
2. Конечная точка траектории а в формате [x, y, z];
2. Стартовая точка траектории б в формате [x, y, z];
3. Конечная точка траектории б в формате [x, y, z].
На выход подается список из двух занчений: [значение угла в град., значение угла в радианах].
"""
def Angle_calculator(start_point_last, finish_point_last, start_point_next, finish_point_next):
    length_last = Path_length_calculator.Path_linear(start_point_last, finish_point_last)
    length_next = Path_length_calculator.Path_linear(start_point_next, finish_point_next)
    length_between = Path_length_calculator.Path_linear(start_point_last, finish_point_next)
    gamma = math.acos((math.pow(length_next,2)+math.pow(length_last,2)-math.pow(length_between,2))/(2*length_last*length_next))
    acute_angle_1 = 180 - math.degrees(gamma)
    acute_angle_2 = math.pi - gamma
    return acute_angle_1, acute_angle_2

"""Функция анализа траектории: выявление углов между участками траектории.
На вход подается:
1. Список координат начальных точек в формате [x, y, z] в мм;
2. Список координат конечных точек в формате [x, y, z] в мм.
На выход подается:
1. Список углов между участками траектории в градусах.
"""
def Trajectory_analisys(start_points, finish_points):
    angle_list = []
    for i in range (len(start_points)-1):
        angle = Angle_calculator(start_points[i], finish_points[i], start_points[i+1], finish_points[i+1])
        angle_list.append(round(angle[0], 1))
    return angle_list

"""Функция построения траектории движения инструмента, истинной с учетом углов и запрограммированной.
На вход подается:
1. Список координат начальных точек в формате [x, y, z] в мм;
2. Список координат конечных точек в формате [x, y, z] в мм;
3. Список степеней точности обработки углов в мм.
На выход подается:
1. График, содержащий запрограммированную и истинную траектории инструмента.
"""
def Trajectory_mapping(start_points, finish_points, tolerance_list, ratio_list, optimal_ratio_list, optimal_agree):
    x_points = []
    y_points = []
    spline = []
    spline_x = []
    spline_y = []
    spline_x_out = []
    spline_y_out = []
    spline_z_out = []
    for i in range (len(start_points)):
        x_points.append(start_points[i][0])
        x_points.append(finish_points[i][0])
        y_points.append(start_points[i][1])
        y_points.append(finish_points[i][1])
    spline_x.append(start_points[0][0])
    spline_y.append(start_points[0][1])
    for i in range (len(start_points)-1):
        if optimal_agree[i] == 1:
            spline = Spline.Spline_6(tolerance_list[i], optimal_ratio_list[i], start_points[i], finish_points[i], start_points[i+1], finish_points[i+1])
        elif optimal_agree[i] == 0:
            spline = Spline.Spline_6(tolerance_list[i], ratio_list[i], start_points[i], finish_points[i], start_points[i+1], finish_points[i+1])
        spline_x_out.append(spline[0])
        spline_y_out.append(spline[1])
        spline_z_out.append(spline[2])
        Graphs.Plotting_02(spline[0], spline[1], spline[3], spline[4],
                           "Ось x, мм", "Ось y, мм", "Траектория инструмента в углу " + str(i+1), "Истинная траектория", "Запрограммированная траектория")
        for j in range (len(spline[0])):
            spline_x.append(spline[0][j])
            spline_y.append(spline[1][j])
    spline_x.append(finish_points[len(start_points)-1][0])
    spline_y.append(finish_points[len(finish_points)-1][1])
    Graphs.Plotting_02(spline_x, spline_y, x_points, y_points, 
                       "Ось x, мм", "Ось y, мм", "Траектория инструмента", "Истинная траектория", "Запрограммированная траектория")
    return spline_x_out, spline_y_out, spline_z_out
