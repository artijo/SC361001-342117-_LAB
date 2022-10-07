def print_square(width=6, length=0):
    if length == 0:
        length = width
    for i in range(1,length+1):
        if i == 1 or i == length:
            print('#'*width)
        else:
            print('#',' '*(width-4),'#')

def print_triangle (width, length=0):
    if length == 0:
        length = width
    # k = 1
    # for i in range(1,length+1):
    #     if i == 1 or i == 2 or i == length:
    #         print('#'*i)
    #     elif i ==3 :
    #         print('#'+'','#')
    #     else:  
    #         print('#'+' '*k,'#')
    #         k+=1
    print(width)
    print(length)
    print("#")
    for i in range(length):
        print("#",end="")
        for j in range(width+1):
            if(j == width):
                print(" "*j+"#")
    print("#"*width)
print_triangle(6,10)