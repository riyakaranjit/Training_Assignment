def multiply_matrices(matrix1: list, matrix2: list) -> list:
    """
    Multiply 2 3*3 matrices.
    :param matrix1: Given 3*3 matrix
    :param matrix2: Given 3*3 matrix
    :return: 3*3 matrix multiple of input matrix
    """
    result = [[0] * len(matrix1) for _ in range(len(matrix1))]  # create an empty list to store the result
    for m in range(len(matrix1)):  # m * p = p * n = m * n
        for n in range(len(matrix2[0])):
            for p in range(len(matrix2)):
                result[m][n] += matrix1[m][p] * matrix2[p][n]
    return result


def odd_numb_pattern():
    rows = int(input('Enter number of rows: '))

    for j in range(1, rows*2, 2):
        print('F' * j)


def fibonacci_pattern():
    total_numbers = int(input('Enter number of rows: '))
    first, second = 1, 1
    fibonacci_list = [first, second]
    for x in range(2, total_numbers):
        next = first + second
        fibonacci_list.append(next)
        first = second
        second = next
    print(fibonacci_list)
    for i in fibonacci_list:
        print('F' * i)


def main():
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = [[111, 22, 33],
         [44, 55, 56],
         [47, 86, 19]]
    C = [[111, 22, 33, 44],
         [44, 55, 56, 1],
         [47, 86, 19, 2],
         [1, 2, 22, 3]]
    D = [[11, 22, 3, 4],
         [4, 5, 6, 1],
         [7, 6, 19, 2],
         [1, 2, 22, 3]]

    print(f'Matrix multiplication of {A} and {B} is: \n {multiply_matrices(A, B)}')
    print(f'Matrix multiplication of {C} and {D} is: \n {multiply_matrices(C, D)}')

    odd_numb_pattern()
    fibonacci_pattern()


if __name__ == "__main__":
    main()
