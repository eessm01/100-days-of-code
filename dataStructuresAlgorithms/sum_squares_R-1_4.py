def sum_squares_smaller_n(n):
    sum_squares = 0
    for i in range(1,n):
        sum_squares = sum_squares + i**2
    return sum_squares


if __name__ == '__main__':
    n = int(input('Cual es el número: '))
    sum_squares = sum_squares_smaller_n(n)
    print(sum_squares)