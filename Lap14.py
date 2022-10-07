count = 0

# sum_rub = int()
# count_rub = int()
# sum_pen = int()
# count_pen = int()
# sum_pap = int()
# count_pap = int()
# order = int()

try:
    f = open('sales.txt', 'r+')
    f.seek(0,0)
    for l in f.readlines():
        l = l.strip()
        count+=1
        try:
            x,y,z,zz = l.split(',')


        except ValueError:
            print('At line {}, an invalid is found, and it was skipped. [{}]'.format(count,l))
            # f.seek(0,0)
            # ccc = len(f.readlines())
            # print (ccc)
            # f.seek(0,0)
            
            # sum_rub = int()
            # count_rub = int()
            # sum_pen = int()
            # count_pen = int()
            # sum_pap = int()
            # count_pap = int()
            # order = int()

            # for l in f.readlines():
            #     l = l.strip()
            #     a,b,c,d = l.split(',')
            #     order+=1

            #     if b == 'Rubber':
            #         sum_rub = int(c)
            #         count_rub = int(d)
            #     if b == 'Pencil':
            #         sum_pen = int(c)
            #         count_pen = count_pen+int(d)
            #     if b == 'Papers':
            #         sum_pap = int(c)
            #         count_pap = int(d)
            # print(order) 
                       

                
        


except FileNotFoundError:
    print('Cannot open '"sales.txt"'')

assert (int(zz)>0), ("AsserttionError:Check data at Line {} [{}]".format(count,l))

f.seek(0,0)
sum_rub = int()
count_rub = int()
sum_pen = int()
count_pen = int()
sum_pap = int()
count_pap = int()
order = int()
for l in f.readlines():
    l = l.strip()
    a,b,c,d = l.split(',')
    order+=1

    if b == 'Rubber':
        sum_rub = int(c)
        count_rub = int(d)
    if b == 'Pencil':
        sum_pen = int(c)
        count_pen = count_pen+int(d)
    if b == 'Papers':
        sum_pap = int(c)
        count_pap = int(d)

    print (b)
    
