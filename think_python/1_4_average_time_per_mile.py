""" This program is a solution for:
    If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? 
    What is your average speed in miles per hour? 
    (Hint: there are 1.61 kilometers in a mile).
"""

if __name__ == "__main__":
    miles = 10/1.61
    # time  in seconds
    time_per_mile = ( (43 * 60) + 30) / miles

    print(f'{time_per_mile / 60} min.')