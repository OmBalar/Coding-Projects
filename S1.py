startingYear = int(input())
n = 0

while True:
    startingYear += 1
    currYear = str(startingYear)
    counter = 0

    for digit in currYear:
        counter += 1
        if currYear.count(digit) > 1:
            break
        elif counter == len(currYear):
            print(int(currYear))
            n = 1
            break

    if n == 1:
        break