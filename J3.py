# Input on the number of rolls
n = int(input())

# Set the score for both people to 100
score1 = 100
score2 = 100

# Go through a loop which repeats for how many times they roll
for i in range(n):
    # Get the input on what they roll and store the value in p1 and p2
    p1, p2 = input().split(" ")

    # Convert both of them to integers
    p1 = int(p1)
    p2 = int(p2)

    # Check which person rolled a bigger number
    # Decrease points from the person who rolled a smaller number
    if p1 > p2:
        score2 -= p1
    
    elif p2 > p1:
        score1 -= p2

# Output their scores
print(score1)
print(score2)