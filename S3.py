t = int(input())
answer = []

for z in range(t):
    m, x, y = input().split(" ")
    m = int(m)
    x = int(x)
    y = int(y)

    if m == 1:
        x += 1
        y += 1

    crystalArray = [[2, 1], [3, 1], [4, 1], [3, 2]]
    possibleCrystal = [[2, 2], [3, 3], [4, 2]]

    def checkCrystal(m, x, y):
        cells = 5 ** (m - 1)
        xCheck = x
        yCheck = y

        if m != 1:

            if xCheck <= cells:
                xCheck = 1

            elif xCheck > cells and xCheck <= 2 * cells:
                xCheck = 2

            elif xCheck > 2 * cells and xCheck <= 3 * cells:
                xCheck = 3

            elif xCheck > 3 * cells and xCheck <= 4 * cells:
                xCheck = 4

            else:
                xCheck = 5

            if yCheck <= cells:
                yCheck = 1

            elif yCheck > cells and yCheck <= 2 * cells:
                yCheck = 2

            elif yCheck > 2 * cells and yCheck <= 3 * cells:
                yCheck = 3

            elif yCheck > 3 * cells and yCheck <= 4 * cells:
                yCheck = 4

            else:
                yCheck = 5

        if [xCheck, yCheck] in crystalArray:
            return "crystal"

        elif [xCheck, yCheck] in possibleCrystal and m != 1:
            return checkCrystal(m - 1, x / 5 + (x % cells) / 5, y / 5 + (y % cells) / 5)
        else:
            return "empty"

    
    answer.append(checkCrystal(m, x, y))

for i in answer:
    print(i)