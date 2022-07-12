def bubble_sort(arr):
    """
    Comparing  two adjacent elements and swapping the values
    :param arr: unsorted list
    :return: sorted list
    """
    size = len(arr)

    for i in range(size):
        already_sorted = True  # to check if the elements are already sorted
        for j in range(0, size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False

        if already_sorted:
            break


def selection_sort(arr):
    """
    Swapping the first value with the minimum value. Also created two array: sorted(front)
    and unsorted(back)
    :param arr: unsorted list
    :return: sorted list
    """
    size = len(arr)

    for i in range(size - 1):
        minimum_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[minimum_index]:
                minimum_index = j
        if i != minimum_index:  # if the ith element already contains the minimum element, swap is not necessary
            arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
        # print(arr)


def insertion_sort(elements):
    size = len(elements)
    for current_index in range(1, size):
        current_element = elements[current_index]
        previous_index = current_index - 1
        while elements[previous_index] > current_element and previous_index >= 0:
            elements[previous_index + 1] = elements[previous_index]
            previous_index = previous_index - 1
        elements[previous_index + 1] = current_element


def main():
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


if __name__ == '__main__':
    main()

# print('The __name__ here is:', __name__)
