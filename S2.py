w = int(input())
n = int(input())
sum = [0, 0, 0, 0]
loop = True

for i in range(n):
    sum.append(int(input()))
    sum.pop(0)

    if sum[0] + sum[1] + sum[2] + sum[3] > w and loop:
        print(i)
        loop = False
