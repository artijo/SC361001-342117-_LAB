while True:
    score = input('กรุณากรอกคะแนน ถ้าต้องการหยุดการทำงานให้ตอบ (N/n): ')
    if (score == 'n' or score == 'N'):
        print('สิ้นสุดการทำงาน')
        break
    else:
        score = int(score)
        if (score >= 80 and score <=100):
            print('เกรดของคุณคือ A')
        elif (score >= 75 and score < 80):
            print('เกรดของคุณคือ B+')
        elif (score >= 70 and score < 75):
            print('เกรดของคุณคือ B')
        elif (score >= 65 and score < 70):
            print('เกรดของคุณคือ C+')
        elif (score >= 60 and score < 65):
            print('เกรดของคุณคือ C')
        elif (score >= 55 and score < 60):
            print('เกรดของคุณคือ D+')
        elif (score >= 50 and score < 55):
            print('เกรดของคุณคือ D')
        else:
            print('เกรดของคุณคือ F')