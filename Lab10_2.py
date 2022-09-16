text = "Structured Programming for Information Technology".lower().replace(" ","")
text = sorted(text)
print(text)
ctext = {}
#print(text)
for i in text:
    #x = text.count(i)
    ctext.setdefault(i,text.count(i))
    # text.replace(i,"")
# x = (sorted(ctext.values(),reverse=True))
# print(ctext.items())

#ctext = sorted(ctext)
resualts = {k: v for k, v in sorted(ctext.items(), key=lambda item: item[1], reverse=True)}
#print (resualts)
#print(ctext)

for key in resualts:
    print(key,':',resualts[key])
