from random import randint


def bubble_sort(one_list):
    n = len(one_list)
    limit = n - 1

    for i in range(n):
        for j in range(limit):
            if one_list[j] > one_list[j+1]:
                one_list[j], one_list[j+1] = one_list[j+1], one_list[j]
        limit -= 1

    return one_list
    

if __name__ == "__main__":
    size = int(input('De que tamaño será la lista: '))

    my_list = [randint(0, 100) for i in range(size)]
    # my_list = [5, 3, 11, 2, 1]
    print(my_list)

    ordered_list = bubble_sort(my_list)
    print(ordered_list)