#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modnu = abs(number) % 10
if number < 0:
    modnu *= -1
if modnu == 0:
    print("Last digit of", number, "is", modnu, "and is 0")
elif modnu > 5:
    print("Last digit of", number, "is", modnu, "and is greater than 5")
else:
    print("Last digit of", number, "is", modnu, "and is less than 6 and not 0")
