import string
import random

characters = string.ascii_letters + string.digits + string.punctuation

while True:
    try:
        length = int(input("Password length? "))
        if length <= 0:
            print("Enter a number greater than 0")
            continue
        break
    except ValueError:
        print("Enter a valid number")

password = "".join(random.choice(characters) for _ in range(length))

print("Your password:", password)