"""All the lines are printed except the one that starts
with the hash sign because when the continue is executed,
it ends the current iteration and jumps back to the while
statement to start the next iteration, thus skipping the
print statement.
"""

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')