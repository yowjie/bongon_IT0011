word = input("Enter a string: ")

#vowels
vowels = ["a", "e", "i", "o", "u"]
count = 0
for character in word:
    if character in vowels:
        count += 1

#consonant
vowels = ["a", "e", "i", "o", "u"]
count1 = 0
for character in word:
    if character in vowels:
        count += 1
    elif character in vowels:
        c

print("Vowels:", count)
print("Consonant:", count1)