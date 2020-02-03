def sum_square_difference(num):
    sum_squares = 0
    square_sum = 0
    for i in range(num+1):
        sum_squares = sum_squares + i**2
        square_sum = square_sum + i
    
    difference = (square_sum**2) - sum_squares
    return difference


if __name__ == "__main__":
    print(sum_square_difference(100))