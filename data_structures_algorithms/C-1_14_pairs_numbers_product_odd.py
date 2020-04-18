# Write a short Python function that takes a sequence of integer values and 
# determines if there is a distinct pair of numbers 
# in the sequence whose product is odd.

def get_pairs_product_odd(numbers):
    l = [(n,m) for n in numbers for m in numbers if (n != m) and ( (n * m) % 2 > 0 )]
    return l

if __name__ == "__main__":
    numbers = [ n for n in range(0,10)]
    l = get_pairs_product_odd(numbers)
    print(l)