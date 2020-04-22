#!/usr/bin/env python3
# Return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, input_list):
    return [element] + input_list


my_list = attach_head(1,
            attach_head(46,
                        attach_head(-31,
                                    attach_head("hello", [] ))))

print(my_list)



def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Descompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be defined in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


result = list_sum_recursive([1, 2, 3, 4])
print(result)