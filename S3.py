size, maxPitch, length = input().split()
size = int(size)
maxPitch = int(maxPitch)
length = int(length)

pitch = []  # List to store the pitches
j = 1  # I'll use that later
increment = 1  # Later

count = size  # Formula to check if the sample can be made [count = size + size - 2 + size - 3 + size - 4...+ size - size]
decrement = size - 1

while decrement > 0:
    count += decrement
    decrement -= 1

if count >= length:  # If it can be made...
    remainder = length - size
    sub = 1
    while remainder > 0:
        remainder -= sub
        sub += 1

    sub -= 1

    for i in range(1, size + 1):
        pitch.append(str(j))
        if j == 1:
            increment = 1

        elif j == sub:
            j = 0

        j += increment

    print(" ".join(pitch))
else:
    print(-1)