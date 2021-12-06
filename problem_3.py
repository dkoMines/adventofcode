import advent_file_reader
def part1(file):
    gr = ""
    er = ""
    for i in range(len(file[0])-1):
        c1 = 0
        for line in file:
            bit = int(line[i])
            if bit == 1:
                c1 += 1;
        if c1 > len(file)/2:
            gr = gr+"1"
            er = er+"0"
        else:
            gr = gr + "0"
            er = er+"1"
    gr = int(gr,2)
    er = int(er,2)
    return gr * er


def part2(file):
    # O2
    l = file
    for i in range(len(file[0])-1):
        # Start at first bit, l->r
        ones = []
        zeros = []
        c1 = 0
        c0 = 0
        for line in l:
            c = int(line[i])
            if c == 1:
                ones.append(line)
                c1 += 1
            else:
                zeros.append(line)
                c0 += 1
        if c1 >= c0:
            l = ones
        else:
            l = zeros
        if len(l) == 1:
            print(int(l[0]), "... ", int(l[0][:-1],2))
            ogr = int(l[0],2)
            print(ogr)
    # C02
    l = file
    for i in range(len(file[1])-1):
        # Start at first bit, l->r
        ones = []
        zeros = []
        c1 = 0
        c0 = 0
        for line in l:
            c = int(line[i])
            if c == 1:
                ones.append(line)
                c1 += 1
            elif c == 0:
                zeros.append(line)
                c0 += 1
        if c1 < c0:
            l = ones
        else:
            l = zeros
        if len(l) == 1:
            co2 = int(l[0],2)
            print(co2)
    return ogr*co2


file = advent_file_reader.read_file(3)
print("part1: ", part1(file))
print("part2: ", part2(file))