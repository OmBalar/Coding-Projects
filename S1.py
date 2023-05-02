fl = input()
sl = input()

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

asterisks = sl.count('*')
b = False
extra = 0

for c in chars:
    x = fl.count(c)
    y = sl.count(c)

    if x < y:
        b = True
        break

    elif x > y:
        extra = extra + x - y

if b or asterisks != extra:
    print("N")

else:
    print("A")