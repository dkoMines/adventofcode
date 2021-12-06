import advent_file_reader

def depth_dist(file):
    h = 0
    d = 0
    for line in file:
        direction, magnitude = line.split(" ")
        magnitude = int(magnitude)
        if direction == 'forward':
            h += magnitude
        elif direction == 'down':
            d += magnitude
        elif direction == 'up':
            d -= magnitude
        else:
            print(line)
    return h*d

def depth_aim(file):
    h = 0
    d = 0
    aim = 0
    for line in file:
        direction, magnitude = line.split(" ")
        magnitude = int(magnitude)
        if direction == 'forward':
            h += magnitude
            d += aim * magnitude
        elif direction == 'down':
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude
        else:
            print(line)
    return h*d

file = advent_file_reader.read_file(2)
print("part 1:", depth_dist(file))
# part 1: 1561344
print("part 2:", depth_aim(file))
# part 2: 1848454425