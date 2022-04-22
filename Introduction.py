# from math import factorial  # use of built-in function (very fast)
from math import pi
import random


# 1.  Write a Python code to calculate Permutation (5,3)

def factorial(num: int) -> int:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


# Permutation formula: nPr = n!/(n-r)!\
def permutation(n, r):
    if r <= 0:
        return 'r must be greater than 0.'
    if n < r:
        n, r = r, n
    numerator = factorial(n)  # n!
    denominator = factorial(n - r)  # (n-r)!
    perm = numerator / denominator
    return perm


print("Permutation of (5,3): ", permutation(5, 3))


# 2. Write a Python code to calculate Combination (15,3)
# Combination formula: nCr = n!/r!(n-r)!

def combination(n, r):
    if r <= 0:
        return 'r must be greater than 0.'
    if n < r:
        n, r = r, n
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    comb = numerator / denominator
    return comb


print("Combination of (15,3): ", combination(15, 3))


# 3.  Write a Python code that takes the degree as input from the user and convert it into radian.

def degree_to_radian(d):
    radian = d * (pi / 180)
    print(radian)


degree = int(input('Enter degree to convert into radian: '))
degree_to_radian(degree)


# 4. Ask to enter two numbers (say, a and b). Generate two random numbers between those two numbers and find a
# combination of these two newly generated random numbers.

def combination_of_random_num(rand1, rand2) -> str:
    try:
        random1 = random.randint(rand1, rand2)
        random2 = random.randint(rand1, rand2)
    except ValueError:
        return 'The first number must be smaller than the second number.'
    else:
        comb = combination(random1, random2)
        return 'Combination of {} and {} is: {}'.format(random1, random2, comb)


a = int(input('Enter a random number: '))
b = int(input('Enter another random number: '))
print(combination_of_random_num(a, b))


# 7. Divide 1000 by 3 and print the answer with only 5 numbers after decimal.
def division_by_three():
    num = 1000 / 3
    print("Division of 1000 by 3: {:.5f}".format(num))


division_by_three()

