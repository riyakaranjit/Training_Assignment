def starts_with_B(input_list):
    output_list = []
    for i in input_list:
        if i.startswith('B'):
            output_list.append(i)
    return output_list


def union_of_list(list1: list, list2: list) -> list:
    """
    Union of two input lists
    :return: list
    """
    # return list(set(A).union(set(B)))  # Another method to find union using set's property
    return list(set(list1) | set(list2))  # Using sets | property


def intersection_of_list(list1: list, list2: list) -> list:
    """
    Intersection of two input lists
    :retur: list
    """
    # return list(set(A).intersection(set(B)))  # Another method to find intersection using set's property
    return list(set(list1) & set(list2))  # Using sets & property


def mean(input_list: list) -> int:
    return sum(input_list) / len(input_list)


def variance(input_list: list) -> int:
    var = sum(X - mean(input_list) for X in input_list) ** 2
    return var


def standard_deviation(input_list: list) -> float:
    var = variance(input_list)
    std = (var / len(input_list)) ** 0.5
    return std


def main():
    fifa = ['Italy', 'Argentina', 'Germany', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany', 'France']
    Bob = ['hurricane', 'tambourine', 'blowing', 'numb']
    A = ['a', 'b', 'c', 'd']
    B = ['1', 'a', '2', 'b']
    numbers = [1, 2, 3, 5, 88, 99, 55, 33, 41, 52]
    name_list = ['Liam', 'Olivia', 'Noah', 'Emma', 'Benjamin', 'Ava', 'Elijah', 'Ben', 'William', 'Sophia']
    print('Name of each students in list {} whose name starts with B:\n {}'.format(name_list, starts_with_B(name_list)))

    print('All the unique elements in the list {} are:\n{} '.format(fifa, list(set(fifa))))

    capitalized = [i.capitalize() for i in Bob]
    print("Changing the first alphabet of all the elements in list {} to capital: \n {}".format(Bob, capitalized))

    print('Union of list A {} and B {}: \n {}'.format(A, B, union_of_list(A, B)))

    print('Intersection of list A {} and B{}: \n {}'.format(A, B, intersection_of_list(A, B)))

    print('Mean of the list {} is:\n {}'.format(numbers, mean(numbers)))

    print('Standard deviation of the list {} is:\n {}'.format(numbers, standard_deviation(numbers)))


if __name__ == "__main__":
    main()
