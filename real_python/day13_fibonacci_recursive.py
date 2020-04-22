#!/usr/bin/env python3
from functools import lru_cache

"""
Naively following the recursive deﬁnition of the nth Fibonacci number was 
rather inefficient. As you can see from the output above, we are unnecessarily
recomputing values. Let’s try to improve fibonacci_recursive by caching the
results of each Fibonacci computation Fk:

lru_cache -
Is a decorator that caches the results. Thus, we avoid recomputation
by explicitly checking for the value before trying to compute it. One thing to
keep in mind about lru_cache is that since it uses a dictionary to cache
results, the positional and keyword arguments (which serve as keys in that
dictionary) to the function must be hashable.
"""

@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


fibonacci_recursive(5)