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

def Trajectory_analisys(start_points, finish_points):
    angle_list = []
    for i in range (len(start_points)-1):
        angle = Angle_calculator(start_points[i], finish_points[i], start_points[i+1], finish_points[i+1])
        angle_list.append(round(angle[0], 1))
    return angle_list

def Trajectory_mapping(start_points, finish_points, tolerance_list):
    x_points = []
    y_points = []
    spline = []
    spline_x = []
    spline_y = []
    for i in range (len(start_points)):
        x_points.append(start_points[i][0])
        x_points.append(finish_points[i][0])
        y_points.append(start_points[i][1])
        y_points.append(finish_points[i][1])
    spline_x.append(start_points[0][0])
    spline_y.append(start_points[0][1])
    for i in range (len(start_points)-1):
        spline = Spline.Spline(start_points[i], finish_points[i], start_points[i+1], finish_points[i+1], tolerance_list[i])
        for j in range (len(spline[0])):
            spline_x.append(spline[0][j])
            spline_y.append(spline[1][j])
    spline_x.append(finish_points[len(start_points)-1][0])
    spline_y.append(finish_points[len(finish_points)-1][1])
    Graphs.Plotting_02(spline_x, spline_y, x_points, y_points,
                       "Ось x", "Ось y", "Траектория инструмента", "Истинная траектория", "Запрограммированная траектория")
