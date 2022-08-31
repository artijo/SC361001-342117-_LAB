text = input('Enter your Char: ')
check = False
no = ''
count=0
for i in text:
    #  print (i)
    if i.isdigit():
        check = True
        no = no+i #str + กันจะเอามาต่อกัน
        # print(i,end="")
        count+=1

if check:
    print('มีตัวเลขคือ:',no)
    print('มีตัวเลข=',count,'ตัว')
else:
    print('ไม่มีตัวเลข')