"""Python for everybody.

Exercise 1: Write a program to read through a 
file and print the contents of the file (line 
by line) all in upper case. Executing the 
program will look as follows:
"""

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File not found')
    exit()

for line in fhand:
    print(line)

