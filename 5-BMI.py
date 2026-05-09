# BMI Calculator

def get_valid_number(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))

            if value < min_value or value > max_value:
                print(f"Invalid input. Please enter a value between {min_value} and {max_value}.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a numeric value.")



height = get_valid_number("Enter your height in meters: ", 0.5, 2.5)
weight = get_valid_number("Enter your weight in kilograms: ", 2, 500)

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")