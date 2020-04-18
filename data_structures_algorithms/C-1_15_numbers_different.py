# Write a Python function that takes a sequence of numbers and determines if all the numbers are different 
# from each other (that is, they are distinct).

def are_differents(numbers):
    differents = list()
    for i in range(0,len(numbers)):
        is_repeat = False
        for j in range(0,len(numbers)):
            if i != j:
                if numbers[i] == numbers[j]:
                    is_repeat = True
                    break
        if not is_repeat:
            differents.append(numbers[i])
    
    return differents
        

if __name__ == "__main__":
    data = input('Ingrese los números: ')
    data = data.split(',')
    numbers = [ int(e) for e in data ]
    differents = are_differents(numbers)
    print('números no repetidos: ')
    print(differents)