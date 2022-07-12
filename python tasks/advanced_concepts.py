from dataclasses import dataclass, astuple, asdict, field
from math import radians, sin, asin, cos, sqrt
import random


@dataclass
class Position:
    """
    The default value for the dunder methods are:
        dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
    """
    name: str
    longitude: float = 0.0  # Assigning a default value
    latitude: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.longitude), radians(other.longitude)
        phi_1, phi_2 = radians(self.latitude), radians(other.latitude)
        h = (sin((phi_2 - phi_1) / 2) ** 2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2)
        return 2 * r * asin(sqrt(h))


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: str
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        print('The __post_init is called!')
        self.can_vote = 18 <= self.age <= 75
        self.sort_index = self.age  # Sorts by age, by default sorts by name.


person1 = Person('Mark Lucas', 12)
print(person1)
members = [
    Person(name='John', age=25),
    Person(name='Bob', age=35),
    Person(name='Alice', age=30)
]
sorted_member = sorted(members)
print('sorted_member', sorted_member)
for member in members:
    print(f'{member.name}(age={member.age})')


def list_comprehension():
    # Conditional List Comprehensions
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    fruits_with_a = [x for x in fruits if "a" in x]
    print(fruits_with_a)

    number_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
    print(number_list)

    obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
    print(obj)

    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()
    word_lengths = [len(word) for word in words if word != "the"]
    print(words)
    print(word_lengths)


def first_generator_func():
    """
    They are special kind of function that returns a lazy iterators, where you can iterate objects like a list.
    But, unlike list, lazy iterators do not store their contents in memory. You can ask for the next value from
    the iterable as many times as necessary until you've reached the end.

    For loop takes an iterator and iterates it over using next() function and it automatically ends when StopIteration
    is raised.
    """
    # returns a 1st number between 1 and 15
    yield random.randint(1, 15)

    # returns next 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)


def main():
    list_comprehension()

    oslo = Position('Oslo', 10.8, 59.9)
    vancouver = Position('Vancouver', -123.1, 49.3)
    print(asdict(oslo))  # Conversion of an instance of dataclass to dict / tuple
    print(f'{oslo.name} is at {oslo.latitude}N , {oslo.longitude}E.')
    print(astuple(vancouver))
    print(f'The distance between {oslo.name} and {vancouver.name} is: {oslo.distance_to(vancouver)}')



    # While dealing with the iterators, we need to keep a count of iterations.

    for count, random_num in enumerate(first_generator_func(), start=1):
        print(f'The next number {count} is: {random_num}')


if __name__ == '__main__':
    main()
