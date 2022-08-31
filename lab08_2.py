text = input('Enter your Char: ')
text = text.upper()
a = text.count('A')
b = text.count('B')
lOther = 'CDEFGHIJKLMNOPQRSTUVWXYZ'
sumother = 0
for i in lOther:
    other = text.count(i)
    sumother = sumother + other


print('A:',a)
print('B:',b)
# print(type(a))
print('Other',sumother)