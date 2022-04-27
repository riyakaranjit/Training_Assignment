from functools import reduce


def exponent(x: int, y: int) -> int:
    return x ** y


def multiply_list(input_list: list) -> int:
    """
    Multiplies all the elements in the lsit
    :param input_list: Given input list
    :return: int: Multiple of all the elements
    """
    result = reduce((lambda x, y: x * y), input_list)
    return result


def upper_lowercase_count(input_string: str) -> str:
    lowercase_count = 0
    uppercase_count = 0
    for s in input_string:
        if s.islower():
            lowercase_count += 1
        elif s.isupper():
            uppercase_count += 1
    return f'The number of lowercase and uppercase in {input_string} are {lowercase_count} ' \
           f'and {uppercase_count} respectively. '


def is_pangram(input_string: str) -> bool:
    if len('abcdefghijklmnopqrstuvwxyz') - len(set(input_string.lower())) == 0:
        return True
    else:
        return False


def sorting(arg1: list) -> str:
    arg1 = sorted(arg1)
    return '-'.join(arg1)


def reverse(arg: str) -> str:
    return arg[::-1]


if __name__ == "__main__":
    X, Y = map(int, input("Enter the base and exponent separated by space: ").split())
    print(f'The exponential value of base {X} and exponent {Y} is: {exponent(X, Y)}')

    list1 = list(map(int, input("Enter the element of list separated by space: ").split()))
    print(multiply_list(list1))

    string1 = input('Enter a word to count its uppercase and lowercase: ')
    print(upper_lowercase_count(string1))

    given_string = input('Enter a string to check if its pangram or not: ')
    print(is_pangram(given_string))

    hyphen_separated_input = input("Enter words separated by hyphens: ").split('-')
    print(f'The sorted hyphen separated words is: \n {sorting(hyphen_separated_input)}')

    input_string = input('Enter a string to see its reserve: ')
    print(f'The reverse of {input_string} is: {reverse(input_string)}')

    lambda_func = lambda a, b: 2 * a + b
    print(lambda_func(2, 10))
