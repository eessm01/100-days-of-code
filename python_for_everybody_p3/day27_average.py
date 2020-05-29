"""Write a program which repeatedly reads numbers until the user 
enters “done”. Once “done” is entered, print out the total, 
count, and average of the numbers. If the user enters anything 
other than a number, detect their mistake using try and except 
and print an error message and skip to the next number.
"""

def get_num(data):
    try:
        return int(data)
    except:
        return None


count, total = 0, 0
while True:
    data = input('Enter a number: ')

    if data == 'done':
        break
    
    num = get_num(data)

    if num:
        count += 1
        total += num
    else: 
        print('Invalid input')

average = total / count

print(f'{total} {count} {average}')
