from itertools import count


ns = int(input('Start: '))
ne = int(input('End: '))
count = 0
for i in range(ns,ne+1):
    if i > 1:
        # print(i)
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            print('prime is',i)