"""Python for everybody.

Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
"""

fname = input('Enter a file name: ')

if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened')
    exit()

count = 0
total_spam = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        total_spam += float(line[20::])

print('Average spam confidence: {}'.format(
    total_spam / count
))