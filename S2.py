n = int(input())

studentAnswers = []
correctAnswers = []

for i in range(n):
    studentAnswers.append(input())

answersCorrect = 0

for i in range(n):
    if studentAnswers[i] == input():
        answersCorrect += 1

print(answersCorrect)
