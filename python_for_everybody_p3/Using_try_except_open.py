"""Python for everyone. Using try, except, and open
"""

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: {}'.format(fname))
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1

print('There were {} subject lines in {}'.format(
    count, fname
))