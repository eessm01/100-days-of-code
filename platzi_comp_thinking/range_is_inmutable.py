# range(comienzo, fin, pasos)
my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)

range1 = range(0, 7, 2)
range2 = range(0, 8, 2)

# value equality
print(range1 == range2)

print(id(range1))
print(id(range2))

# object equality
print(range1 is range2)


# challenge none numbers, 1 to 99
for i in range(1, 100, 2):
    print(i)