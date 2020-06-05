a = [1, 2, 3]

# two objects
b = a
print(a)
print(b)

# two objects pointing to the same memory address
print(id(a))
print(id(b))

c = [a, b]
a.append(5)

print(c)

# clone list
a = [1, 2, 3]
print(id(a))
b = a
print(id(a))

c = list(a)
print(id(c))

d = a[::]
print(d)
print(id(d)


# list comprehesions
my_list = list(range(100))

double = [i * 2 for i in my_list]

pares = [i for i in my_list if i % 2 == 0]