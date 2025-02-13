def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(folder):
    try:
        with open(f"{folder}/numbers.txt", 'r') as file:
            for i, line in enumerate(file, start=1):
                numbers = list(map(int, line.strip().split(',')))
                total = sum(numbers)
                result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
                print(f"Line {i}: {','.join(map(str, numbers))} (sum {total}) - {result}")
                if i == 10:
                    break
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# Example usage
process_file("MIDTERM_TECHNICAL")
