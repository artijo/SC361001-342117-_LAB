month = {3:"MAR", 1:"JAN", 2:"FEB"}
for key in sorted(month.keys()):
    print(key, month[key])
    print("============")

for val in sorted(month.values()):
    list_value = list(month.values())
    index = list_value.index(val)
    list_key = list(month.keys())
    print(list_key[index], val)