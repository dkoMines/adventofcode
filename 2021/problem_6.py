import advent_file_reader

newage = 8
timerreset = 6

def part1(file, days):
    ages = file[0].split(",")
    counts = []
    # counts is array counting # of lightfish at each age
    for i in range(9):
        counts.append(0)
    # Transfer file to counts array
    for age in ages:
        age = int(age)
        counts[age] += 1
    # Day loop
    for day in range(days):
        zeros = counts[0]
        for i in range(len(counts)-1):
            counts[i] = counts[i+1]
        counts[newage] = zeros
        counts[timerreset] += zeros
    # Add up # of lightfish
    sum = 0
    for c in counts:
        sum += c
    return sum

def part2(file):
    return

file = advent_file_reader.read_file(6)
print("part1: ", part1(file, 80))
# part1:  396210
print("part2: ", part1(file, 256))
# part2:  1770823541496