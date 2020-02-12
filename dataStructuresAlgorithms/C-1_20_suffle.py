"""This program is a solution for:
    Python’s random module includes a function shuffle(data) that accepts a list of elements and 
    randomly reorders the elements so that each possible order occurs with equal probability. 
    The random module includes a more basic function randint(a, b) that returns a uniformly random 
    integer from a to b (including both endpoints). Using only the randint function, implement your 
    own version of the shuffle function.
"""
import random


def suffle(data):
    """This function accepts a list of elements and randomly reorders the 
    elements so that elements so that each possible order occurs with equal probability
    """
    index_list = []
    new_data = []
    n = len(data)
    
    while len(index_list) < n:
        newi = random.randint(0,n-1)
        if newi not in index_list:
            index_list.append(newi)
            new_data.append(data[newi])

    return new_data


if __name__ == "__main__":
    data = input('Ingrese la lista, con los elementos separados por comas: ')
    data = [ element for element in data.split(',') ]
    new_data = suffle(data)
    print(new_data)
