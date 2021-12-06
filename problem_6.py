import advent_file_reader

newage = 8

def part1(file, days):
    ages = file[0].split(",")
    counts = []
    for i in range(9):
        counts.append(0)
    for age in ages:
        age = int(age)
        counts[age] += 1
    for day in range(days):
        zeros = counts[0]
        for i in range(len(counts)-1):
            counts[i] = counts[i+1]
        counts[8] = zeros
        counts[6] += zeros
    sum = 0
    for c in counts:
        sum += c
    return sum

def part2(file):
    return

file = advent_file_reader.read_file(6)
print("part1: ", part1(file, 80))
print("part2: ", part1(file, 256))