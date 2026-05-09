# Print a greeting message using the provided name and age.
import re

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
        elif len(name) > 50:
            print("Name cannot exeed 50 characters. Please try again.")
        elif not re.match(r"^[A-Za-z\s\-']+$", name):
            print("Name can only contain letters, space, hyphens, or apostrophes. Please try again.")
        else:
            return name

def get_valid_age():
    while True:
        age = (input("Enter your age: ")).strip()
        if not age.isdigit():
            print("Age must be a whole number. Please try again.")
        elif int(age) < 0:
            print("Age cannot be negative. Please try again.")
        elif int(age) > 150:
            print("Age cannot exceed 150. Please try again.")
        else:
            return int(age)

name = get_valid_name()
age = get_valid_age()
print(f"Hello, {name}! You are {age} years old. Welcome!")
