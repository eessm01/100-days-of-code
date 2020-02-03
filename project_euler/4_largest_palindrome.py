def is_palindrome(number):
    string = str(number)
    reverse = string[::-1]
    if string == reverse:
        return True
    return False


def largest_palindrome(start, end):
    the_largest_palindrome = 0
    for i in range(start,end):
        for j in range(start,end):
            number = i * j
            if is_palindrome(number) and number > the_largest_palindrome:
                the_largest_palindrome = number
    return the_largest_palindrome


if __name__ == '__main__':
    result = largest_palindrome(100,1000)
    print(result)
