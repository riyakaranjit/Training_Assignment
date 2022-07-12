from collections import deque
from string import ascii_lowercase


def deque_func():
    input_string = deque(ascii_lowercase)

    print(input_string)
    print('Item count:', str(len(input_string)))

    input_string.pop()  # Pops value from the end
    input_string.popleft()  # Pops value from the beginning

    input_string.append(2)  # Appends value in the end
    input_string.appendleft(1)  # Appends value in the beginning

    print(input_string)
    input_string.rotate(5)  # The last elements rotates then second last and so on unto n ...
    print(input_string)


def main():
    deque_func()


if __name__ == '__main__':
    main()
