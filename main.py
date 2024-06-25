# Number Guessing Game

import random
import time

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 10 tries to guess it.
""")

a = input("Enter a number between 1 and 100: ")
b = random.randint(1, 100)  # generates a random number between 1 and 100
n = 0
time.sleep(1)

while (int(a) != b) and n < 10:
    if int(a) > b:
        print("Too high, try again.")
    else:
        print("Too low, try again.")
    n = n + 1
    print("You have " + str(10 - n) + " tries left.")
    a = input("Enter a number between 1 and 100: ")
    time.sleep(1)

print("Congratulations! You guessed it correctly.")
print("Thanks for playing!")
