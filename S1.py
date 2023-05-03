k = int(input())
sumInt = []

for i in range(k):
    j = int(input())

    if j == 0:
        del sumInt[-1]

    else:
        sumInt.append(j)

print(sum(sumInt))