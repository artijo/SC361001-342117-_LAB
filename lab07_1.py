onetime= False
min=0
max=0
sum=0
count=0
while True:
    num = int(input('Enter Your Number: '))
    if num == 0:
        break
    if onetime == False: #เพิ่มค่าใส่numครั้งแรก
        min = num
        max=num
        onetime = True
    if num<min:
        min=num
    if num>max:
        max=num
    sum = sum+num
    count = count + 1
    
print ('ค่าต่ำสุดคือ:',min)
print ('ค่าสูงสุดคือ:',max)
result = sum/count
print('ค่าเฉลี่ยคือ:',result)