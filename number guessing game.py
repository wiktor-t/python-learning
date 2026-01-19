import random

number = random.randint(1, 10)

guess = int(input("Pick a number between 1 and 10: "))

if guess == number:
    print("Correct!")
else:
    print("Incorrect. The number was", number)