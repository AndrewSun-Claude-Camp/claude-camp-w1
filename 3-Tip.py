# Tip calculator
def get_number(prompt, min_value=0, max_value=None):
    while True:
        try:
            value = float(input(prompt))

            if value <= min_value:
                print(f"Invalid input. Value must be more than {min_value}.")
            elif max_value is not None and value > max_value:
                print(f"Invalid input. Value must be no more than {max_value}.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


amount = get_number("Enter the bill amount: ")
tip_percentage = get_number("Enter the tip percentage: ", 0, 100)

tip_amount = amount * tip_percentage / 100
total_amount = amount + tip_amount

print(f"Bill amount: ${amount:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount: ${total_amount:.2f}")