"""Python for everyone. Letting the user choose the file name
"""

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0

for line in fhand:
    if line.startswith('Subject:'):
        print(line)
        count += 1
    
print('There were {} subject lines in {}'.format(
    count, fname
))