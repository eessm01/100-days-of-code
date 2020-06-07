"""Count a single letter in a string

Encapsulate this code in a function named count, and gen- eralize
it so that it accepts the string and the letter as arguments.

There is a string method called count that is similar to the function
in the previous exercise. Read the documentation of this method at:
https://docs.python.org/library/stdtypes.html#string-methods
Write an invocation that counts the number of times the letter 
a occurs in “ba- nana”.
"""

def get_word():
    word = input('Word: ')
    if not word or len(word) < 0:
        return get_word()
    else: 
        return word


def get_letter():
    letter = input('Letter: ')
    if not letter:
        return get_letter()
    elif len(letter) != 1: 
        print('Only one character, please')
        return get_letter()
    else:
        return letter


def count(a_letter, word):
    count = 0
    for letter in word:
        if letter == a_letter:
            count += 1

    return count


if __name__ == '__main__':
    word = get_word()
    letter = get_letter()
    count = count(letter, word)
    print(count)

    count2 = word.count(letter)
    print(count2)

