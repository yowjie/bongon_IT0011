text = input("Enter a string with digits: ")

sum_digits = 0

for x in text: 
    if "0" <= x <= "9":  
        sum_digits += int(x) 

print("Sum of digits:", sum_digits)
