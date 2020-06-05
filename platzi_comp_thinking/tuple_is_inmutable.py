"""Uses of tuples
"""

# Tuplesareimmutable
my_tuple = (1, 'dos', True)
print(my_tuple[0])
# my_tuple[0] = 2  

tuple1 = (1)  # It isn't a tuple. 
print(f'tuple1 = (1)  {type(tuple1)}')

tuple1 = 1,  # The tuple constructor is the comma (,)
print(f'tuple1 = 1,  {type(tuple1)}')

# parentheses to help us quickly identify tuples when we look at Python code
tuple1 = (1,)  
print(f'tuple1 = (1,)  {type(tuple1)}')

other_tuple = (2, 3, 4)

# You can’t modify the elements of a tuple, 
# but you can replace one tuple with another:
tuple1 += other_tuple 
print(tuple1)

# unpack
print('unpack')
x, y, z = other_tuple
print(f'x {x}')
print(f'y {y}')
print(f'z {z}')

m = other_tuple
print(f'm[0] {m[0]}')
print(f'm[1] {m[1]}')
print(f'm[2] {m[2]}')


# Return a tuple in a function
print('Return a tuple in a function')
def coordenadas():
    return (5, 4)

data = coordenadas()
print(f'data  {data}')

x , y = coordenadas()
print(f'x {x}')
print(f'y {y}')
