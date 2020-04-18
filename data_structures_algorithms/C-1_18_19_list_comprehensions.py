# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

# Demonstrate how to use Python’s list comprehension syntax to produce the
# list[ a , b , c ,..., z ],but without having to typea ll 26 such characters literally.

# Write a short Python program that takes two arrays a and b of length n storing int values,
# and returns the dot product of a and b. That is, it returns an array c of length n such that 
# c[i] = a[i]·b[i], for i = 0,...,n−1.


if __name__ == "__main__":
    l1 = [ e*(e+1) for e in range(0,10)]
    print(l1)

    l2 = [ chr(i) for i in range(97,123)]
    print(l2)

    la = [1,2,3,4]
    lb = [2,2,2,2]
    lc = [ a*b for a,b in zip(la,lb)]
    print(lc)