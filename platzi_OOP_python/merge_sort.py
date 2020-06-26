from random import randint


def merge_sort(one_list):
    # print('Llamada a merge_sort')
    n = len(one_list)

    if n > 1:
        
        m = n // 2
        left = one_list[0:m]
        right = one_list[m:]

        # print(left)
        # print(right)

        left = merge_sort(left)
        right = merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                one_list[k] = left[i]
                i += 1
            else:
                one_list[k] = right[j]
                j += 1
            k += 1
    
        while i < len(left):
            one_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            one_list[k] = right[j]
            j += 1
            k += 1 
        
    # print(f'return {one_list}')
    return one_list
    

if __name__ == "__main__":
    size = int(input('De que tamaño será la lista: '))

    my_list = [randint(0, 100) for i in range(size)]
    # my_list = [5, 3, 11, 2, 1]
    print(my_list)

    ordered_list = merge_sort(my_list)
    print(ordered_list)