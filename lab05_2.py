price = int(input('Please Enter Product Pirce: '))
if (price > 100):
    vat = ((price*7)/100)
    print('===== CP Supermarket =====\nProduct Price is',price,'\nTotal',price+vat)
else:
    print('===== CP Supermarket =====\nProduct Price is',price,'\nTotal',price)