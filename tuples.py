# 1. Convert tuples to list.
from math import sqrt, atan


def list_to_tuple(input_list: list) -> tuple:
    return tuple(input_list)


def vector_calculation():
    a = (20, 30)
    b = (30, 40)
    position_vector = tuple(map(lambda i, j: i - j, a, b))
    magnitude = sqrt(position_vector[0] ** 2 + position_vector[1] ** 2)
    direction = atan(position_vector[1] / position_vector[0])
    return magnitude, direction


# 3. Write a program to demonstrate data types that can be elements of a tuple.
def types_of_tuple():
    empty_tuple = ()
    similar_type_tuple = (1, 2, 3)  # similar data type
    mixed_tuple = (1, 'hi', 1.2,)  # mixed type
    nested_tuple = (['a', 'apple'], ('b', 'ball'), {'c': 'cat'})
    return f'Empty tuple: {empty_tuple} \n Tuple with similar data type: {similar_type_tuple} \n Tuple with similar ' \
           f'data type:{mixed_tuple} \n List and dictionary inside a tuple: {nested_tuple} '


def main():
    input_values_to_list = input('Enter a values separated by space in a list to convert into tuples:')
    print(list_to_tuple(input_values_to_list.split()))
    mag, dir = vector_calculation()
    print('The magnitude and direction of A(20, 30) and B(30,40) are: {:.3f} and {:.3f}'.format(mag, dir))
    print('the different data types that can be elements of tuples are:\n', types_of_tuple())
    my_tuple = 3, 4.6, "dog"  # without parenthesis
    print('Tuples can be assigned without parenthesis: ', my_tuple)
    tuple1, tuple2, tuple3 = my_tuple  # tuple unpacking
    print('Tuples can be unpacked without parenthesis: ', tuple1, tuple2, tuple3)
    tuple4 = 'apple',
    print('Adding a single element in a tuple: ', tuple4)


if __name__ == '__main__':
    main()
