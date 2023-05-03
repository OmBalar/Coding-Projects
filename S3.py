t = int(input())

for i in range(t):
    n = int(input())

    cars = []

    for j in range(n):
        cars.append(int(input()))
    
    cars.reverse()

    needed = 1
    branch = [100001]
    added = 0
    count = 0

    while added != n:
        if count < len(cars):
            car = cars[count]
        
        else:
            car = 0

        if car == needed:
            needed += 1
            added += 1
            count += 1
        
        elif branch[0] == needed:
            branch.pop(0)
            needed += 1
            added += 1
        
        elif car < branch[0]:
            branch.insert(0, car)
            count += 1
        
        else:
            print("N")
            break

        if added + len(branch) - 1 == n:
            print("Y")
            break