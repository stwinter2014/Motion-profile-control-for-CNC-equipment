import math
def Time_gen (feedrate, number, length, max_acc, max_dec):
    length_new = []
    for i in range (len(length)):
        length_new.append(length[i])
    for i in range (len(feedrate)):
        if feedrate[number] <= feedrate[number+1]:
            time_dec = 0
            time_acc = 2*feedrate[number]/max_acc
            len_ad = 1/4*max_acc*math.pow(time_acc, 2) + 1/4*max_acc*math.pow(time_dec, 2)
            for j in range(3):
                if len_ad > length_new[j]:
                    print(len_ad)
                    print(length_new[j])
                    time_const = 0
                    length_new[j] = (length[j] + length[j+1])
                    length_new.pop(j)
                    length_new.append(0)
    return length_new

feedrate = [10,10,10]
length = [10,30,10]
acc = 5
dec = 5
print(Time_gen (feedrate, 0, length, acc, dec))
