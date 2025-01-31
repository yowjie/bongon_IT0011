text = input("Enter a string: ")

vowels = "aeiouAEIOU"
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

count_vowels = 0
count_consonants = 0
count_spaces = 0
count_others = 0

for x in text:
    if x in vowels:
        count_vowels += 1
    elif x in alphabets and x not in vowels:  
        count_consonants += 1
    elif x == " ": 
        count_spaces += 1
    else:  
        count_others += 1
        
print()
print("Vowels:", count_vowels)
print("Consonant:", count_consonants)
print("Spaces:", count_spaces)
print("Other characters:", count_others)