if __name__ == "__main__":
    a = [100,200,300]
    b = [1,2,3]
    lista = [ x + y for x in a for y in b]
    print(lista)
    # [101, 102, 103, 201, 202, 203, 301, 302, 303]
    lista2 = [ x + y for x,y in zip(a,b)]
    print(lista2)
    # [101, 202, 303]
