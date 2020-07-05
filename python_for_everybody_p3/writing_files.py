"""Python for everoutput.ybody. Writing files."""


# If the file already exists, opening it in write 
# mode clears out the old data and starts fresh, 
# so be careful! If the file doesn’t exist, a new 
# one is created, or replace if exists.
fout = open('output.txt', 'w')
print(fout)

# The write ethod of the file handle object puts data
# into the file, returning the number of characters 
# written.
line1 = 'Day 3.\n'
line2 = 'Today, I focus on what I want to attract into my life.\n'
num_characters = fout.write(line1)
num_characters = fout.write(line2)

# When you are done writing, you have to close the file to make sure 
# that the last bit of data is physically written to the disk so it 
# will not be lost if the power goes off.
fout.close()
print(num_characters)