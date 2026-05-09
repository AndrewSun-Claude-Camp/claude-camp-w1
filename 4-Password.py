# Password Generator

import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("Enter the password length: "))

            if length <= 0:
                print("Invalid input. Password length must be greater than 0.")
            else:
                return length

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

length = get_password_length()
password = generate_password(length)

print(f"Generated password: {password}")