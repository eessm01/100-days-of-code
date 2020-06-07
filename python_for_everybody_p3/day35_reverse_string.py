"""Print words of a string in reverse order.

Write a while loop that starts at the last character in the 
string and works its way backwards to the first character in 
the string, printing each letter on a separate line, except 
backwards.
"""

word = 'Este es un gato flaco'
index = len(word) -1

while index >= 0:
    letter = word[index]
    print(letter, end='')
    index -= 1

# other form
print()
print(word[::-1])

