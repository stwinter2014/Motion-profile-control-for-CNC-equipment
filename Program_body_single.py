import Path_length_calculator
import Block_type
import Profile_generation
import Graphs
import math
"""Коды типов G-инструкций:
001 - G00;
010 - G01;
0110 - G02 + радиус;
1000 - G03 + радиус;
0111 - G02 + координаты центра;
1001 - G03 + координаты центра.
"""

"""Тело программы"""
path_code = "010"

"""Данные об обработке"""
feedrate = 10
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
type_path = Path_length_calculator.path_type(path_code)

"""Подсчет длины пути"""
if type_path == 1:
    print("Тип интерполяции - линейный.")
    path_l = Path_length_calculator.path_linear (st_point, fn_point)
    print("Длина пути: ", path_l)
elif type_path == 2:
    print("Тип интерполяции - круговой. Задание окружности с помощью радиуса.")
    path_l = Path_length_calculator.path_circular_r (st_point, fn_point, rad, way_move)
    print("Длина пути: ", path_l)
elif type_path == 3:
    print("Тип интерполяции - круговой. Задание окружности с помощью координат центра.")
    path_l = Path_length_calculator.path_circular_p (st_point, fn_point, cn_point, way_move)
    print("Длина пути: ", path_l)
else:
    print("Тип пути не определен.")

"""Проверка типа блока (обычный или короткий)"""
type_block = Block_type.block_t_check(path_l, feedrate, max_acceleration, max_deceleration)
if type_block[0] == 1:
    print("Тип блока - обычный")
    time_periods = Block_type.Time_Generator_n(feedrate, path_l, max_acceleration, max_deceleration)
    print("Время разгона: ", time_periods[0])
    print("Время постоянной скорости: ", time_periods[1])
    print("Время торможения: ", time_periods[2])
    acc_profile = Profile_generation.Acceleration_profile(max_acceleration, time_periods[0], time_periods[1], time_periods[2], 0.05)
    Graphs.Plotting_1(acc_profile[1], acc_profile[0], "Время", "Ускорение", "Профиль ускорения", "Ускорение")
    vel_profile = Profile_generation.Velocity_profile(max_acceleration, time_periods[0], time_periods[1], time_periods[2], 0.05, 0, feedrate)
    Graphs.Plotting_1(vel_profile[1], vel_profile[0], "Время", "Скорость", "Профиль скорости", "Скорость")
elif type_block[0] == 2:
    print("Тип блока - короткий")
