import string

priorityValues = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# Part 1
with open('input') as backpacks:
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


with open('input') as backpacks:
    prioritySum, elfCounter, items = 0, 0, []
    for backpack in backpacks:
        if elfCounter == 3:
            prioritySum += calculate_intersecting_priority_value(items)
            elfCounter = 0
        items.append(backpack.rstrip('\n'))
        elfCounter += 1
    prioritySum += calculate_intersecting_priority_value(items)

    print('The sum of priorities for badge authentication is %d' % prioritySum)
