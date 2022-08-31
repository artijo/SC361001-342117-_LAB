ns = int(input('Enter Start: '))
ne = int(input('Enter End: '))
for i in range(ns,ne+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print ('จำนวนเฉพาะคือ',i)
