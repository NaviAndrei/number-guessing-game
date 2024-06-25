# Number Guessing Game

import random
import time

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 10 tries to guess it.
""")

a = input("Enter a number between 1 and 100: ")
while not a.isnumeric():
    a = input("Invalid input. Please enter a number: ")

while (int(a) < 1) or (int(a) > 100):
    a = input("Invalid input. Please enter a number between 1 and 100: ")


b = random.randint(1, 100)  # generates a random number between 1 and 100
n = 0
time.sleep(1)

while (int(a) != b) and n < 10:
    if int(a) > b:
        print("Too high, try again.")
    else:
        print("Too low, try again.")
    n += 1
    print("You have " + str(10 - n) + " tries left.")
    if str(10 - n) == "0":
        print("You have run out of tries. The number was " + str(b) + ".")
        print("Thanks for playing!")
        exit(1)
    a = input("Enter a number between 1 and 100: ")
    time.sleep(1)
    if int(a) == b:
        print("Congratulations! You guessed it correctly.")
        print("Thanks for playing!")
        exit(1)
