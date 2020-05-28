"""Chapter 4. Functions. Exercise 7

Rewrite the grade program from the previous chapter using a function
called computegrade that takes a score as its parameter and returns
a grade as a string.
"""

def get_grade(score):
    try:
        score = float(score)
        
        if score >= 1 or score < 0:
            return None
        elif score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        elif score < 0.6:
            return 'F'

    except:
        return None 


score = input('Enter score: ')
grade = get_grade(score)
if grade:
    print(grade)
else: 
    print('Bad score')