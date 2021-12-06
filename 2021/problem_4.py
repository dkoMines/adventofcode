import advent_file_reader


def checkRows(board):
    for line in board:
        b = True
        for c in line:
            if c != 'X':
                b = False
        if b:
            return True
    return False

def checkCols(board):
    for j in range(len(board[0])):
        b = True
        for i in range(len(board)):
            if board[i][j] != 'X':
                b = False
        if b:
            return True
    return False

def calcRest(board):
    sum = 0
    for line in board:
        for c in line:
            if c != 'X':
                c = int(c)
                sum += c
    return sum

def board_win_turn(board, numsCalled):
    c = 0
    for num in numsCalled:
        num = int(num)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == num:
                    board[i][j] = 'X'
                    if checkRows(board) or checkCols(board):
                        return c, num, calcRest(board)
        c += 1

def part1_2(file, part):
    numsCalled = file[0].split(',')
    b = 0
    boards = []
    board = []
    # Set up boards
    for i in range(2,len(file)):
        line = file[i].split()
        if len(line) == 5:
            for i in range(len(line)):
                line[i] = int(line[i])
            board.append(line)
        if len(board) == 5:
            boards.append(board)
            board = []
    stats = []
    for board in boards:
        turn, num, calcRest = board_win_turn(board, numsCalled)
        stats.append([turn,num,calcRest])
    if part == 1:
        max = 9999999999
        bestBoard = stats[0]
        for s in stats:
            if s[0] < max:
                bestBoard = s
                max = s[0]
        # print(bestBoard)
        return bestBoard[1]*bestBoard[2]
    elif part == 2:
        min = -1
        bestBoard = stats[0]
        for s in stats:
            if s[0] > min:
                bestBoard = s
                min = s[0]
        # print(bestBoard)
        return bestBoard[1]*bestBoard[2]




file = advent_file_reader.read_file(4)
print("part1: ", part1_2(file,1))
# part1:  35670
print("part2: ", part1_2(file,2))
# part2:  22704