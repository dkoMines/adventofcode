import advent_file_reader

def part1(file):
    numbers = file[0].split(',')
    fuel_cost = 999999999
    best_meet = 9999999
    min_value = int(min(numbers))
    max_value = int(max(numbers))

    for i in range(min_value, max_value):
        c_cost = 0
        for n in numbers:
            n = int(n)
            c_cost += abs(n-i)
        if c_cost < fuel_cost:
            fuel_cost = c_cost
            best_meet = i
    return fuel_cost

def part2(file):
    numbers = file[0].split(',')
    fuel_cost = 999999999
    best_meet = 9999999
    min_value = int(min(numbers))
    max_value = int(max(numbers))

    for i in range(min_value, max_value):
        c_cost = 0
        for n in numbers:
            n = int(n)
            cost = abs(n-i)
            # https://math.stackexchange.com/questions/593318/factorial-but-with-addition/593323
            cost = ((cost**2)+cost)/2
            c_cost += cost
        if c_cost < fuel_cost:
            fuel_cost = c_cost
            best_meet = i
    return int(fuel_cost)

file = advent_file_reader.read_file(7)
print("part1: ", part1(file))
# part1:  344297
print("part2: ", part2(file))
# part2:  97164301