count = 0
sum_rub = int()
count_rub = int()
sum_pen = int()
count_pen = int()
sum_pap = int()
count_pap = int()
order = int()

try:
    f = open('sales.txt', 'r+')
    f.seek(0,0)
    for l in f.readlines():
        l = l.strip()
        count+=1
        try:
            x,y,z,zz = l.split(', ')
            if y == 'Rubber':
                sum_rub = int(z)
                count_rub+=int(zz)
                order+=1
            if y == 'Pencil':
                sum_pen = int(z)
                count_pen+=int(zz)
                order+=1
            if y == 'Papers':
                sum_pap = int(z)
                count_pap+=int(zz)
                order+=1

        except ValueError:
            print('At line {}, an invalid is found, and it was skipped. [{}]'.format(count,l))

except FileNotFoundError:
    print('Cannot open '"sales.txt"'')

assert (int(zz)>0), ("AsserttionError:Check data at Line {} [{}]".format(count,l))
    
print('The data in files contains {} orders.'.format(order))
print('='*30)
print('Products were sold {} items'.format(count))
print('Rubber x {} items x {} bath = {} bath.'.format(count_rub,sum_rub,count_rub*sum_rub))
print('Pencil x {} items x {} bath = {} bath.'.format(count_pen,sum_pen,count_pen*sum_pen))
print('Papers x {} items x {} bath = {} bath.'.format(count_pap,sum_pap,count_pap*sum_pap))
print('='*30)
print('Total sales {} bath.'.format((count_rub*sum_rub)+(count_pen*sum_pen)+(count_pap*sum_pap)))