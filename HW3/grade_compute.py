# function receives and validates user input
def getInput():
    user = input("Enter test grades ended with $ signs: ").upper() 

    # gives exit code if Q is present
    if 'Q' in user:
        return 0

    grades = validateInput(user)
    
    # gives error code if validation failed
    if grades == 1:
        return 1

    return grades

# function ensures user input is usable
def validateInput(user : str):

    grades = [];
    accept = ['A', 'B', 'C', 'D', 'F', '+', '-', ' ', '$']

    grade : str = ""

    # ensures that the input is usable and parses the grades based on the end sign $
    # $ is required after a grade for it to be counted
    # there are no checks on the number of items in grades, so this can be used with more than 4 test scores, 
    # but too many will break the GUI and be caught as an error by the GUI code
    for char in user:
        if char not in accept:
            return 1
        if char != ' ' and char != '$':
            grade += char
        elif char == '$':
            grades.append(grade)
            grade : str = ""
        if len(grade) > 2:
            return 1
    
    return grades

# function translates the letter grade into a number grade
def letterToNumber(grades : list):

    numGrades = []

    for grade in grades:
        match (grade):
            case 'A+': numGrades.append(4.0)
            case 'A': numGrades.append(4.0)
            case 'A-': numGrades.append(3.7)
            case 'B+': numGrades.append(3.3)
            case 'B': numGrades.append(3.0)
            case 'B-': numGrades.append(2.7)
            case 'C+': numGrades.append(2.3)
            case 'C': numGrades.append(2.0)
            case 'C-': numGrades.append(1.7)
            case 'D+': numGrades.append(1.3)
            case 'D': numGrades.append(1.0)
            case _: numGrades.append(0.0)
    
    numGrades.sort(reverse=True)

    return numGrades

# function translate the number grade back to a letter grade
# since A and A+ have the same weight, they are both retranslated to A
def numberToLetter(number):

    letGrade = ''

    if (number == 4.0): 
        letGrade = 'A'
    elif (number >= 3.7): 
        letGrade = 'A-'
    elif (number >= 3.3): 
        letGrade = 'B+'
    elif (number >= 3.0): 
        letGrade = 'B'
    elif (number >= 2.7): 
        letGrade = 'B-'
    elif (number >= 2.3): 
        letGrade = 'C+'
    elif (number >= 2.0): 
        letGrade = 'C'
    elif (number >= 1,7): 
        letGrade = 'C-'
    elif (number >= 3.7): 
        letGrade = 'D+'
    elif (number >= 3.7): 
        letGrade = 'D'
    else:
        letGrade = 'F'

    return letGrade