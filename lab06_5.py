num = int(input('Enter your Number:'))
if num>1:
    for i in range(2,num):
        if (num%i == 0):
            print(num,'เป็นจำนวนประกอบ')
            break
    else:
        print(num,'เป็นจำนวนเฉพาะ')
else:
    print(num,'เป็นจำนวนประกอบ')