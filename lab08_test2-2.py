text = input('Enter your Char: ')
text = text.upper()
a = text.count('A')
b = text.count('B')
other = len(text)-(text.count('A')+(text.count('B')))
print('A:',a)
print('B:',b)
print('Other:',other)