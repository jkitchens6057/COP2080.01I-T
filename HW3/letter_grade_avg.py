from grade_compute import *

# main program
def main():
    grades = getInput()

    # exits the program if Q or invalid symbol
    if grades == 0:
        print("Exiting Program\nProgram Exited With Exit Code 0")
        return 0
    elif grades == 1:
        print("Error: Invalid Input\nProgram Exited With Exit Code 1")
        return 1

    numGrades = letterToNumber(grades)

    # creates a sorted letter grade list based on the number grades list
    gradesSorted = []

    for grade in numGrades:
        gradesSorted.append(numberToLetter(grade))

    # removes the lowest grade
    low = numGrades.pop()

    # calculates the average grade
    avgGrade = sum(numGrades)/len(numGrades)

    # adds .25 if every letter is B- or lower
    # n is used as a counter variable to keep track of the amount of scores B- or lower
    n = 0
    for num in numGrades:
        if num <= 2.7:
            n += 1

    if n == len(numGrades):
        avgGrade += .25

    low = numberToLetter(low)

    final = numberToLetter(avgGrade)

    # GUI code
    # mostly constists of print statements and code to ensure proper GUI sizing with variable grade sizes (ie, a, c+)
    # g and l are used as temporary storage variables for strings of text and lengths, respectively
    print('----------------------------------------')
    print('|         Grade Report Summary         |')
    print('----------------------------------------')
    g : str = str("| Grades Entered: ")
    n = 0
    for grade in gradesSorted:
        g += grade
        n +=1
        if n != len(gradesSorted):
            g += ", "
    l = 40 - len(g)
    # quits the program if there are too many scores and the GUI would overflow (there is no overflow with the way it is implemented, 
    # this would just cause errors)
    if l < 1:
        print("Error: Too Many Scores\nProgram Exited With Exit Code 2")
        return 2
    print(g, end="")
    for n in range(l - 1):
        print(" ", end='')
    print("|")
    g : str = str("| Lowest Grade Dropped: ")
    g += low
    print(g,end="")
    l= 40 - len(g)
    for n in range (l - 1):
        print(" ", end="")
    print('|')
    print("| Calculated Average: " + str(round(avgGrade, 2)) + "             |")
    g : str = str("| Final Letter Grade: ")
    g += final
    print(g,end="")
    l= 40 - len(g)
    for n in range (l - 1):
        print(" ", end="")
    print('|')
    print('----------------------------------------')
    return True

# runs the program until told to close with Q or invalid input (error code)
run = True
while run == True:
    run = main()