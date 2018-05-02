import math
def time_gen_normal (feedrate, length, max_acc, max_dec, len_ad):
    time_list = []
    time_acc = 0
    time_dec = 0
    time_con = 0
    time_acc = 2*feedrate/(len_ad/2)
    time_list.append(time_acc)
    time_list.append(time_con)
    time_dec = 2*feedrate/(len_ad/2)
    time_list.append(time_dec)
    len_ad = math.pow(feedrate, 2)/(2*max_acc)
    time_con = (length-len_ad)/feedrate
    time_list[1] = time_con
    return time_list

def time_gen_short (feedrate, length, max_acc, max_dec):
    time_list = []
    time_acc = 0
    time_dec = 0
    time_con = 0
    time_acc = feedrate/max_acc
    time_list.append(time_acc)
    time_list.append(time_con)
    time_dec = feedrate/max_dec
    time_list.append(time_dec)
    return time_list
