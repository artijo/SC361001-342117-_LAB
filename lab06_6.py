i = 1
personal = "1"
van = "2"
truck = "3"
count_personal = 0
count_van = 0 
count_truck = 0
fee = 0

while i<=5 :
    name = input('กรุณากรอกรหัสรถยนต์: ')
    if (name == personal):
        fee = fee+40
        count_personal +=1
    if (name == van):
        fee = fee + 60
        count_van +=1
    if (name == truck):
        fee = fee + 80
        count_truck +=1
    i+=1
    
print ('รถ 5 คันแบ่งเป็น')
print ('- รถยนต์ส่วนบุคคล',count_personal,'คัน')
print ('- รถตู้',count_van,'คัน')
print ('- รถยนต์บรรทุก',count_truck,'คัน')
print ('ค่าผ่านทางรวมทั้งหมด',fee,'บาท')