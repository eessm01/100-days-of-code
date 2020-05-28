"""To compute the smallest number
"""

smallest = None

for intervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or intervar < smallest:
        smallest = intervar
    print('Loop: ', intervar, smallest)
print('Smallest: ', smallest)