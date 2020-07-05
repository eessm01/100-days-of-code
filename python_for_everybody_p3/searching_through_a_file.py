"""Python for everyone. Searching in a file

When you are searching through data in a file, 
it is a very common pattern to read through a 
file, ignoring most of the lines and only 
processing lines which meet a particular 
condition
"""

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)


# As your file processing programs get more complicated, 
# you may want to structure your search loops using 
# continue. The basic idea of the search loop is that 
# you are looking for “interesting” lines and effectively 
# skipping “uninteresting” lines. And then when we find 
# an interesting line, we do something with that line.

print('Other form for search')
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # Skip uninteresting lines
    if not line.startswith('From:'):
        continue
    # process our interesting line
    print(line)




print('Searching someone come from the University of Cape Twon')
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)
