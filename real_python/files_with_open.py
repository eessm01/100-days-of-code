"""Real Python tutorial. Working with files in Python.

Python's "with open(...) as ...." Pattern
"""

with open('21daysOfAbundance.txt','r') as f:
    data = f.read()

print(data)


with open('21daysOfAbundance_day6.txt', w) as f:
    data = 'everything I desire, is within me.'
    f.write(data)