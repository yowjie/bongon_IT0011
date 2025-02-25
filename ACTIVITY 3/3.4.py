try:
    with open("ACTIVITY 3/students.txt", "r") as file:
        content = file.read()
        print("\nReading Student Information:\n" + (content if content else "The file is empty."))
except FileNotFoundError:
    print("Error: 'students.txt' not found in 'ACTIVITY 3' folder.")
