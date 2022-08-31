myList = []
while True:
    i = input('ป้อน (A) เพื่อเพื่มรายวิชา\nป้อน (D) เพื่อลบรายวิชา\nป้อน (P) เพื่อแสดงรายวิชาทั้งหมด\nป้อน (Y) เพื่อจบการทำงาน\n')
    if i == 'y' or i == 'Y':
        print('ปิดโปรแกรมแล้ว!')
        break
    if i == 'a' or i == 'A':
        subject = input('กรุณาป้อนชื่อวิชา: ')
        myList.append(subject)
        print('เพิ่มวิชา',subject,'เรียบร้อยแล้ว')
    if i == 'd' or i == 'D':
        while True:
            rmSubject = input('กรุณาป้อนชื่อวิชาที่ต้องการลบ ต้องการยกเลิกป้อน (B) : ')
            if rmSubject == 'b' or rmSubject == 'B':
                break
            if rmSubject in myList:
                rmCheck = input('คุณต้องการลบวิชา {} ใช่ไหม (Y/N): ' .format(rmSubject))
                if rmCheck == 'Y' or rmCheck == 'y':
                    myList.remove(rmSubject)
                    print('ลบวิชา',rmSubject,'แล้ว')
                    break
                elif rmCheck == 'N' or rmCheck == 'n':
                    continue
                else:
                    print('ทำรายการไม่ถูกต้อง')
            else:
                print('ไม่พบรายวิชานี้ กรุณาทำรายการใหม่อีกครั้ง')
    if i == 'p' or i == 'P':
        print('รายวิชาในระบบทั้งหมด\n',myList)
