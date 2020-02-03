def minmax(data):
    data = data.split(',')
    data = [ int(element) for element in data ]
    data.sort()
    tup = (data[0], data[-1])
    return tup


if __name__ == "__main__":
    data = input('Ingrese los números separados por comas: ')
    tup = minmax(data)
    print(tup)