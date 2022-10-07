def checkZero(qty,line,items):
    if int(qty)<0:
        with open('sales.txt', 'r') as file:
            data=file.read()
        newdata=data.replace(qty,'1');
        with open('sales.txt', 'w') as file:
            file.write(newdata)
    assert int(qty)>0, "Check data at line {} {}".format(line,items)
    
try:
    products={}
    c=1
    with open("sales.txt", encoding = 'utf-8') as f:
        f.seek(40,0)
        for i in f: 
            c+=1
            i=i.strip()
            if(len(i.split(', '))<4):
                print('At line {}, an invalid data is found, and it was skipped. [{}]'.format(c,i))
            else:
                receipt, product, unit_price, quantity=i.split(', ')
                checkZero(quantity,c,i)
                detail={}
                if product not in products:
                    detail["unit_price"]=int(unit_price)
                    detail["quantity"]=int(quantity)
                    products[product]=detail
                else:
                    products[product]["quantity"]+=int(quantity)

    print("The data in file constain {} orders".format(len(products)))
    print("="*40)
    total_price=0
    for k,v in products.items():
        total_price+=v["unit_price"]*v["quantity"]
        print("{} x {} items x {} baht = {} baht".format(k,v["quantity"],v["unit_price"],v["unit_price"]*v["quantity"]))
    print("="*40)
    print("Total sales {} baht".format(total_price))
    
                
except FileNotFoundError:
  print("file does not exist :(")
