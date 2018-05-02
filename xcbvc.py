st = [3,4,5]
st_1 = []
for i in range (len(st)):
    st_1.append(st[i])
st_1[0] = st_1[0]+st_1[1]
print(st)
print(st_1)
