# Exercise 3.1. Move the last line of this program to the top, so the function call 
# appears before the definitions. Run the program and see what error message you get.
# repeat_lyrics()
# Traceback (most recent call last):
#   File "3_exercises.py", line 1, in <module>
#     repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined



def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# repeat_lyrics()
# Traceback (most recent call last):
#   File "3_exercises.py", line 16, in <module>
#     repeat_lyrics()
#   File "3_exercises.py", line 13, in repeat_lyrics
#     print_lyrics()
# NameError: name 'print_lyrics' is not defined

def print_lyrics():
    print("I´s a lumberjack, and I´m okay.")
    print("I sleep all night and I work all day.")


repeat_lyrics()
