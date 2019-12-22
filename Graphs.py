import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
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
def Plotting_1 (x, y, name_x, name_y, name_graph, label, time_per, filename):
    time_sum = 0
    time_sum_hole = 0
    alph = 0.2
    fig = plt.figure()
    plt.plot(x,y,label=label)
    currentAxis = plt.gca()
    for i in range (len(time_per)):
        for j in range (len(time_per[i])):
            time_sum += time_per[i][j]
        currentAxis.add_patch(mpl.patches.Rectangle((time_sum_hole, -100), time_sum, 40, alpha=alph, color='#D5D0CF'))
        time_sum_hole += time_sum
        time_sum = 0
        if i%2 == 0:
            alph += 0.2
        else:
            alph -= 0.2
    plt.xlabel(name_x, fontsize = 13)
    plt.ylabel(name_y, fontsize = 13)
    plt.title(name_graph, fontsize = 13)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'w')
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['font.family'] = 'Calibri'
    plt.show()
    fig.savefig(filename + '.pdf')

def Plotting_01 (x, y, name_x, name_y, name_graph, label, filename):
    fig = plt.figure()
    plt.plot(x,y,label=label)
    plt.xlabel(name_x, fontsize = 13)
    plt.ylabel(name_y, fontsize = 13)
    plt.title(name_graph, fontsize = 13)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['font.family'] = 'Calibri'
    plt.show()
    fig.savefig(filename + '.pdf')

"""Две кривые на одном графике."""
def Plotting_02(x1, y1, x2, y2, name_x, name_y, name_graph, label1, label2, filename):
    fig = plt.figure()
    plt.plot(x1, y1, label = label1)
    plt.plot(x2, y2, label = label2, alpha=0.4)
    plt.xlabel(name_x, fontsize = 13)
    plt.ylabel(name_y, fontsize = 13)
    plt.title(name_graph, fontsize = 13)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['font.family'] = 'Calibri'
    plt.show()
    fig.savefig(filename + '.pdf')

def Plotting_03_help(x1, y1, x2, y2, x3, y3, name_x, name_y, name_graph, label1, label2):
    plt.plot(x1, y1, label = label1)
    plt.plot(x2, y2, label = label2, alpha=0.4)
    plt.plot(x3, y3)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.text(0, 0, 'da', fontsize=14, bbox=props)
    plt.xlabel(name_x, fontsize = 13)
    plt.ylabel(name_y, fontsize = 13)
    plt.title(name_graph, fontsize = 13)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    plt.show()

def Plotting_02_colors(x1, y1, x2, y2, name_x, name_y, name_graph, label1, label2, filename):
    fig = plt.figure()
    plt.plot(x1, y1, color = 'r', label = label1)
    plt.plot(x2, y2, label = label2, color='b', alpha=0.5)
    plt.xlabel(name_x, fontsize = 13)
    plt.ylabel(name_y, fontsize = 13)
    plt.title(name_graph, fontsize = 13)
    plt.legend()
    plt.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['font.family'] = 'Calibri'
    plt.show()
    fig.savefig(filename + '.pdf')

def Plotting_03(x1, y1, x2, y2, x3, y3, name_x, name_y, name_graph, label1, label2, label3):
    plt.plot(x1, y1, label = label1)
    plt.plot(x2, y2, label = label2, alpha=0.4)
    plt.plot(x3, y3, label = label3)
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
    plt.legend()
    plt.show()
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['font.family'] = 'Calibri'
    fig.savefig('Noooo.pdf')

def Plotting_22 (x, y, x2, y2, x3, y3, x4, y4, name_x, name_y, name_graph1, name_graph2, label1, label2):
    fig = plt.figure()
    fig1 = fig.add_subplot(121)
    fig2 = fig.add_subplot(122)
    fig1.set_title(name_graph1, fontsize = 13)
    fig1.plot(x, y, label=label1)
    fig1.plot(x2, y2, label=label2, alpha = 0.4)
    fig2.set_title(name_graph2, fontsize = 13)
    fig2.plot(x3, y3, label = label1)
    fig2.plot(x4, y4, label = label2, alpha = 0.4)
    fig1.set_ylabel(name_y, fontsize = 13)
    fig2.set_ylabel(name_y, fontsize = 13)
    fig1.set_xlabel(name_x, fontsize = 13)
    fig2.set_xlabel(name_x, fontsize = 13)
    fig1.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    fig2.grid(b=None, which='major', axis='both', color = 'black', alpha = 0.4)
    fig1.legend()
    fig2.legend()
    plt.show()
