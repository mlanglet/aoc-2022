import string

priorityValues = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# Part 1
with open('../../input/day3') as backpacks:
    prioritySum = 0
    for backpack in backpacks:
        items = backpack.rstrip('\n')
        middle = int(len(items) / 2)
        compartment1 = items[0:middle]
        compartment2 = items[middle:len(items)]
        commonLetter = set(compartment1).intersection(compartment2).pop()
        prioritySum += priorityValues.index(commonLetter) + 1

    print('The sum of priorities for backpack sorting is %d' % prioritySum)

# Part 2
def calculate_intersecting_priority_value(items):
    commonLetter = set(items.pop()).intersection(items.pop())
    commonLetter = set(items.pop()).intersection(commonLetter).pop()
    return priorityValues.index(commonLetter) + 1


with open('../../input/day3') as backpacks:
    prioritySum, items = 0, []
    for backpack in backpacks:
        if len(items) == 3:
            prioritySum += calculate_intersecting_priority_value(items)
        items.append(backpack.rstrip('\n'))

    prioritySum += calculate_intersecting_priority_value(items)

    print('The sum of priorities for badge authentication is %d' % prioritySum)
