fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

print()
full = fname + " " + lname
print("Full Name:", full)

sli = fname[:3]
print("Sliced Name:", sli)

print("Greeting Message: Hello,", sli + "!", "Welcome. You are", age, "years old.")
