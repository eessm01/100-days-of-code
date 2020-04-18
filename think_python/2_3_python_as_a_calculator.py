""" This program is a solution for:
    1. The volume of a sphere with radius r is 4 πr3. 
        What is the volume of a sphere with radius 5?
        Hint: 392.7 is wrong!
    2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
        Shipping costs $3 for the first copy and 75 cents for each additional copy. 
        What is the total wholesale cost for 60 copies?
    3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
        then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do 
        I get home for breakfast?
"""
import math

def volume_sphere():
    r = 5
    r = (4/3)*math.pi*(r**3)
    return r


def total_wholesale():
    books = 60
    cost_book = 24.95
    cost_bookstores = cost_book - (cost_book*.4)
    wholesale = (cost_bookstores * 60) + 3 + ( (books - 1) * .75)
    return wholesale


def time_to_breakfast():
    # time in minuts
    whole_time = ( (( (8*60) + 15 ) * 2) + ( ( (7*60) + 12 ) * 3) ) / 60
    return whole_time

if __name__ == '__main__':
    print(volume_sphere())
    print(total_wholesale())
    print(time_to_breakfast())