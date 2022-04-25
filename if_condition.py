def largest_number(n1: int, n2: int, n3: int) -> int:
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


def case_type(char: str) -> str:
    """
    Check if the char is uppercase or lowercase:
    :param char: input character
    :return: str
    """
    if char.isupper():
        return '{} Character is uppercase.'.format(char)
    elif char.islower():
        return '{} Character is lowercase.'.format(char)
    else:
        return '{} Character is mixed.'.format(char)


def is_vowel(char: str) -> str:
    if char in ('a', 'e', 'i', 'o', 'u') or ('A', 'E', 'I', 'O', 'U'):
        return '{} Alphabet is a vowel.'.format(char)
    else:
        return '{} Alphabet is consonant.'.format(char)


def is_leap_year(year: int) -> str:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return '{} is a leap year.'.format(year)
    else:
        return '{} is not a leap year.'.format(year)


def compute_grade(marks: int) -> str:
    if 100 >= marks >= 90:
        return 'The grade for marks {} is: A'.format(marks)
    elif 90 >= marks >= 80:
        return 'The grade for marks {} is: B'.format(marks)
    elif 80 >= marks >= 70:
        return 'The grade for marks {} is: C'.format(marks)
    elif 70 >= marks >= 60:
        return 'The grade for marks {} is: D'.format(marks)
    elif 60 >= marks >= 50:
        return 'The grade for marks {} is: E'.format(marks)
    elif marks <= 50:
        return 'The grade for marks {} is: F'.format(marks)
    else:
        return 'The marks cannot exceed 100.'


if __name__ == '__main__':
    # num1, num2, num3 = map(int, input("Enter 3 numbers separated by space: ").split())
    # print(largest_number(num1, num2, num3))
    # char1 = str(input('Enter a character to check its type: '))
    # print(case_type(char1))
    # alphabet = str(input('Enter a alphabet to check if it is vowel or consonant: '))
    # print(is_vowel(alphabet))
    # input_year = int(input('Enter a year to check if it is leap year or not: '))
    # print(is_leap_year(input_year))
    grade = int(input('Enter your marks to check your grade: '))
    print(compute_grade(grade))
