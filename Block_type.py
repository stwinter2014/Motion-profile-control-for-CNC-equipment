import math
import Work_with_files

def block_t_check (length, feedrate, max_acc, max_dec):
    type_res = []
    len_acc_dec = 2*math.pow(feedrate, 2)/(max_acc)
    if len_acc_dec < length:
        type_res.append(1)
        type_res.append(len_acc_dec)
    else:
        type_res.append(2)
        type_res.append(len_acc_dec)
    return type_res

def Time_Generator_n(feedrate, length, max_acc, max_dec):
    time_acc = 2*feedrate/max_acc
    time_dec = 2*feedrate/max_dec
    time_const = 2*(length-(2*math.pow(feedrate, 2)/max_acc))/(max_acc*time_acc)
    return time_acc, time_const, time_dec

def block_t_check_la (length, feedrate, max_acc, max_dec):
    type_res = []
    len_acc_dec = 2*math.pow(feedrate, 2)/(max_acc)
    if len_acc_dec < length:
        type_res.append(1)
        type_res.append(len_acc_dec)
    else:
        type_res.append(2)
        type_res.append(len_acc_dec)
    return type_res

"""Функция для подсчета времени разгона/торможения, постоянной скорости для нормального блока.
На вход подается:
1. Список величин подачи для каждого блока;
2. Номер рассматриваемого блока (подсчет от нуля);
3. Длина пути движения инструмента за блок;
4. Максимально возможное ускорение;
5. максимально возможное замедление.
На выход подается:
1. Время разгона;
2. Время постоянной скорости;
3. Время торможения."""
def Time_Generator_lookahead(feedrate, number, length, max_acc, max_dec, vel_last):
    if number == 0 and number < len(feedrate)-1:
        if feedrate[number] <= feedrate[number+1]:
            time_acc = 2*feedrate[number]/max_acc
            time_dec = 0
            time_const = 0
            len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
            if len_ad > length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_acc = math.sqrt(length*4/max_acc)
            elif len_ad == length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_acc = math.sqrt(length*4/max_acc)
            else:
                print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
        elif feedrate[number] > feedrate[number+1]:
            len_ad_t = 0
            time_acc = 2*feedrate[number]/max_acc
            time_dec = 2*feedrate[number]/max_dec - 2*feedrate[number+1]/max_acc
            len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
            if len_ad > length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_acc = 2*feedrate[number+1]/max_acc
                time_dec = 0
                len_ad_t = 1/4*max_acc*time_acc
                if len_ad_t < length:
                    time_const = (length-len_ad_t)/feedrate[number+1]
                elif len_ad_t == length:
                    time_const = 0
                else:
                    time_acc = math.sqrt(length*4/max_acc)
            elif len_ad == length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
    elif number != 0 and number == len(feedrate)-1:
        if feedrate[number] <= feedrate[number-1]:
            time_acc = 0
            time_dec = 2*feedrate[number]/max_dec
            len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
            if len_ad > length:
                time_const = 0
                pass
            elif len_ad == length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
        elif feedrate[number] > feedrate[number-1]:
            time_acc = 2*feedrate[number]/max_acc - 2*feedrate[number-1]/max_dec
            time_dec = 2*feedrate[number]/max_dec
            len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
            if len_ad > length:
                time_const = 0
                pass
            elif len_ad == length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
    elif number == 0 and number == len(feedrate)-1:
        time_acc = 2*feedrate[number]/max_acc
        time_dec = 2*feedrate[number]/max_dec
        len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
        if len_ad > length:
            print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
            time_acc = math.sqrt(length*2/max_acc)
            time_dec = math.sqrt(length*2/max_dec)
        elif len_ad == length:
            print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
        else:
            print(Work_with_files.Write_log("Тип блока - обычный."))
            time_const = (length-len_ad)/feedrate[number]
    else:
        if feedrate[number] <= feedrate[number-1]:
            time_acc = 0
        elif feedrate[number] > feedrate[number-1]:
            if vel_last < feedrate[number]:
                time_acc = 2*feedrate[number]/max_acc - 2*vel_last/max_acc
            else:
                time_acc = 2*feedrate[number]/max_acc - 2*feedrate[number-1]/max_dec
        if feedrate[number] <= feedrate[number+1]:
            time_dec = 0
        elif feedrate[number] > feedrate[number+1]:
            time_dec = 2*feedrate[number]/max_dec - 2*feedrate[number+1]/max_acc
        len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
        if len_ad > length:
            time_const = 0
            pass
        elif len_ad == length:
            print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
        else:
            print(Work_with_files.Write_log("Тип блока - обычный."))
            time_const = (length-len_ad)/feedrate[number]
    return time_acc, time_const, time_dec

"""Функция для подсчета времени разгона/торможения, постоянной скорости для нормального блока.
На вход подается:
1. Список величин подачи для каждого блока;
2. Номер рассматриваемого блока (подсчет от нуля);
3. Длина пути движения инструмента за блок;
4. Максимально возможное ускорение;
5. максимально возможное замедление.
На выход подается:
1. Время разгона;
2. Время постоянной скорости;
3. Время торможения."""
def Time_Generator_lookahead_1(feedrate, number, length, max_acc, max_dec, vel_last, max_acc1, max_dec1, max_acc2, max_dec2):
    if number == 0 and number < len(feedrate)-1:
        if feedrate[number] <= feedrate[number+1]:
            time_acc = 2*feedrate[number]/max_acc
            time_dec = 0
            time_const = 0
            len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
            if len_ad > length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_acc = math.sqrt(length*4/max_acc)
            elif len_ad == length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_acc = math.sqrt(length*4/max_acc)
            else:
                print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
        elif feedrate[number] > feedrate[number+1]:
            len_ad_t = 0
            time_acc = 2*feedrate[number]/max_acc
            time_dec = 2*feedrate[number]/max_dec - 2*feedrate[number+1]/max_dec
            print("da")
            len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_dec*math.pow(time_dec, 2)
            if len_ad > length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_acc = 2*feedrate[number+1]/max_acc
                time_dec = 0
                len_ad_t = 1/4*max_acc*time_acc
                if len_ad_t < length:
                    time_const = (length-len_ad_t)/feedrate[number+1]
                elif len_ad_t == length:
                    time_const = 0
                else:
                    time_acc = math.sqrt(length*4/max_acc)
            elif len_ad == length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
    elif number != 0 and number == len(feedrate)-1:
        if feedrate[number] <= feedrate[number-1]:
            time_acc = 0
            time_dec = 2*feedrate[number]/max_dec
            len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
            if len_ad > length:
                time_const = 0
                pass
            elif len_ad == length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
        elif feedrate[number] > feedrate[number-1]:
            time_acc = 2*feedrate[number]/max_acc - 2*feedrate[number-1]/max_acc
            time_dec = 2*feedrate[number]/max_dec
            len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
            if len_ad > length:
                time_const = 0
                pass
            elif len_ad == length:
                print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
    elif number == 0 and number == len(feedrate)-1:
        time_acc = 2*feedrate[number]/max_acc
        time_dec = 2*feedrate[number]/max_dec
        len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
        if len_ad > length:
            print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
            time_acc = math.sqrt(length*2/max_acc)
            time_dec = math.sqrt(length*2/max_dec)
        elif len_ad == length:
            print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
        else:
            print(Work_with_files.Write_log("Тип блока - обычный."))
            time_const = (length-len_ad)/feedrate[number]
    else:
        if feedrate[number] <= feedrate[number-1]:
            time_acc = 0
        elif feedrate[number] > feedrate[number-1]:
            if vel_last < feedrate[number]:
                time_acc = 2*feedrate[number]/max_acc - 2*vel_last/max_acc
            else:
                time_acc = 2*feedrate[number]/max_acc - 2*feedrate[number-1]/max_dec
        if feedrate[number] <= feedrate[number+1]:
            time_dec = 0
        elif feedrate[number] > feedrate[number+1]:
            time_dec = 2*feedrate[number]/max_dec - 2*feedrate[number+1]/max_acc
        len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
        if len_ad > length:
            time_const = 0
            pass
        elif len_ad == length:
            print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
        else:
            print(Work_with_files.Write_log("Тип блока - обычный."))
            time_const = (length-len_ad)/feedrate[number]
    return time_acc, time_const, time_dec

"""Функция для подсчета времени разгона/торможения, постоянной скорости для нормального блока.
На вход подается:
1. Список величин подачи для каждого блока;
2. Номер рассматриваемого блока (подсчет от нуля);
3. Длина пути движения инструмента за блок;
4. Максимально возможное ускорение;
5. максимально возможное замедление.
На выход подается:
1. Время разгона;
2. Время постоянной скорости;
3. Время торможения."""
def Time_Generator_la_withangles(feedrate, number, length, max_acc, max_dec, vel_last):
    if number == 0 and number < len(feedrate)-1:
        if feedrate[number] <= feedrate[number+1]:
            time_acc = 2*feedrate[number]/max_acc
            time_dec = 0
            time_const = 0
            len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
            if len_ad > length:
                #print(Work_with_files.Write_log("Тип блока - короткий."))
                time_acc = math.sqrt(length*4/max_acc)
            elif len_ad == length:
                #print(Work_with_files.Write_log("Тип блока - короткий."))
                time_acc = math.sqrt(length*4/max_acc)
            else:
                #print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
        elif feedrate[number] > feedrate[number+1]:
            time_acc = 2*feedrate[number]/max_acc
            time_dec = 2*feedrate[number]/max_dec - 2*feedrate[number+1]/max_acc
            len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
            len_ad_t = len_ad
            if len_ad > length:
                #print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
                feed = feedrate[number]
                while len_ad_t > length:
                    feed = feed-0.001
                    time_acc = 2*feed/max_acc
                    time_dec = 2*feed/max_dec - 2*feedrate[number+1]/max_acc
                    len_ad_t = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
            elif len_ad == length:
                #print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                #print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
    elif number != 0 and number == len(feedrate)-1:
        if feedrate[number] <= feedrate[number-1]:
            time_acc = 0
            time_dec = 2*feedrate[number]/max_dec
            len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
            if len_ad == length:
                #print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                #print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
        elif feedrate[number] > feedrate[number-1]:
            time_acc = 2*feedrate[number]/max_acc - 2*feedrate[number-1]/max_dec
            time_dec = 2*feedrate[number]/max_dec
            len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
            len_ad_t = len_ad
            if len_ad > length:
                time_const = 0
                #print(Work_with_files.Write_log("Тип блока - короткий."))
                feed = feedrate[number]
                while len_ad_t > length:
                    feed = feed-0.1
                    time_acc = 2*feed/max_acc - 2*feedrate[number-1]/max_dec
                    time_dec = 2*feed/max_dec
                    len_ad_t = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
            elif len_ad == length:
                #print(Work_with_files.Write_log("Тип блока - короткий."))
                time_const = 0
            else:
                #print(Work_with_files.Write_log("Тип блока - обычный."))
                time_const = (length-len_ad)/feedrate[number]
    elif number == 0 and number == len(feedrate)-1:
        time_acc = 2*feedrate[number]/max_acc
        time_dec = 2*feedrate[number]/max_dec
        len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
        if len_ad > length:
            #print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
            time_acc = math.sqrt(length*2/max_acc)
            time_dec = math.sqrt(length*2/max_dec)
        elif len_ad == length:
            #print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
        else:
            #print(Work_with_files.Write_log("Тип блока - обычный."))
            time_const = (length-len_ad)/feedrate[number]
    else:
        if feedrate[number] <= feedrate[number-1]:
            time_acc = 0
        elif feedrate[number] > feedrate[number-1]:
            if vel_last < feedrate[number]:
                time_acc = 2*feedrate[number]/max_acc - 2*vel_last/max_acc
            else:
                time_acc = 2*feedrate[number]/max_acc - 2*feedrate[number-1]/max_dec
        if feedrate[number] <= feedrate[number+1]:
            time_dec = 0
        elif feedrate[number] > feedrate[number+1]:
            time_dec = 2*feedrate[number]/max_dec - 2*feedrate[number+1]/max_acc
        len_ad = 1/4*max_acc*time_acc + 1/4*max_acc*time_dec
        if len_ad > length:
            time_const = 0
            pass
        elif len_ad == length:
            #print(Work_with_files.Write_log("Тип блока - короткий."))
            time_const = 0
        else:
            #print(Work_with_files.Write_log("Тип блока - обычный."))
            time_const = (length-len_ad)/feedrate[number]
    return time_acc, time_const, time_dec
