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
    file = file.readlines()
    prev = False
    count = 0
    for i in range(len(file)-2):
        curr = int(file[i])+int(file[i+1])+int(file[i+2])
        if prev:
            if curr > prev:
                count += 1
        prev = curr
    return count

file = open('C:/Users/48246/Documents/Fall21/adventofcode/input_problem1.txt', 'r')
print(windowed_count(file))