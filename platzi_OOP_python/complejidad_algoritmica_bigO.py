import math

def o_1(n):
    return 1


def o_logn(n):
    return math.log10(n)


def o_n(n):
    return n


def o_nlogn(n):
    return n * math.log10(n)


def o_n_exp2(n):
    return n**2


def o_2_expn(n):
    return 2**n


if __name__ == "__main__":
    print(o_2_expn(1000))