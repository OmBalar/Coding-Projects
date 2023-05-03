n = int(input())
str = ""

for i in range(n):
    str += input()

strList = list(str)

t = strList.count('t')
t += strList.count('T')

s = strList.count('s')
s += strList.count('S')

if t > s:
    print("English")

else:
    print("French")
