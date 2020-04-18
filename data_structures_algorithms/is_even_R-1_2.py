def is_even(k):
    tup = ('0','2','4','6','8')
    strk = str(k)
    last_digit = strk[-1]
    if last_digit in tup:
        return True
    else:
        return False


if __name__ == "__main__":
    k = int(input('Ingrese un número: '))
    exist = is_even(k)
    if exist:
        print(f'{k} es par')
    else:
        print(f'{k} es impar')