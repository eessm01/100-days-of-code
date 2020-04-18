"""This program is a solution for:
   Write a short Python function that counts the number of vowels in a given
   character string.
"""

def get_numbers_of_vowels(string):
    characters = list(string)
    vowels = ('a','e','i','o','u')
    count_vowels = 0
    for char in characters:
        for vowel in vowels:
            if vowel == char:
                count_vowels += 1
                break
    
    return count_vowels


if __name__ == "__main__":
    string = input('Ingresa la cadena: ')
    count = get_numbers_of_vowels(string)
    print(count)