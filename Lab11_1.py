def checked_miror(pm):
    mirror = []
    for i in pm:
        if i.lower() == i.lower()[::-1]:
            mirror.append(i)
            # print('Mirror words:',i)
    # print(mirror)
    print('Mirror words:',', '.join(mirror))

#problem1
list_input = ["aloha", "wow", "Level", "step on no pets"]

# for i in list_input:
#     print(i[::-1])
checked_miror(list_input)

list_input = ["mom", "cat", "suMmer", "Civic"]
checked_miror(list_input)



