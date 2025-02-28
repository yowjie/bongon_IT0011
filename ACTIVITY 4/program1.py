import os

def calculate_final_grade(cs, me):
    return cs * 0.6 + me * 0.4


def load_records():
    filename = input("Enter filename to open: ")
    try:
        with open(filename) as file:
            records = [dict(zip(["id", "name", "cs", "me"], [p[0], (p[1], p[2]), float(p[3]), float(p[4])])) for p in (line.strip().split(",") for line in file)]
        print(f"File '{filename}' loaded successfully!")
        return records, filename  
    except FileNotFoundError:
        print("File not found.")
        return [], ""  


def save_records(records, filename):
    with open(filename, "w") as file:
        file.writelines(f"{r['id']},{r['name'][0]},{r['name'][1]},{r['cs']},{r['me']}\n" for r in records)
    print("Records saved!")


def save_as_records(records):
    filename = input("Enter filename to save as: ")
    filepath = os.path.join("ACTIVITY 4", filename)
    with open(filepath, "w") as file:
        file.writelines(f"{r['id']},{r['name'][0]},{r['name'][1]},{r['cs']},{r['me']}\n" for r in records)
    print("The file is saved.")
    return filepath  


def display_records(records, order_by="name"):
    records.sort(key=lambda r: r["name"][1] if order_by == "name" else -calculate_final_grade(r["cs"], r["me"]))
    print("\nStudent Records:")
    for r in records:
        print(f"ID: {r['id']}, Name: {r['name'][0]} {r['name'][1]}, Final Grade: {calculate_final_grade(r['cs'], r['me']):.2f}")


def modify_record(records, action):
    student_id = input("Enter Student ID: ")
    record = next((r for r in records if r["id"] == student_id), None)
    if not record:
        print("Record not found.")
        return records
    
    if action == "show":
        print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Final Grade: {calculate_final_grade(record['cs'], record['me']):.2f}")
    
    elif action == "edit":
        record["cs"], record["me"] = float(input("New Class Standing: ")), float(input("New Major Exam: "))
        print("Record updated!")
    
    elif action == "delete":
        records.remove(record)
        print("Record deleted.")
    
    return records


def add_record(records):
    student_id = input("Enter 6-digit Student ID: ")
    if len(student_id) != 6 or not student_id.isdigit():
        print("Invalid ID.")
        return records
    records.append({"id": student_id, "name": (input("First Name: "), input("Last Name: ")), "cs": float(input("Class Standing: ")), "me": float(input("Major Exam: "))})
    print("Record added!")
    return records


def main():
    records = []
    filename = "records.txt"  
    while True:
        choice = input("\nSTUDENT RECORD MANAGEMENT:\n"
                       "1. Open File\n"
                       "2. Save File\n"
                       "3. Save As File\n"
                       "4. Show All Students Record\n"
                       "5. Order by Last Name\n"
                       "6. Order by Grade\n"
                       "7. Show Student Record\n"
                       "8. Add Record\n"
                       "9. Edit Record\n"
                       "10. Delete Record\n"
                       "11. Exit\nChoice: ")

        if choice == "1":
            records, filename = load_records()
        elif choice == "2":
            if filename:
                save_records(records, filename)
            else:
                print("No file opened. Use 'Save As' first.")
        elif choice == "3":
            filename = save_as_records(records)  
        elif choice == "4":
            display_records(records)  
        elif choice == "5":
            display_records(records, "name")  
        elif choice == "6":
            display_records(records, "grade")  
        elif choice == "7":
            modify_record(records, "show")  
        elif choice == "8":
            records = add_record(records)
            if filename:
                save_records(records, filename)  
        elif choice == "9":
            records = modify_record(records, "edit")
            if filename:
                save_records(records, filename)  
        elif choice == "10":
            records = modify_record(records, "delete")
            if filename:
                save_records(records, filename)  
        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
