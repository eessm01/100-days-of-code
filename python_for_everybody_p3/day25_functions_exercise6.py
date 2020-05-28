"""Chapter 4. Functions. Exercise 6

Rewrite your pay computation with time-and-a-half 
for over- time and create a function called computepay which 
takes two parameters (hours and rate).
"""

def get_float(string):
    try:
        return float(string)
    except:
        print('please enter numeric input')
        return None


def computepay(hours, rate):
    return hours * rate


hours = get_float(input('Enter Hours: '))
if hours: 
    rate = get_float(input('Enter Rate: '))
    if rate: 
        result = computepay(hours, rate)
        print(f'Pay: {result}')