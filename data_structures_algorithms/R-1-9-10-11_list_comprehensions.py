# R-1.9 What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
# R-1.10 What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

if __name__ == "__main__":
    l1 = [ x for x in range(50,81,10) ]
    print(l1)

    l2 = [ x for x in range(8,-9,-2)]
    print(l2)

    l3 = [ pow(2,i) for i in range(0,9) ]
    print(l3)

    l4 = [e*e for i,e in enumerate(range(2,10,2)) if 4 > i > 0 ]
    print(l4)
    # n = 10
    # for p in range(2,n):
    #     print(f'p {p}')
    #     for d in range(2,p):
    #         print( p % d )

    n = 100
    primes = [ p for p in range (2,n) if 0 not in [ p % d for d in range(2,p)] ]
    # prime_pairs = [ (p*q) <= n for (p,q) in primes ]
    prime_pairs = [(p,q) for p in primes for q in primes if (p*q) <= n]
    print(primes)
    print(prime_pairs)
    