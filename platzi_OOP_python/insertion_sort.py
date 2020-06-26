from random import randint


def insertion_sort(one_list):

    # iterate over one_list from 1 to list's length
    for i in range(1, len(one_list)):
        current_element = one_list[i]

        # iterate over all elements in the left side (from i-1 to 0)
        for j in range(i-1,-1,-1):  
            # compare current element whith each left element
            if current_element < one_list[j]:
                # if current_element is smaller, then swap
                one_list[j+1] = one_list[j]
                one_list[j] = current_element

    return one_list


if __name__ == "__main__":
    size = int(input('De que tamaño será la lista: '))

    my_list = [randint(0, 100) for i in range(size)]
    print(my_list)

    ordered_list = insertion_sort(my_list)
    print(ordered_list)