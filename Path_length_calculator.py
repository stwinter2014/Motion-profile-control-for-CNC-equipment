import math

"""Функция для подсчета длины траектории при линейном типе движения.
На вход подается:
1.G-код (или его интерпретация), означающий тип движения

На выход подается:
1. Тип траектории (1 - линейная, 2 - круговая);
В зависимости от кода типа траектории вызывается функция подсчета длины траектории.
"""
def path_type (type_g):
    if type_g == "001":
        type_code = 1
    elif type_g == "010":
        type_code = 1
    elif type_g == "011":
        type_code = 2
    elif type_g == "100":
        type_code = 2
    elif type_g == "101":
        type_code = 3
    elif type_g == "110":
        type_code = 3
    else:
        type_code = str("Тип пути не определен.")
    return type_code

"""Функция для подсчета длины траектории при круговом типе движения.
На вход подается:
1. Список координат начальной точки в формате [x, y, z];
2. Список координат конечной точки в формате [x, y, z];
3. Величина радиуса окружности.
На выход подается:
1. Длина траектории, мм (число типа float).
"""
def path_circular_r (start_points, finish_points, radius, way):
    length_path = 0
    length_axes_list = []
    length_axes = 0
    check = 0
    """Определение перемещения"""
    for i in range (len(start_points)):
        length_axes = math.fabs(start_points[i] - finish_points[i])
        if length_axes != 0:
            check += 1
        length_axes_list.append(length_axes)
        length_axes = 0
    if check == 1:
        for i in range (len(length_axes_list)):
            if length_axes_list[i] != 0:
                length_path = length_axes_list[i]
    elif check == 2:
        for i in range (len(length_axes_list)):
            temp = math.pow(length_axes_list[i], 2)
            length_path += temp
            temp = 0
        length_path = math.sqrt(length_path)
    elif check == 3:
        for i in range (len(length_axes_list)-1):
            temp = math.pow(length_axes_list[i], 2)
            length_path += temp
            temp = 0
        length_path = math.sqrt(length_path)
        length_path = math.sqrt(math.pow(length_path, 2) + math.pow(length_axes_list[2], 2))
    """Вычисление углов равнобедненного треугольника"""
    cos_alpha = length_path/(2*radius)
    alpha = math.degrees(math.acos(cos_alpha))
    beta = 180 - 2*alpha
    """Вычисление длины дуги - длины траеткории"""
    if way == 1:
        length = (math.pi*radius*beta)/(180)
    elif way == 2:
        length = (math.pi*radius*(360-beta))/(180)
    return length

"""Функция для подсчета длины траектории при круговом типе движения
при задании  координат центра окружности.
На вход подается:
1. Список координат начальной точки в формате [x, y, z];
2. Список координат конечной точки в формате [x, y, z];
3. Список координат центра окружности в формате [x, y, z];
4. Код направления движения (1 - по часовой стрелке, 2 - против часовой стрелки).
На выход подается:
1. Длина траектории, мм (число типа float).
"""
def path_circular_p (start_points, finish_points, center_points, way):
    radius = 0
    length_r_list = []
    length_r = 0
    check = 0
    """Определение радиуса окружности"""
    for i in range (len(start_points)):
        length_r = math.fabs(start_points[i] - center_points[i])
        if length_r != 0:
            check += 1
        length_r_list.append(length_r)
        length_r = 0
    if check == 1:
        for i in range (len(length_r_list)):
            if length_r_list[i] != 0:
                radius = length_r_list[i]
    elif check == 2:
        for i in range (len(length_r_list)):
            temp = math.pow(length_r_list[i], 2)
            radius += temp
            temp = 0
        radius = math.sqrt(radius)
    elif check == 3:
        for i in range (len(length_r_list)-1):
            temp = math.pow(length_r_list[i], 2)
            radius += temp
            temp = 0
        radius = math.sqrt(radius)
        radius = math.sqrt(math.pow(radius, 2) + math.pow(length_r_list[2], 2))
    """Определение кратчайшего пути"""
    length_sh_path = 0
    length_axes_list = []
    length_axes = 0
    check = 0
    for i in range (len(start_points)):
        length_axes = math.fabs(start_points[i] - finish_points[i])
        if length_axes != 0:
            check += 1
        length_axes_list.append(length_axes)
        length_axes = 0
    if check == 1:
        for i in range (len(length_axes_list)):
            if length_axes_list[i] != 0:
                length_sh_path = length_axes_list[i]
    elif check == 2:
        for i in range (len(length_axes_list)):
            temp = math.pow(length_axes_list[i], 2)
            length_sh_path += temp
            temp = 0
        length_sh_path = math.sqrt(length_sh_path)
    elif check == 3:
        for i in range (len(length_axes_list)-1):
            temp = math.pow(length_axes_list[i], 2)
            length_sh_path += temp
            temp = 0
        length_sh_path = math.sqrt(length_sh_path)
        length_sh_path = math.sqrt(math.pow(length_sh_path, 2) + math.pow(length_axes_list[2], 2))
    """Вычисление углов равнобедненного треугольника"""
    cos_alpha = length_sh_path/(2*radius)
    alpha = math.degrees(math.acos(cos_alpha))
    beta = 180 - 2*alpha
    """Вычисление длины дуги - длины траеткории"""
    if way == 1:
        length = (math.pi*radius*beta)/(180)
    elif way == 2:
        length = (math.pi*radius*(360-beta))/(180)
    return length

"""Функция для подсчета длины траектории при линейном или круговом типе движения.
На вход подается:
1. Список координат начальной точки в формате [x, y, z]
2. Список координат конечной точки в формате [x, y, z]
На выход подается:
1. Длина траектории, мм (число типа float)
"""
def Path_linear (start_points, finish_points):
    length_path = 0
    length_axes_list = []
    length_axes = 0
    check = 0
    """Определение перемещения"""
    for i in range (len(start_points)):
        length_axes = math.fabs(start_points[i] - finish_points[i])
        if length_axes != 0:
            check += 1
        length_axes_list.append(length_axes)
        length_axes = 0
    if check == 1:
        for i in range (len(length_axes_list)):
            if length_axes_list[i] != 0:
                length_path = length_axes_list[i]
    elif check == 2:
        for i in range (len(length_axes_list)):
            temp = math.pow(length_axes_list[i], 2)
            length_path += temp
            temp = 0
        length_path = math.sqrt(length_path)
    elif check == 3:
        for i in range (len(length_axes_list)-1):
            temp = math.pow(length_axes_list[i], 2)
            length_path += temp
            temp = 0
        length_path = math.sqrt(length_path)
        length_path = math.sqrt(math.pow(length_path, 2) + math.pow(length_axes_list[2], 2))
    return length_path
