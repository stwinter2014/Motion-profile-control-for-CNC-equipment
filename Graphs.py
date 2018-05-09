import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy import pi, cos, sin
import math

"""
Функция построения графиков.
На вход принимается:
1. Значения оси x: время.
2. Значения оси y: ускорение, скорость, перемещение или толчок.
3. Название оси x.
4. Название оси y.
5. Название графика.
6. 
"""
def Plotting_1 (x, y, name_x, name_y, name_graph, label, time_per):
    time_sum = 0
    time_sum_hole = 0
    alph = 0.2
    plt.plot(x,y,label=label)
    currentAxis = plt.gca()
    for i in range (len(time_per)):
        for j in range (len(time_per[i])):
            time_sum += time_per[i][j]
        currentAxis.add_patch(mpl.patches.Rectangle((time_sum_hole, -10), time_sum, 100, alpha=alph, color='#D5D0CF'))
        time_sum_hole += time_sum
        time_sum = 0
        if i%2 == 0:
            alph += 0.2
        else:
            alph -= 0.2
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(name_graph)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'w')
    plt.show()

def Plotting_01 (x, y, name_x, name_y, name_graph, label):
    plt.plot(x,y,label=label)
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(name_graph)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    plt.show()

def Plotting_02(x1, y1, x2, y2, name_x, name_y, name_graph, label1, label2):
    plt.plot(x1, y1, label = label1)
    plt.plot(x2, y2, label = label2, alpha=0.4)
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(name_graph)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    plt.show()

def Plotting_2 (x, y, x2, y2, name_x, name_y1, name_y2, name_graph1, name_graph2):
    fig = plt.figure()
    fig1 = fig.add_subplot(211)
    fig2 = fig.add_subplot(212)
    fig1.set_title(name_graph1)
    fig1.plot(x, y)
    fig2.set_title(name_graph2)
    fig2.plot(x2, y2)
    fig1.set_ylabel(name_y1)
    fig2.set_ylabel(name_y2)
    plt.xlabel(name_x)
    fig1.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    fig2.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    plt.show()
