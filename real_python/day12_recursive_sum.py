#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Let's calculate 1 + 2 + 3 ... + 10 using recursion.
The state that we have to maintain is (current number we adding, accumulated sum
till now)
"""

def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(
                    current_number + 1, 
                    accumulated_sum + current_number
               )


sum_recursive = sum_recursive(1,0)
print(sum_recursive)
