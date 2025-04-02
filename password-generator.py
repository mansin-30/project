import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security!")
        return None

    # Define character sets
    lower = string.ascii_lowercase   # a-z
    upper = string.ascii_uppercase   # A-Z
    digits = string.digits           # 0-9
    special = string.punctuation     # Special characters

    # Ensure password has at least one of each type
    all_chars = lower + upper + digits + special
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)

    # Fill the rest of the password length with random choices
    password += ''.join(random.choices(all_chars, k=length-4))

    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))

    return password

# User input for password length
try:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Invalid input! Please enter a number.")