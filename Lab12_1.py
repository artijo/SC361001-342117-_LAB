

# choose 1 sentence for test
sentence = "Hello World!!".replace(" ","")
x = filter(lambda m:m.isupper(),sentence)
print ('Upper letters:',', '.join(x))
sentence = "OMG, Program Error!".replace(" ","")
x = filter(lambda m:m.isupper(),sentence)
print ('Upper letters:',', '.join(x))
