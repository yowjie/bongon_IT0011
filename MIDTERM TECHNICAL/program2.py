def format_date(date_str):
    try:
        month, day, year = map(int, date_str.split("/"))
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return months[month - 1] + " " + str(day) + ", " + str(year)
    except (ValueError, IndexError):
        return "Invalid date format."

date_input = input("Enter date (mm/dd/yyyy): ")
print("Date Output:", format_date(date_input))
