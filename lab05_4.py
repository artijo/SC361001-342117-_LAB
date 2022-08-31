grade = float(input('กรุณากรอกคะแนนสะสม: '))
if (grade >= 3.25 and grade <= 4.00):
    print('Result : คะแนนเฉลี่ยของคุณอยู่ในเกณฑ์\tดีมาก')
elif (grade >= 2.75 and grade < 3.25):
    print('Result : คะแนนเฉลี่ยของคุณอยู่ในเกณฑ์\tดี')
elif (grade >= 2.00 and grade <2.75):
    print('Result : คะแนนเฉลี่ยของคุณอยู่ในเกณฑ์\tพอใช้')
elif (grade >= 0 and grade < 2.00):
    print('Result : คะแนนเฉลี่ยของคุณอยู่ในเกณฑ์\tปรับปรุง')
else:
    print('**ช่วงของเรก คือ 0 - 4.00**')

if (grade > 3.25): 
    gradeD = input('คุณเคยได้รับ D หรือไม่(Y/N): ')
    if (grade >= 3.25 and grade < 3.60):
        if (gradeD == 'N' or gradeD == 'n'):
            print('ขอแสดงความยินดี คุณได้รับเกียรตินิยมอันดับสอง')
    if (grade >= 3.60 and grade <= 4.00):
        if (gradeD == 'N' or gradeD == 'n'):
            print('ขอแสดงความยินดี คุณได้รับเกียรตินิยมอันดับหนึ่ง')
print('ขอบคุณที่ใช้บริการ')