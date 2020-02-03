def get_smallest_multiple(max_divisor):
    is_find = False
    initial_smallest_number = 2520

    while not is_find:
        for i in range(max_divisor, 1, -1):
            if initial_smallest_number % i > 0:
                break
            else:
                if i == 2:
                    is_find = True
                    return initial_smallest_number

        initial_smallest_number += 1


if __name__ == '__main__':
    max_divisor = int(input('Ingrese el número máximo:'))
    initial_smallest_number = get_smallest_multiple(max_divisor)
    print(initial_smallest_number)

