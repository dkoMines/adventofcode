import advent_file_reader
file = advent_file_reader.read_file(10)

d = {'(':')', '<':'>', '{':'}', '[':']'}
points = 0
incompLines = []

for line in file:
    line = line.strip()
    l = []
    errorFound = False
    for c in line:
        if c == '(' or c == '[' or c == '<' or c == '{':
            l.append(c)
        elif not errorFound:
            target = l.pop()
            if d[target] != c:
                if c == ')':
                    points += 3
                elif c == ']':
                    points += 57
                elif c == '}':
                    points += 1197
                elif c == '>':
                    points += 25137
                errorFound = True
    if not errorFound:
        incompLines.append(line)
print(points)

scores = []
# print(len(incompLines))
for line in incompLines:
    line.strip()
    score = 0
    l = []
    for c in line:
        if c == '(' or c == '[' or c == '<' or c == '{':
            l.append(c)
        else:
            target = l.pop()
            if d[target] != c:
                print("oh no")
    l.reverse()
    for c in l:
        # print(c)
        score *= 5
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4
    scores.append(score)
scores.sort()
print(scores[len(scores)//2])        