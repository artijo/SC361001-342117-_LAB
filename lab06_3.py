total = 1
num = int(input("Enter your Number: "))
print('ผลลัพธ์ของ ',end="")
for i in range(1,num+1):
    total = total*i
print(num,end="")
print('! =',total)