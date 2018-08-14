import Spline
import Path_length_calculator
import math
import Graphs

start_point_1 = [20, 10, 0]
finish_point_1 = [42.361, 30, 0]
start_point_2 = [42.361, 30, 0]
finish_point_2 = [64.721, 10, 0]

Lt = 2
n = 0.3
d = Lt/(2*n+1)
c = n*d
cd = c + d
print('c =', c)
print('d =', d)
point_1 = Spline.Point_find(start_point_1, finish_point_1, Lt, 0)
point_6 = Spline.Point_find(start_point_2, finish_point_2, Lt, 1)

point_2 = Spline.Point_find(start_point_1, finish_point_1, cd, 0)
point_3 = Spline.Point_find(start_point_1, finish_point_1, d, 0)

point_4 = Spline.Point_find(start_point_2, finish_point_2, d, 1)
point_5 = Spline.Point_find(start_point_2, finish_point_2, cd, 1)

t = 0.5
x1 = math.pow((1-t), 5)*point_1[0] + 5*t*math.pow((1-t), 4)*point_2[0] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[0] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[0] + 5*math.pow(t, 4)*(1-t)*point_5[0] + math.pow(t, 5)*point_6[0]
y1 = math.pow((1-t), 5)*point_1[1] + 5*t*math.pow((1-t), 4)*point_2[1] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[1] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[1] + 5*math.pow(t, 4)*(1-t)*point_5[1] + math.pow(t, 5)*point_6[1]
print('x1 =', x1)
print('y1 =', y1)
t = 0.55
x2 = math.pow((1-t), 5)*point_1[0] + 5*t*math.pow((1-t), 4)*point_2[0] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[0] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[0] + 5*math.pow(t, 4)*(1-t)*point_5[0] + math.pow(t, 5)*point_6[0]
y2 = math.pow((1-t), 5)*point_1[1] + 5*t*math.pow((1-t), 4)*point_2[1] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[1] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[1] + 5*math.pow(t, 4)*(1-t)*point_5[1] + math.pow(t, 5)*point_6[1]

t = 0.45
x3 = math.pow((1-t), 5)*point_1[0] + 5*t*math.pow((1-t), 4)*point_2[0] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[0] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[0] + 5*math.pow(t, 4)*(1-t)*point_5[0] + math.pow(t, 5)*point_6[0]
y3 = math.pow((1-t), 5)*point_1[1] + 5*t*math.pow((1-t), 4)*point_2[1] + 10*math.pow(t,2)*math.pow((1-t), 3)*point_3[1] + 10*math.pow(t, 3)*math.pow((1-t), 2)*point_4[1] + 5*math.pow(t, 4)*(1-t)*point_5[1] + math.pow(t, 5)*point_6[1]


"""Пoстроение кривой"""
x_curve = [x1, x2, x3]
y_curve = [y1, y2, y3]

x_trajectory = [start_point_1[0], finish_point_1[0], finish_point_2[0]]
y_trajectory = [start_point_1[1], finish_point_1[1], finish_point_2[1]]
Graphs.Plotting_02(x_curve, y_curve, x_trajectory, y_trajectory, 'net', 'da', 'da', 'da', 'net')

epsilon = Path_length_calculator.Path_linear([x1, y1], finish_point_1)
print('e1 =', epsilon)

X1 = 1/32*(point_1[0] + 5*point_2[0] + 10*point_3[0] + 10*point_4[0] + 5*point_5[0] + point_6[0])
Y1 = 1/32*(point_1[1] + 5*point_2[1] + 10*point_3[1] + 10*point_4[1] + 5*point_5[1] + point_6[1])
epsilon1 = Path_length_calculator.Path_linear([X1, Y1], finish_point_1)
print('e2 =', epsilon1)

X2 = float(finish_point_1[0] + 1/32*(-(2*c+d) + 5*(-(2*c+d)+ c) + 10*(-(2*c+d)+ 2*c)))
Y2 = float(finish_point_1[1] + 1/32*(-(2*c+d) + 5*(-(2*c+d)+ c) + 10*(-(2*c+d)+ 2*c)))
epsilon2 = Path_length_calculator.Path_linear([X2, Y2], finish_point_1)
print('e3 =', epsilon2)

print('X1 =', X1)
print('Y1 =', Y1)

print('X2 =', X2)
print('Y2 =', Y2)

e = ((7*n+16))/32*d
print('e =', e)

Y22 = finish_point_1[1] - e
X22 = finish_point_1[0] - e

print('X22 =', X22)
print('Y22 =', Y22)
