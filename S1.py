j = int(input())

if j < 4:
    print(0)

elif j == 4:
    print(1)

else:
    sumNum = [1]
    increment = 2

    for i in range(j - 4):
        sumNum.append(sumNum[i] + increment)
        increment += 1

    print(sum(sumNum))