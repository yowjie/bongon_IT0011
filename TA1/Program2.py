text = input("Enter a string with digits: ")

sum_digits = 0

for char in text: 
    if '0' <= char <= '9':  
        sum_digits += int(char) 

print("Sum of digits:", sum_digits)
