scores = {"231": 77, "942": 80, "253": 51, "146": 65, "258": 91, "229": 87, "354": 88}
numEven = []
sum = 0
scoreSort = sorted(scores.keys(),reverse=True)
#print(scoreShort)
for i in scoreSort:
    i=int(i)
    if i%2 == 0:
        #sum = sum+i
        i=str(i)
        numEven.append(i)
        sum = sum + scores[i]
#print(numEven)
print ('Number of even id =',len(numEven))
print ('Even id :',', '.join(numEven))

# for i in numEven:
#     sum = sum + scores[i]
print ('Average score of even id =',sum/len(numEven))
