import advent_file_reader

def compare(num1,num2):
    # print(num1, num2)
    aNotInb = 0
    bNotIna = 0
    for a in num1:
        if not a in num2:
            aNotInb += 1
    for b in num2:
        if not b in num1:
            bNotIna += 1  
    return aNotInb, bNotIna

def compare_codes(code1, code2):
    for a in code1:
        if not a in code2:
            return False
    for a in code2:
        if not a in code1:
            return False
    return True

def allTrue(l):
    for i in l:
        if not i:
            return False
    return True

def part1(file):
    count = 0
    for line in file:
        past = False
        for a in line.split():
            if a == '|':
                past = True
            if past:
                if len(a)==2:
                    # 1
                    count += 1
                if len(a)==3:
                    # 7
                    count += 1
                if len(a)==4:
                    # 4
                    count += 1
                if len(a)==7:
                    count+=1
    return count

def part2(file):
    total = 0
    for line in file:
        past = False
        numbers = [False for a in range(10)]
        code = [False for a in range(10)]
        firsthalf, secondhalf = line.split("|")
        for a in firsthalf.split():
            if len(a)==2:
                # 1, left side
                numbers[1] = True
                code[1] = a
            elif len(a)==3: 
                # 7 left and top
                numbers[7] = True
                code[7] = a
            elif len(a)==4:
                # 4 left, middle, top-right
                numbers[4] = True
                code[4] = a
            elif len(a)==7: # Doesn't help map
                # 8
                numbers[8] = True
                code[8] = a
        for a in firsthalf.split():
            if len(a)==5:
                # 5,2,3
                num1_1,b = compare(code[1], a) # 5: 1,4 2: 1,4 3: 0,3
                if num1_1 == 0:
                    numbers[3] = True
                    code[3] = a
                num1_4,b = compare(code[4], a) # 5: 1,2 #2: 2,3
                if num1_4==1 and num1_1 != 0:
                    numbers[5] = True
                    code[5] = a
                elif num1_4==2 and num1_1 != 0:
                    numbers[2] = True
                    code[2] = a
            if len(a)==6:
                # 9,6,0
                num1_1,b = compare(code[1], a) # 9: 0,4 6: 1,x 0: 0,x
                if num1_1==1:
                    numbers[6] = True
                    code[6] = a
                num1_4,b = compare(code[4], a) # 9: 0,2 0: 1
                if num1_4==1 and num1_1 != 1:
                    numbers[0] = True
                    code[0] = a
                elif num1_4==0 and num1_1 != 1:
                    numbers[9] = True
                    code[9] = a
        digit = ""
        for a in secondhalf.split():
            for i in range(10):
                if compare_codes(a,code[i]):
                    digit += str(i)
        assert(len(digit)==4)
        total += int(digit)
    return total

file = advent_file_reader.read_file(8)
print("part1: ", part1(file))
# part1:  440
print("part2: ", part2(file))
# part2:  1046281