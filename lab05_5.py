score = float(input('กรุณากรอกคะแนน: '))
if (score >= 80 and score <=100):
    print('คะแนนของคุณคือ',int(score))
    print('เกรดของคุณคือ A')
elif (score >= 75 and score < 80):
    print('คะแนนของคุณคือ',int(score))
    print('เกรดของคุณคือ B+')
elif (score >= 70 and score < 75):
    print('คะแนนของคุณคือ',int(score))
    print('เกรดของคุณคือ B')
elif (score >= 65 and score < 70):
    print('คะแนนของคุณคือ',int(score))
    print('เกรดของคุณคือ C+')
elif (score >= 60 and score < 65):
    print('คะแนนของคุณคือ',int(score))
    print('เกรดของคุณคือ C')
elif (score >= 55 and score < 60):
    print('คะแนนของคุณคือ',int(score))
    print('เกรดของคุณคือ D+')
elif (score >= 50 and score < 55):
    print('คะแนนของคุณคือ',int(score))
    print('เกรดของคุณคือ D')
elif (score < 50 and score >= 0):
    print('คะแนนของคุณคือ',int(score))
    print('เกรดของคุณคือ F')
else:
    print('**ช่วงของคะแนน คือ 0-100**')