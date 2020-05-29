"""Write another program that prompts for a list of numbers 
as above and at the end prints out both the maximum and 
minimum of the numbers instead of the average.
"""

def get_num(data):
    try:
        return int(data)
    except:
        return None


def run():
    smallest = None
    largest = None

    while True:
        data = input('Enter a number: ')

        # if user type done, break loop
        if data == 'done':
            break
        
        num = get_num(data)

        # num is a number
        if num:
            if not smallest or num < smallest:
                smallest = num
            if not largest or num > largest:
                largest = num
        else: 
            print('Invalid input')

    print(f'smallest: {smallest}, largest: {largest}')


if __name__ == '__main__':
    run()
