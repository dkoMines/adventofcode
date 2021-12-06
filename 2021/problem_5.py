import advent_file_reader

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vents = 0


def part1(file, part):
    cells = []
    # Generate a 2d array of 1k x 1k
    for i in range(1000):
        row = []
        for j in range(1000):
            c = Cell(i,j)
            row.append(c)
        cells.append(row)

    # Calc fissure lines from file and place onto 2d array.
    for line in file:
        x1,y1 = line.split(" -> ")[0].split(",")
        x2,y2 = line.split(" -> ")[1].split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        # V lines
        if x1 == x2:
            if y1 > y2:
                temp = y2
                y2 = y1
                y1 = temp
            for y in range(y1, y2+1):
                cells[x1][y].vents += 1
        # H lines
        elif y1 == y2:
            if x1 > x2:
                temp = x2
                x2 = x1
                x1 = temp
            for x in range(x1, x2+1):
                cells[x][y1].vents += 1
        # D Lines
        elif part == 2:
            if abs(x1-x2) == abs(y1-y2):
                x = x1
                y = y1
                xInc = x1 < x2
                yInc = y1 < y2
                for i in range(abs(x1-x2)+1):
                    cells[x][y].vents += 1
                    if xInc:
                        x += 1
                    else:
                        x -= 1
                    if yInc:
                        y += 1
                    else:
                        y -= 1
    
    # Count # of hotspots (2 or more)
    count = 0
    for i in range(1000):
        row = []
        for j in range(1000):
            if cells[i][j].vents >= 2:
                count += 1
    return count


file = advent_file_reader.read_file(5)
print("part1: ",part1(file, 1))
# part1:  5306
print("part2: ",part1(file, 2))
# part2:  17787