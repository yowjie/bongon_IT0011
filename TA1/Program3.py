#nested for statement 
for i in range(1, 6):  
    print(" " * (5 - i), end="") 
    for j in range(1, i + 1):  
        print(j, end="")     
    print()  

print(end="\n")

#nested while statement
i = 1  
while i < 5:  
    j = 1
    while j <= i * 2 - 1:  
        print(i * 2 - 1, end="")  
        j += 1  
    print()  

    if i == 3:  
        k = 1
        while k <= 6:  
            print("6", end="")  
            k += 1  
        print()

    i += 1   


