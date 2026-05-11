#!/usr/bin/python3
"""Fizz Buzz

Print numbers from 1 to 100 with Fizz/Buzz rules.
"""

def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three print Fizz instead of the number and for
    multiples of five print Buzz. For multiples of both three and five
    print FizzBuzz. Each element is followed by a space.
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


if __name__ == "__main__":
    fizzbuzz()
