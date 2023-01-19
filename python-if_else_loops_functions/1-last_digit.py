#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
if (number > 0 and number > 5) :
    print(f"Last digit of {number} is {number %10} and is greater than 5")
elif (0 < number < 6):
    print(f"Last digit of {number} is {number %10} and is less than 6 and not 0")
elif (number %10 == 0) :
    print(f"Last digit of {number} is {number %10} and is 0")
elif (number < 0) :
    n = (number * -1 ) %10
    print(f"Last digit of {number} is {n * -1} and is less than 6 and not 0")
