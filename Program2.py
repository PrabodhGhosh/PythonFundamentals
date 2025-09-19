"""Countdown Program

A program that asks the user for a number and prints
a countdown from that number down to zero.
"""

# Get number from user
number = int(input("Enter your number: "))

# Print countdown from entered number to zero
for i in range(number, -1, -1):
    print(i)