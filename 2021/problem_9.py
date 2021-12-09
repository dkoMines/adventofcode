import advent_file_reader

currentBasin = set()
def part1(file):
    lowPoints = []
    file = [[int(c) for c in line.strip()] for line in file]
    for j, line in enumerate(file):
        for i, c in enumerate(line):
            if isLowPoint(file,i,j):
                lowPoints.append(int(c))
    # print(lowPoints)
    risk = sum(a+1 for a in lowPoints)
    return risk

def isLowPoint(file, i, j):
    # print(j,i)
    c = file[j][i]
    if c == 9:
        return False
    lowPoint = True
    # Up
    if j > 0 and c >= file[j-1][i]:
        lowPoint = False
    # Down
    if j < len(file)-1 and c >= file[j+1][i]:
        lowPoint = False
    # Left
    if i > 0 and c >= file[j][i-1]:
        lowPoint = False
    # Right
    if i < len(file[0])-1 and c >= file[j][i+1]:
        lowPoint = False
    return lowPoint


# Part 2 was a real struggle. I misread the instructions and thought to be part of the basin, it had to be the lowest point, other than parts of the basin. 
# It actually just needed to be higher than another point in the basin.
# Looked at # https://www.reddit.com/r/adventofcode/comments/rca6vp/comment/hntlmtd/?utm_source=share&utm_medium=web2x&context=3 to figure out what I did wrong.

def isInBasin(file, i, j, v):
    # print(j,i)
    c = file[j][i]
    if c < 9 and c not in currentBasin and c > v:
        return True
    return False

def checkAround(file, i, j):
    if (i,j) in currentBasin:
        return 0
    currentBasin.add((i,j))
    count = 1
    # Up
    if j > 0:
        if isInBasin(file, i,j-1, file[j][i]):
            count += checkAround(file, i,j-1)
    # Down
    if j < len(file)-1:
        if isInBasin(file,i,j+1, file[j][i]):
            count += checkAround(file, i,j+1)
    # Left
    if i > 0:
        if isInBasin(file,i-1,j, file[j][i]):
            count += checkAround(file, i-1,j)
    # Right
    if i < len(file[0])-1:
        if isInBasin(file,i+1,j, file[j][i]):
            count += checkAround(file, i+1,j)
    return count

def part2(file):
    basinSizes = []
    file = [[int(c) for c in line.strip()] for line in file]
    for j, line in enumerate(file):
        for i, c in enumerate(line):
            if isLowPoint(file,i,j):
                currentBasin.clear()
                basinSizes.append(checkAround(file, i, j))
                currentBasin.clear()
    top3 = []
    # print(basinSizes)
    while len(top3) < 3:
        top3.append(max(basinSizes))
        basinSizes.remove(max(basinSizes))
    # print(top3)
    return top3[0] * top3[1] * top3[2]

    

file = advent_file_reader.read_file(9)
print("part1: ", part1(file))

print("part2: ", part2(file))
