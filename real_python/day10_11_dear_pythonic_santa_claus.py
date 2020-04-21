#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Exercises from https://realpython.com/python-thinking-recursively/
The algorithm for interative present delivery implemented in Python

Now that we have some intuition about recursion, let's introduce the formal
definition of a recursive function. A recursive function is a function defined
in terms of itself via self-referencial expressions.

This means that the function will continue to call itself and repeat its
behavior until some condition is met to return a result. All recursive 
functions share a common structure made up of two parts: 
1. base case  
2. recursive case.
"""

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively():
    for house in houses:
        print("Delivering present to", house)


# deliver_presents_iteratively()


# Each function call represents an elf doing his work
def deliver_presents_elves_iteratively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_elves_iteratively(first_half)
        deliver_presents_elves_iteratively(second_half)


deliver_presents_elves_iteratively(houses)



# Recursive function for calculating n! implemented in Python
def factorial_recursive(n):
    #Base case: 1! = 1
    if n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

factorial = factorial_recursive(8)
print(factorial)
