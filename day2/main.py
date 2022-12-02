
# Part 1
with open('input') as rounds:
    totalScore = 0
    # A Rock - X rock - 1 point
    # B Paper - Y paper - 2 points
    # C Scissors - Z Scissors - 3 points
    # win 6, draw 3, loss 0
    for round in rounds:
        round = round.rstrip('\n')
        moves = round.split(" ")
        if moves[1] == 'X':
            if moves[0] == 'A':
                totalScore += 4
            elif moves[0] == 'B':
                totalScore += 1
            elif moves[0] == 'C':
                totalScore += 7
        if moves[1] == 'Y':
            if moves[0] == 'A':
                totalScore += 8
            elif moves[0] == 'B':
                totalScore += 5
            elif moves[0] == 'C':
                totalScore += 2
        if moves[1] == 'Z':
            if moves[0] == 'A':
                totalScore += 3
            elif moves[0] == 'B':
                totalScore += 9
            elif moves[0] == 'C':
                totalScore += 6

    print('The total score of the first strategy is %d' % totalScore)

# Part 2
with open('input') as rounds:
    totalScore = 0
    # A Rock - X lose - 1 point
    # B Paper - Y draw - 2 points
    # C Scissors - Z win - 3 points
    # win 6, draw 3, loss 0
    for round in rounds:
        round = round.rstrip('\n')
        moves = round.split(" ")
        if moves[1] == 'X':
            if moves[0] == 'A':
                totalScore += 3
            elif moves[0] == 'B':
                totalScore += 1
            elif moves[0] == 'C':
                totalScore += 2
        if moves[1] == 'Y':
            if moves[0] == 'A':
                totalScore += 4
            elif moves[0] == 'B':
                totalScore += 5
            elif moves[0] == 'C':
                totalScore += 6
        if moves[1] == 'Z':
            if moves[0] == 'A':
                totalScore += 8
            elif moves[0] == 'B':
                totalScore += 9
            elif moves[0] == 'C':
                totalScore += 7

    print('The total score of the second strategy is %d' % totalScore)
