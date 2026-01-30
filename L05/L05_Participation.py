a, b, c, d = 1, 2, 3, 4

a_tuple = (1,2,3,4,5,6,7)
a_list = [22,33,44,55]
def some_dict():
    a_dict = {'abe': 123, 'doe': 345, 'ken': 789}
    return a_dict
print(*a_tuple)
print(*a_list)
print(*some_dict())

new_health = lambda hp, damage: hp - damage

damage = 20
hp = 100

print(f'Your character took {damage} points of damage')
print(f'Your character has dropped from {hp} hit points to {new_health(hp,damage)} hit points available')

def scoreToNumber(score):

    '''
    Returns the score based on the given outcom
    
            Parameters:
                    score (str): a string containing the outcome of the game

            Returns:
                    result (int): the score associated with the given outcome
    '''

    score = str.upper(score)
    result = 0
    first = score[0]
    if first == "G" :
        result = 10
    elif first == "O" :
       result = 5
    elif first == "P" :
        result = 3
    return result
def main():
    score1 = input('Enter score 1 as Great, Ok or Poor: ')
    score2 = input('Enter score 2 as Great, Ok or Poor: ')
    score3 = input('Enter score 3 as Great, Ok or Poor: ')
    x1 = scoreToNumber(score1)
    x2 = scoreToNumber(score2)
    x3 = scoreToNumber(score3)
    xmax = max(x1, x2, x3)
    some_avg = (x1 + x2 + x3) / 3
    print(f'The maximum score was {xmax}')
    print(f'The avg score on 1-10 scale would have been {round(some_avg, 2)}')

main()

grades = [95, 88, 85, 75]
letter_grade = ['A', 'B+', 'B', 'C']
print('The original list ',letter_grade)
print('The zipped tuples ', list(zip(letter_grade, grades)))
print('Next is a map-lambda version')
print(list(map(lambda *a: a, letter_grade, grades))) # equivalent to zip

print([(x, y) for x in ['a', 'b', 'c'] for y in ['first','b', 3] if x not in str(y)])

a_list = [7, 5, -4, 6, -7, -10, 8, -9]

check_negative = [x * -1 for x in a_list if x < 0]
print(check_negative)