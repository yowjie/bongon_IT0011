def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(folder):
    try:
        with open(f"{folder}/numbers.txt",'r') as file:
            for i, line in enumerate(file, 1):
                total = sum(map(int, line.strip().split(',')))
                print(f"Line {i}: {line.strip()} (sum {total}) - {'Palindrome' if is_palindrome(total) else 'Not a palindrome'}")
                if i == 10:
                    break
    except FileNotFoundError:
        print("File not found. Please check the filename.")

process_file("MIDTERM_TECHNICAL")
