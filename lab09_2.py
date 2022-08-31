mySubject = []
myScore = []
i = 0
while i<5:
    subject = input('กรุณาป้อนชื่อวิชา: ')
    score = int(input('กรุณาป้อนคะแนนวิชา {} : ' .format(subject)))
    mySubject.append(subject)
    myScore.append(score)
    i+=1

sMax = max(myScore)
subMax = myScore.index(sMax)

sMin = min(myScore)
subMin = myScore.index(sMin)

print('วิชาที่ได้คะแนนสูงสุดคือ',mySubject[subMax],'ได้',sMax,'คะแนน')
print('วิชาที่ได้คะแนนต่ำสุดคือ',mySubject[subMin],'ได้',sMin,'คะแนน')