#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
greater = "and is greater than 5"
zero = "and is 0"
less = "and is less than 6 and not 0"

if number < 0:
    lastDigit = number % -10
else:
    lastDigit = number % 10

if lastDigit > 5:
    print("{} {:d} is {:d} {}".format(string, number, lastDigit, greater))
elif lastDigit == 0:
    print("{} {:d} is {:d} {}".format(string, number, lastDigit, zero))
else:
    print("{} {:d} is {:d} {}".format(string, number, lastDigit, less))
