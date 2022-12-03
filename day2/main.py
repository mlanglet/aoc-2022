
# Part 1
with open('input') as file:
    totalScore = 0
    valueMap = {
        'A X': 4,
        'B X': 1,
        'C X': 7,
        'A Y': 8,
        'B Y': 5,
        'C Y': 2,
        'A Z': 3,
        'B Z': 9,
        'C Z': 6,
    }

    for move in file:
        totalScore += valueMap.get(move.strip('\n'))

    print('The total score of the first strategy is %d' % totalScore)

# Part 2
with open('input') as file:
    totalScore = 0
    valueMap = {
        'A X': 3,
        'B X': 1,
        'C X': 2,
        'A Y': 4,
        'B Y': 5,
        'C Y': 6,
        'A Z': 8,
        'B Z': 9,
        'C Z': 7,
    }

    for move in file:
        totalScore += valueMap.get(move.strip('\n'))

    print('The total score of the second strategy is %d' % totalScore)
