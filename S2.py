# Way to check if a number is prime
from math import sqrt


def is_prime(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


num_inputs = int(input(""))

for i in range(num_inputs):
    n = int(input(""))

    sumX = n * 2

    for i in range(0, n, 2):
        if is_prime(i + 1) and is_prime(sumX - i - 1):
            print(str(i + 1) + " " + str(sumX - i - 1))
            break
