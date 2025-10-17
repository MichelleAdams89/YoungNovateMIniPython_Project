import random
import string

length = int(input("Enter the desired password length: "))
include_special = input("Do you want to include special characters? (yes/no): ").lower()

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

if include_special == "yes":
    all_characters = letters + digits + special_chars
else:
    all_characters = letters + digits

password = ''.join(random.choice(all_characters) for _ in range(length))

print("\nYour generated password is:", password)
print("\nYour generated password is:", password)