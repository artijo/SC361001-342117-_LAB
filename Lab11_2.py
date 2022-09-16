#problem 2
num1 = [10, 11, 15, 12, 9, 14, 7]
num1 = sorted(num1)
num2 = [12, 5, 9, -3]
num2 = sorted(num2)
# print(num1)
def lostNum(pm):
    ls = []
    for i in range(pm[0],pm[-1]+1):
        if i not in pm:
            i=str(i)
            ls.append(i)
            # print(i)
    return ls
    # print(pm[-1])
# print(type(lostNum(num1)))
print('Lost numbers contain:',', '.join(lostNum(num1)))
print('Lost numbers contain:',', '.join(lostNum(num2)))