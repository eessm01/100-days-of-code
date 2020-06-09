import unittest

def judge(arg):
    flag = 1 if arg > 15 else 0
    return flag

def while_example(a,b):
    output = 'NOK'
    while True:
        ret1 = judge(a)
        ret2 = judge(b)

        if ret1 == 0 ret2 == 0:
            print('both a and b are OK')
            output = 'OK'
            break
        else:
            print('both a and b are not OK')
            a = -1
            b = -1

    return output


