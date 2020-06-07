"""Compare a string with the string 'banana'

The comparison operators work on strings. To see if two strings are equal:
Other comparison operations are useful for putting words in alphabetical order:
"""

def get_word():
    word = input('Word: ')
    if not word or len(word) < 0:
        return get_word()
    else: 
        return word


if __name__ == '__main__':
    word = get_word()
    banana = 'banana'

    if word < banana:
        print('Your word, {}, comes before {}'.format(word, banana))
    elif word > banana:
        print('Your word, {}, comes after {}'.format(word, banana))
    else:
        print('All right, {}s.'.format(banana))

