sUnit = 0
sUA = 0
while True:
    Unit = float(input('กรุณาป้อนหน่วยกิต (จบการทำงานกรอก 0): '))
    if Unit == 0:
        break
    Grade = float(input('กรุณากรอกเกรด: '))
    sUnit = sUnit+Unit
    sum = Unit*Grade
    sUA = sUA+ sum

result = sUA/sUnit
print('GPA:',round(result,2))