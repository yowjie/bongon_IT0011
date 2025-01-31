#nested for statement 
print(end="a. Nested for statement: ")
print()
for x in range(1, 6):  
    print(" " * (5 - x), end="") 
    for y in range(1, x + 1):  
        print(y, end="")     
    print()  

print()

#nested while statement
print(end="b. Nested while statement: ")
print()
x = 1  
while x < 5:  
    y = 1
    while y <= x * 2 - 1:  
        print(x * 2 - 1, end="")  
        y += 1  
    print()  

    if x == 3:  
        y = 1
        while y <= 6:  
            print("6", end="")  
            y += 1  
        print()

    x += 1   


