def calculate_final_grade(cs, me):
    return cs * 0.6 + me * 0.4


def load_records(filename="ACTIVITY 4/records.txt"):
    try:
        with open(filename) as file:
            return [dict(zip(["id", "name", "cs", "me"], [p[0], (p[1], p[2]), float(p[3]), float(p[4])])) for p in (line.strip().split(",") for line in file)]
    except FileNotFoundError:
        return []


def save_records(records, filename="ACTIVITY 4/records.txt"):
    with open(filename, "w") as file:
        file.writelines(f"{r['id']},{r['name'][0]},{r['name'][1]},{r['cs']},{r['me']}\n" for r in records)


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
    records = load_records()
    while True:
        choice = input("\nSTUDENT RECORD MANAGEMENT:\n1. Show by Name\n2. Show by Grade\n3. Show Student Record\n4. Add Record\n5. Edit Record\n6. Delete Record\n7. Exit\nChoice: ")
        if choice in "12":
            display_records(records, "name" if choice == "1" else "grade")
        elif choice == "3":
            modify_record(records, "show")
        elif choice in "45":
            records = add_record(records) if choice == "4" else modify_record(records, "edit")
            save_records(records)
        elif choice == "6":
            records = modify_record(records, "delete")
            save_records(records)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()