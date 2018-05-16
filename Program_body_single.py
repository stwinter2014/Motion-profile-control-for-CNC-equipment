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
feedrate = 25
max_acceleration = 25
max_deceleration = 25
time_periods = []
time_interpolation = 0.05
"""Данные о перемещении"""
path_l = 0
#st_point = [60, 20, 0]
#fn_point = [140, 80, 0]
st_point = [40, 30, 0]
fn_point = [140, 80, 0]
"Данные для круговой траектории инструмента"
cn_point = [79.616,0,19.494]
rad = 71
way_move = 1

"""Определение типа пути (линейный или круговой, тип задания окружности)"""
type_path = Path_length_calculator.path_type(path_code)

"""Подсчет длины пути"""
if type_path == 1:
    print("Тип интерполяции - линейный.")
    path_l = Path_length_calculator.Path_linear (st_point, fn_point)
    print("Длина пути: ", round(path_l, 3), "мм.")
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
times = []
"""Проверка типа блока (обычный или короткий)"""
path_l = 30
print("Длина пути: ", round(path_l, 3), "мм.")
type_block = Block_type.block_t_check(path_l, feedrate, max_acceleration, max_deceleration)
if type_block[0] == 1:
    print("Тип блока - обычный")
else:
    print("Тип блока - короткий")
time_periods = Block_type.Time_Generator_n(feedrate, path_l, max_acceleration, max_deceleration)
print("Время разгона: ", round(time_periods[0], 3), "с.")
print("Время постоянной скорости: ", round(time_periods[1], 3), "с.")
print("Время торможения: ", round(time_periods[2], 3), "с.")
times.append(time_periods)
jerk_profile = Profile_generation.Jerk_profile(max_acceleration, max_deceleration, time_periods[0], time_periods[1], time_periods[2], time_interpolation, 0)
Graphs.Plotting_1(jerk_profile[1], jerk_profile[0], "Время, с", "Толчок, мм/с3", "Профиль толчка", "Толчок", times)
acc_profile = Profile_generation.Acceleration_profile(max_acceleration, max_deceleration, time_periods[0], time_periods[1], time_periods[2], time_interpolation, 0)
Graphs.Plotting_1(acc_profile[1], acc_profile[0], "Время, с", "Ускорение, мм/с2", "Профиль ускорения", "Ускорение", times)
vel_profile = Profile_generation.Velocity_profile(max_acceleration, max_deceleration, time_periods[0], time_periods[1], time_periods[2], time_interpolation, 0, feedrate)
Graphs.Plotting_1(vel_profile[1], vel_profile[0], "Время, с", "Скорость, мм/с", "Профиль скорости", "Скорость", times)
print("Максимальная достигнутая скорость на блоке: " + str(vel_profile[3]) + " мм/с.")
dis_profile = Profile_generation.Displacement_profile(max_acceleration, max_deceleration, time_periods[0], time_periods[1], time_periods[2], time_interpolation, 0)
Graphs.Plotting_1(dis_profile[1], dis_profile[0], "Время, с", "Перемещение, мм", "Профиль перемещения", "Перемещение", times)
print("Обработка блока 1 закончена.")
print("______________________________________")
