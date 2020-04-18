"""This program is only a solution for:
   Write a short Python program that takes two arrays a and b of length n 
   storing int values, and returns the dot product of a and b. That is, it returns
   an array c of length n such that c[i[ = a[i]*b[i], for i = 0,...,n-1.
"""

def dot_product(a,b):
    """This function return the dot product of a and b arrays."""
    return [ i*j for i,j in zip(a,b) ]

if __name__ == "__main__":
    a = [3,5,7,8]
    b = [3,2,0,8]
    c = dot_product(a,b)
    print(c)