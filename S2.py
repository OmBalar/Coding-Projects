x = int(input())
sameGroup = []
diffGroup = []
sameNames = []
diffNames = []

for i in range(x):
    names = input().split()
    sameNames.append(names[0])
    sameNames.append(names[1])
    sameGroup.append(names)

y = int(input())
for i in range(y):
    names = input().split()
    diffNames.append(names[0])
    diffNames.append(names[1])
    diffGroup.append(names)

g = int(input())
counter = 0
for i in range(g):
    member1, member2, member3 = input().split()

    if member1 in sameNames:
        j = sameGroup[int(sameNames.index(member1) / 2)]
        if j[1] != member1 and j[1] != member2 and j[1] != member3:
            counter += 1

    if member2 in sameNames:
        j = sameGroup[int(sameNames.index(member2) / 2)]
        if j[1] != member1 and j[1] != member2 and j[1] != member3:
            counter += 1

    if member3 in sameNames:
        j = sameGroup[int(sameNames.index(member3) / 2)]
        if j[1] != member1 and j[1] != member2 and j[1] != member3:
            counter += 1

    if member1 in diffNames:
        k = diffGroup[int(diffNames.index(member1) / 2)]
        if k[1] == member2 or k[1] == member3:
            counter += 1

    if member2 in diffNames:
        k = diffGroup[int(diffNames.index(member2) / 2)]
        if k[1] == member1 or k[1] == member3:
            counter += 1

    if member3 in diffNames:
        k = diffGroup[int(diffNames.index(member3) / 2)]
        if k[1] == member1 or k[1] == member2:
            counter += 1

print(counter)