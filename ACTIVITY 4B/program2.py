import csv
def exchange_rates(filename):
    rates, names = {}, {}
    with open(filename, 'r', encoding='ISO-8859-1') as file:
        reader = csv.reader(file)
        next(reader)
        for code, name, rate in reader:
            rates[code] = float(rate)
            names[code] = name
    return rates, names

def main():
    rates, names = exchange_rates("ACTIVITY 4B/currency.csv")
    amount = float(input("How much dollar do you have? "))
    currency = input("What currency do you want to have? ").upper()
    
    if currency in rates:
        converted = amount * rates[currency]
        amount_display = int(amount)
        print(f"\nDollar: {amount_display} USD")
        print(f"{names[currency]}: {converted:.9f} ")
    else:
        print("Currency not found.")

if __name__ == "__main__":
    main()
    
    