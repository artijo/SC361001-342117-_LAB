numStart = int(input("กรุณากรอกช่วงตัวเลขเริ่มต้น: "))
numEnd = int(input("กรุณากรอกช่วงตัวเลขสิ้นสุด: "))
count = 0
for i in range(numStart,numEnd+1):
    if (i%2 != 0):
        count = count + 1
print("จำนวนเลขคี่",numStart,"ถึง",numEnd,'มี',count,'จำนวน = [',end="")

for i in range(numStart,numEnd+1):
    if (i%2 != 0):
        print(i,end="")
        if numEnd%2==0:
            numEnd = numEnd-1
        if i < numEnd:
            print(end=",")
print("]",end="")