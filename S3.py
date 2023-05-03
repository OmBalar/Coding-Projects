new_file = open("c:/Users/dhruv/Desktop/PythonFiles/2015CCC/s", "r")
list_of_lines = new_file.readlines()
print(1)
g = int(list_of_lines[0])
p = int(list_of_lines[1])

docked = [1] * g
counter = 0

for i in range(p):
    toDock = int(list_of_lines[i + 2])

    if toDock >= g:
        toDock = g - 1

    while docked[toDock] == 0 and toDock > 0:
        toDock -= 1

    if toDock > 0:
        docked[toDock] = 0
        counter += 1

    else:
        break

print(counter)