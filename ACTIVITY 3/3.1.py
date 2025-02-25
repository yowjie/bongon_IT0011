fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

full = fname + " " + lname
sli = fname[:3] 

print()
print("Full Name:", full)
print("Sliced Name:", sli)
print(f"Hello, {sli}! Welcome. You are {age} years old.")

