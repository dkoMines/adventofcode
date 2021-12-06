import advent_file_reader

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vents = 0


def part1(file):
    cells = []
    # Generate Cells
    for i in range(1000):
        row = []
        for j in range(1000):
            c = Cell(i,j)
            row.append(c)
        cells.append(row)

    # Make h v lines
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
        else:
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
    
    # Count 2s
    count = 0
    for i in range(1000):
        row = []
        for j in range(1000):
            if cells[i][j].vents >= 2:
                count += 1

    return count


file = advent_file_reader.read_file(5)
print("part1: ",part1(file))