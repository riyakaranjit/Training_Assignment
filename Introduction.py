# from math import factorial  # use of built-in function (very fast)
from math import pi
import random


# 1.  Write a Python code to calculate Permutation (5,3)

def factorial(num: int) -> int:
    """
    calculates the factorial of a number
    :param num: input number
    :return: int
    """
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


def permutation(n, r):
    """
    Permutation formula: nPr = n!/(n-r)!
    :param n: total number of objects
    :param r: subset of n
    :return: int
    """
    if r <= 0:
        return 'r must be greater than 0.'
    if n < r:
        n, r = r, n
    numerator = factorial(n)  # n!
    denominator = factorial(n - r)  # (n-r)!
    perm = numerator / denominator
    return perm


# 2. Write a Python code to calculate Combination (15,3)

def combination(n, r):
    """
    Combination formula:  nCr = n!/r!(n-r)!
    :param n: total number of objects
    :param r: subset of n
    :return: int
    """
    if r <= 0:
        return 'r must be greater than 0.'
    if n < r:
        n, r = r, n
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    comb = numerator / denominator
    return comb


# 3.  Write a Python code that takes the degree as input from the user and convert it into radian.

def degree_to_radian(deg: int) -> float:
    radian = deg * (pi / 180)
    return radian


# 4. Ask to enter two numbers (say, a and b). Generate two random numbers between those two numbers and find a
# combination of these two newly generated random numbers.

def combination_of_random_num(rand1, rand2) -> str:
    try:
        random1 = random.randint(rand1, rand2)
        random2 = random.randint(rand1, rand2)

        comb = combination(random1, random2)
        return 'Combination of {} and {} is: {}'.format(random1, random2, comb)
    except ValueError:
        return 'The first number must be smaller than the second number.'


# 7. Divide 1000 by 3 and print the answer with only 5 numbers after decimal.
def division_by_three():
    num = 1000 / 3
    print("Division of 1000 by 3: {:.5f}".format(num))


# division_by_three()

def decimal_to_binary(n):
    return "{0:#b}".format(int(n))


def decimal_to_hexadecimal(n):
    return "{0:#x}".format(int(n))


if __name__ == "__main__":
    print("Permutation of (5,3): ", permutation(5, 3))
    print("Combination of (15,3): ", combination(15, 3))

    degree = int(input('Enter degree to convert into radian: '))
    print(degree_to_radian(degree))
    a = int(input('Enter a random number: '))
    b = int(input('Enter another random number: '))
    print(combination_of_random_num(a, b))
    print('The binary conversion of 108 is: ', decimal_to_binary(108))
    print('The hexadecimal conversion of 1008 is:', decimal_to_hexadecimal(1008))
