import advent_file_reader

def increased_count(file):
    prev = False
    count = 0
    for line in file:
        if prev:
            if int(line) > prev:
                # Increased
                count += 1
        prev = int(line)
    return count

def windowed_count(file):
    prev = False
    count = 0
    for i in range(len(file)-2):
        curr = int(file[i])+int(file[i+1])+int(file[i+2])
        if prev:
            if curr > prev:
                count += 1
        prev = curr
    return count

file = advent_file_reader.read_file(1)
print("part 1:", increased_count(file))
# part 1: 1681
print("part 2:", windowed_count(file))
# part 2: 1704