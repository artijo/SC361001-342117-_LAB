countA = 0
countB = 0
countO = 0
while True:
    word = input('Input A-Z (if to stop input Y): ')
    word = word.upper()
    if (word == 'Y'):
        break
    elif (word == 'A'):
        countA = countA+1
    elif (word == 'B'):
        countB = countB+1
    else:
        countO = countO+1

print('A:',countA)
print('B:',countB)
print('Other:',countO)