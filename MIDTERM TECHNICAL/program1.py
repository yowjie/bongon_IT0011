def is_palindrome(num):
    return str(num) == str(num)[::-1]

def process_file(numbers):
    
    try:
        with open(numbers, 'r') as file:
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not Palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
    except Exception as e:
        print(f"Error: {e}")
        
process_file("numbers.txt")

