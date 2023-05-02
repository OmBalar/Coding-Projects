n = int(input())
counter = 0

maxNum = int(n / 4)
minNum = 0

for i in range(maxNum + minNum + 1):
    sumI = maxNum * 4 + minNum * 5

    while sumI > n:
        minNum -= 1
        sumI = maxNum * 4 + minNum * 5

    if sumI == n:
        counter += 1

    maxNum -= 1
    minNum += 1

print(counter)
