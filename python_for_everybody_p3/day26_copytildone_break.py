"""The program echoes whatever the user types, if the user
types done, the break statement exists the loop.
"""

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')