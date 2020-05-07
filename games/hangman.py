from random import randint

WORDS = [
    'pig',
    'sheep',
    'kitty',
    'puppy',
    'dog',
    'duck',
    'sleeping',
    'swimming'
]

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def get_random_word():
    """ Return a random word from words list """
    index = randint(0, len(WORDS) - 1)
    return WORDS[index]


def get_new_word(word, hidden_word, letter):
    """ If letter in word then return a new word with the entered letter """
    list_characters = list(hidden_word)

    for i, caracter in enumerate(word):
        if caracter == letter:
            list_characters[i] = letter

    return ''.join(list_characters)


def run():
    print("Gibran, Welcome to hangman game ")

    word = get_random_word()
    hidden_word = '-' * len(word)
    max_failures = len(HANGMAN) - 1
    tries = 0
    failures = 0

    print("Your word is laki this: {data}".format(data=hidden_word))

    while failures < max_failures:
        letter = input('Choose a letter: ')
        tries += 1
        old_word = hidden_word
        hidden_word = get_new_word(word, hidden_word, letter)
        if old_word == hidden_word:
            failures += 1

        print(HANGMAN[failures])
        print(hidden_word)
    
        if word == hidden_word:
            print("Congratulations! You are the winner!")
            break

    if failures == max_failures:
        print('I\'m sorry, you lost. The word was "{}" '.format(word))


if __name__ == "__main__":
    run()