grade = float(input('Please Enter Product Your Grade: '))
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