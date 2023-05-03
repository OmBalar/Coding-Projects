def winning(s):
    score = [0, 0, 0, 0]
    for j in range(6):
        if s[j] == 'W':
            score[poss[j][0]] += 3
            score[poss[j][1]] += 0
        elif s[j] == 'L':
            score[poss[j][0]] += 0
            score[poss[j][1]] += 3
        else:
            score[poss[j][0]] += 1
            score[poss[j][1]] += 1

    if score[t] == max(score) and score.count(max(score)) == 1:
        return True
    else:
        return False

def recurse(s, gp):  # s is a state, gp is the # of games played
    if gp == 6:
        if winning(s):
            global count
            count += 1
        return

    ind = s.index('-')  # Find next unplayed game

    s = s[:ind] + 'W' + s[ind + 1:]  # Win
    recurse(s, gp + 1)

    s = s[:ind] + 'L' + s[ind + 1:]  # Loss
    recurse(s, gp + 1)

    s = s[:ind] + 'T' + s[ind + 1:]  # Tie
    recurse(s, gp + 1)

    s = s[:ind] + '-' + s[ind + 1:]


poss = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

t = int(input("")) - 1
g = int(input(""))
count = 0

original = "------"

for i in range(g):
    x = input("").strip().split()
    a = int(x[0]) - 1
    b = int(x[1]) - 1
    sa = x[2]
    sb = x[3]
    if sa > sb:
        letter = "W"
    elif sa < sb:
        letter = "L"
    else:
        letter = "T"
    for j in range(6):
        if (a == poss[j][0] and b == poss[j][1]):
            original = original[:j] + letter + original[j + 1:]

recurse(original, g)

print(count)
