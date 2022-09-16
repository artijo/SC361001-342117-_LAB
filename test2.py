cars = [('citroen', 'xsara', 1100), ('lincoln', 'navigator', 2000), ('bmw', 'x5', 1700)]

print(sorted(cars, key=lambda k: k[0]))
print(sorted(cars, key=lambda k: k[1]))
print(sorted(cars, key=lambda k: k[2]))