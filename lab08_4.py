stdID = input('Enter Your ID: ')
stdID.count('-')
if stdID.count('-') == 0:
    print('ไม่มีขีด (-)')
else:
    stdID = stdID.split('-')
    a = int(stdID[0][-1::])
    b = int(stdID[1][0])
    print ('ผลลัพธ์:',a,'+',b,'=',a+b)
    # print(int(stdID[0][-1::])+int(stdID[1][0]))
# result = int(stdID[0])+int(stdID[1])
# print(result)
