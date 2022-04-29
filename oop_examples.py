class Polygon:
    """
    This is the Base Class.
    """

    def __init__(self, number_of_sides: int):
        self.n = number_of_sides
        self.sides = [0 for i in range(self.n)]

    def __repr__(self):
        return str(self.n)

    def input_sides(self):
        self.sides = [float(input(f'Enter side {i + 1}: ')) for i in range(self.n)]
        # return self.sides

    def display_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is: ", self.sides[i])

    def find_area(self):
        pass

    def fact(self) -> str:
        return 'Fun Fact: I am a Polygon.'


class Triangle(Polygon):
    """
    This is a child class inherited from Polygon base class.
    """

    def __init__(self):
        super().__init__(3)

    def find_perimeter(self) -> str:
        return 'Perimeter of a triangle:'.format(sum(self.sides))

    def find_area(self):  # When the object calls find_area, this will be called instead of one from base class.
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return 'The area of the triangle is: {}'.format(area)


class Square(Polygon):
    """
    This is a child class inherited from Polygon base class.
    """

    def __init__(self):
        super().__init__(4)

    def find_area(self) -> str:
        a, b, c, d = self.sides
        if a == b == c == d:
            return 'Area of square: {}'.format(a ** 2)
        else:
            return 'Not a square!'

    def fact(self):
        super().fact()  # super function is used to call the method of base class
        return f"I am being called from {__class__} class."


class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


def main():
    """
    Few examples demonstrating Polymorphism and Inheritance:
    """
    scalar_triangle = Triangle()  # instantiating a new object for Triangle class.

    scalar_triangle.input_sides()
    scalar_triangle.display_sides()
    print(scalar_triangle.find_perimeter())
    print(scalar_triangle.find_area())
    print(scalar_triangle.fact())  # This calls the fact() from base class as it does not have one of its own.

    sq = Square()  # instantiating a new object for Square class.

    sq.input_sides()
    sq.display_sides()
    print(sq.find_area())
    print(sq.fact())  # This calls the fact() from its child class as it does have one its own fact().

    # This is an example for multiple inheritance.
    td = TextDescriber('hi hello hi  hello world')
    print('Multiple Resolution order: ', TextDescriber.mro())  # Own, Left, Right and at last class object
    print('--------')
    print(td.tokens)
    print(td.vocab)
    print(td.word_count)


if __name__ == '__main__':
    main()
