text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count_vowels = 0
count_consonants = 0
count_spaces = 0
count_others = 0

for char in text:
    if char in vowels:
        count_vowels += 1
    elif char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":  
        count_consonants += 1
    elif char == " ": 
        count_spaces += 1
    else:  
        count_others += 1

print("Vowels:", count_vowels)
print("Consonant:", count_consonants)
print("Spaces:", count_spaces)
print("Other characters:", count_others)