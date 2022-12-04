
# Part 1
with open('../../input/day4') as file:
    fullyOverlappingRanges = 0

    for line in file:
        line = line.rstrip('\n')
        assignment = line.split(',')
        minmax1 = assignment[0].split('-')
        minmax2 = assignment[1].split('-')
        min1 = int(minmax1[0])
        min2 = int(minmax2[0])
        max1 = int(minmax1[1])
        max2 = int(minmax2[1])

        if min1 >= min2 and max1 <= max2:
            fullyOverlappingRanges += 1
            continue
        if min2 >= min1 and max2 <= max1:
            fullyOverlappingRanges += 1

    print('The sum of pairs with completely overlapping ranges is %d' % fullyOverlappingRanges)

# Part 2
with open('../../input/day4') as file:
    partOverlappingRanges = 0

    for line in file:
        line = line.rstrip('\n')
        assignment = line.split(',')
        minmax1 = assignment[0].split('-')
        minmax2 = assignment[1].split('-')
        min1 = int(minmax1[0])
        min2 = int(minmax2[0])
        max1 = int(minmax1[1])
        max2 = int(minmax2[1])

        if min2 <= max1 <= max2 or min2 <= min1 <= max2:
            partOverlappingRanges += 1
            continue
        if min1 <= min2 <= max1 or min1 <= max2 <= max1:
            partOverlappingRanges += 1

    print('The sum of pairs with partly overlapping ranges is %d' % partOverlappingRanges)
