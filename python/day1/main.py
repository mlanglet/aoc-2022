
# Part 1
with open('../../input/day1') as file:
    currentCalories, maxCalories = 0, 0
    for line in file:
        if line == '\n':
            if currentCalories > maxCalories:
                maxCalories = currentCalories
            currentCalories = 0
        else:
            currentCalories += int(line.rstrip('\n'))
    print('The most calories carried is %d' % maxCalories)

# Part 2
with open('../../input/day1') as file:
    currentCalories, top1, top2, top3 = 0, 0, 0, 0
    for line in file:
        if line == '\n':
            if currentCalories > top1:
                top3 = top2
                top2 = top1
                top1 = currentCalories
            elif currentCalories > top2:
                top3 = top2
                top2 = currentCalories
            elif currentCalories > top3:
                top3 = currentCalories

            currentCalories = 0
        else:
            currentCalories += int(line.rstrip('\n'))

    print('The sum of calories carried by the three elves carrying the most is %d' % (top1 + top2 + top3))
