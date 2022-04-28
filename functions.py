from functools import reduce
from sorting_algorithm_module import insertion_sort, bubble_sort, selection_sort
from lists import mean, variance, standard_deviation


def exponent(x: int, y: int) -> int:
    return x ** y


def multiply_list(input_list: list) -> int:
    """
    Multiplies all the elements in the list
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


def has_permission(page):
    """
    Example of accessing a function inside a function aka nested function. These internal functions are used for
    encapsulation for completely hiding the function from the global scope. Hence, they can't be accessed directly.
    :param page: input
    :return: function object
    """
    def permission(username):
        if username.lower() == 'admin':
            return f'{username.title()} has permission to access the {page}.'
        else:
            return f'{username.title()} doesn\'t has permission to access the {page}.'
    return permission


def f1():
    statement = 'I love coding.'

    def f2():
        nonlocal statement  # Nonlocal keyword defines the variable in global scope.
        statement = 'Me too'
        print(statement)

    f2()
    print(statement)


def main():
    X, Y = map(int, input("Enter the base and exponent separated by space: ").split())
    print(f'The exponential value of base {X} and exponent {Y} is: {exponent(X, Y)}')

    list1 = list(map(int, input("Enter the element of list separated by space: ").split()))
    print('Multiplies all the element: ', multiply_list(list1))

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

    check_admin_permission = has_permission('Admin Page')
    print(check_admin_permission('admin'))
    print(check_admin_permission('john'))

    f1()

    array = [78, 12, 10, 8, 59, 23, 27]
    print('Before bubble sort:', array)
    bubble_sort(array)
    print('After bubble sort:', array)

    array = [78, 12, 10, 8, 59, 23, 27]
    print('Before selection sort:', array)
    selection_sort(array)
    print('After selection sort:', array)

    array = [78, 12, 10, 8, 59, 23, 27]
    print('Before insertion sort:', array)
    insertion_sort(array)
    print('After insertion sort:', array)

    student_info = {'Richard': 24, 'Lara': 36, 'Prava': 45, 'Peter': 45, 'Judas': 96, 'Jimmy': 56,
                    'Jimi': 89, 'Ronaldo': 12, 'Messi': 10, 'Pogba': 100}
    students_marks = []
    for value in student_info.values():
        students_marks.append(value)
    nl = '\n'
    print(f'For the students {student_info} {nl}' 
          f'Mean: {mean(students_marks)} {nl}'
          f'Variance: {variance(students_marks)} {nl}'
          f'Standard Deviation: {standard_deviation(students_marks)}')


if __name__ == "__main__":
    main()
    

