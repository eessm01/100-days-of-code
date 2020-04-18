""" This programs is a solution for
    Exercise 3.5. This exercise can be done using only the statements and other features we have 
    learned so far.
    1. Write a function that draws a grid like the following:

            +----+----+ 
            |    |    | 
            |    |    | 
            |    |    | 
            |    |    | 
            +----+----+ 
            |    |    | 
            |    |    | 
            |    |    | 
            |    |    | 
            +----+----+
    Hint: to print more than one value on a line, you can print a comma-separated sequence:
        print '+', '-'
    If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.
        print '+',
        print '-'
    The output of these statements is '+ -'.
    A print statement all by itself ends the current line and goes to the next line.
    Write a function that draws a similar grid with four rows and four columns.
"""


def print_row(num_row):
    for i in range(0,num_row):
        print('+', '- '*4, end='')
    print('+', end='')
    print('') 
    for i in range(0,4):
        for i in range(0,num_row):
            print('|',' '*8, end='')
        print('|',' '*8, end='')
        print('')
    

def print_grid(size):
    # numbers of columns
    for i in range(0,size):
        print_row(size)

    # draw the last line
    for i in range(0,size):
        print('+', '- '*4, end='')
    print('+', end='')
    print('') 


if __name__ == "__main__":
    print_grid(3)
    