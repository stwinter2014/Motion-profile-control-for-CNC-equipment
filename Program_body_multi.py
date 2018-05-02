import Path_length_calculator
import Block_type
import Profile_generation
import Graphs
import math
"""Коды типов G-инструкций:
001 - G00;
010 - G01;
011 - G02 + радиус;
100 - G03 + радиус;
101 - G02 + координаты центра;
110 - G03 + координаты центра.
"""

"""Тело программы"""
path_code = ["010", "010", "010"]

"""Данные об обработке"""
feedrate = [10, 8, 12]
max_acceleration = 5
max_deceleration = 5
time_periods = []

"""Данные о перемещении"""
path_l = 0
st_point = [8.956,0,26.437]
fn_point = [79.616,0,90.494]
cn_point = [79.616,0,19.494]
rad = 71
way_move = 1

"""Определение типа пути (линейный или круговой, тип задания окружности)"""
path_l_list = []
time_list = []
time_x_list = []
acc_list = []
vel_list = []
for i in range (0,3):
    print("Обработка блока " + str(i+1) + ".")
    type_path = Path_length_calculator.path_type(path_code[i])
    """Подсчет длины пути"""
    if type_path == 1:
        print("Тип интерполяции - линейный.")
        path_l = Path_length_calculator.path_linear(st_point, fn_point)
        path_l_list.append(path_l)
        path_l = 0
        print("Длина пути: ", path_l_list[i])
    elif type_path == 2:
        print("Тип интерполяции - круговой. Задание окружности с помощью радиуса.")
        path_l = Path_length_calculator.path_circular_r (st_point, fn_point, rad, way_move)
        path_l_list.append(path_l)
        path_l = 0
        print("Длина пути: ", path_l_list[i])
    elif type_path == 3:
        print("Тип интерполяции - круговой. Задание окружности с помощью координат центра.")
        path_l = Path_length_calculator.path_circular_p (st_point, fn_point, cn_point, way_move)
        path_l_list.append(path_l)
        path_l = 0
        print("Длина пути: ", path_l_list[i])
    else:
        print("Тип пути не определен.")

    """Проверка типа блока (обычный или короткий)"""
    type_block = Block_type.block_t_check(path_l_list[i], feedrate[i], max_acceleration, max_deceleration)
    if type_block[0] == 1:
        print("Тип блока - обычный")
        time_periods = Block_type.Time_Generator_n(feedrate[i], path_l_list[i], max_acceleration, max_deceleration)
        time_list.append(time_periods)
        print("Время разгона: ", time_list[i][0])
        print("Время постоянной скорости: ", time_list[i][1])
        print("Время торможения: ", time_list[i][2])
        acc_profile = Profile_generation.Acceleration_profile(max_acceleration, time_list[i][0], time_list[i][1], time_list[i][2], 0.05)
        for j in range (0, len(acc_profile[0])):
            acc_list.append(acc_profile[0][j])
        if i > 0:
            temp = time_x_list[len(time_x_list)-1]
            for j in range (0, len(acc_profile[1])):
                acc_profile[1][j] = acc_profile[1][j]+ temp
                time_x_list.append(acc_profile[1][j])
        else:
            for j in range (0,len(acc_profile[1])):
                time_x_list.append(acc_profile[1][j])
        acc_profile = []
        vel_profile = Profile_generation.Velocity_profile(max_acceleration, time_list[i][0], time_list[i][1], time_list[i][2], 0.05, 0, feedrate[i])
        for j in range (0, len(vel_profile[0])):
            vel_list.append(vel_profile[0][j])
        vel_profile = []
    elif type_block[0] == 2:
        print("Тип блока - короткий")
    print("Обработка блока ", i+1, " закончена.")
    print("______________________________________")
Graphs.Plotting_1(time_x_list, acc_list, "Время, с", "Ускорение, мм/с2", "Профиль ускорения", "Ускорение")
Graphs.Plotting_1(time_x_list, vel_list, "Время, с", "Скорость, мм/с", "Профиль скорости", "Скорость")
