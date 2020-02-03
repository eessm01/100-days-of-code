def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input('n: '))
    m = int(input('m: '))
    result = is_multiple(n, m)
    print(result)