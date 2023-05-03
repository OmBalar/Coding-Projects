j = int(input())
a = int(input())

jerseys = {}

for i in range(j):
    jerseys[i + 1] = input()

athletes = []

for i in range(a):
    a, b = input().split(' ')
    athletes.append([a, int(b)])

counter = 0

for jersey in athletes:
    if jersey[0] == "S":
        if jerseys.get(jersey[1], -1) != -1:
            counter += 1
            del jerseys[jersey[1]]

    elif jersey[0] == "M":
        if jerseys.get(jersey[1], -1) != -1 and (jerseys.get(jersey[1], -1) == "M" or jerseys.get(jersey[1], -1) == "L"):
            counter += 1
            del jerseys[jersey[1]]

    else:
        if jerseys.get(jersey[1], -1) != -1 and jerseys.get(jersey[1], -1) == "L":
            counter += 1
            del jerseys[jersey[1]]

print(counter)