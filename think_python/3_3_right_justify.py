""" This program is a solution for:
    Exercise 3.3. Python provides a built-in function called len that returns the length of
    a string, so the value of len('allen') is 5. Write a function named right_justify that 
    takes a string named s as a parameter and prints the string with enough leading spaces 
    so that the last letter of the string is in column 70 of the display.
    right_justify('allen')
"""


def right_justify(string):
    length = len(string)
    new_string = (' '*(70 - length) ) + string
    print(new_string)
    print(len(new_string))


if __name__ == "__main__":
    string = input('Introduce la cadena: ')
    right_justify(string)