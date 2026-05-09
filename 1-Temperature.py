# Convert between Celsius and Fahrenheit. Decimal precision set to 1000 significant digits 
from decimal import Decimal, InvalidOperation, getcontext
getcontext().prec = 1000

def get_valid_choice():
    while True:
        choice = input("Select conversion type (1 or 2): ")
        if choice in ["1","2"]:
            return choice
        else:
            print("Invalid selection. Please choose 1 or 2.")

def get_valid_temperature():
    while True:
        try:
            return Decimal(input("Enter temperature value: "))
        except InvalidOperation:
           print("Invalid input. Please enter a numeric temperature value.")

print("Temperature Converter\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")

choice = get_valid_choice()
temperature = get_valid_temperature()

if choice == "1":
    result = temperature * Decimal("9") / Decimal("5") + Decimal("32")
    print(f"{temperature:.2f}°C = {result:.2f}°F")
elif choice == "2":
    result = (temperature - Decimal("32")) * Decimal("5") / Decimal("9")
    print(f"{temperature:.2f}°F = {result:.2f}°C")
