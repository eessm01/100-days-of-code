"""Python for everyone. Reading Files
"""


fhand = open('mbox.txt')
print(fhand)

# Because the for loop reads the data one line at a time, it can efficiently 
# read and count the lines in very large files without running out of main 
# memory to store the data.
fhand = open('mbox.txt')
count = 0

for line in fhand:
    count += 1
    # print(line)

print('Line Count: {}'.format(count))


# If you know the file is relatively small compared to the size of your main 
# memory, you can read the whole file into one string using the read method
# on the file handle.
fhand = open('mbox-short.txt')
# In this example, the entire contents (all 94,626 characters) of the file 
# mbox-short.txt are read directly into the variable inp. 
# all of the lines and newline characters are one big string in the variable
# inp
inp = fhand.read()
print(len(inp))

print(inp[:20])

print(len(fhand.read()))


# Remember that this form of the open function should only be used if the file 
# data will fit comfortably in the main memory of your computer. If the file 
# is too large to fit in main memory, you should write your program to read 
# the file in chunks using a for or while loop.