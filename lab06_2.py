total = 0
num = int(input("Enter your Number: "))
print('ผลลัพธ์คือ ',end="")
for i in range(1,num+1):
    total = total+i
    print(i,end="")
    if i < num:
        print(end="+")
    else:
        print(' =',total)