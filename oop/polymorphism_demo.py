# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Raises an exception indicating that this method should be overridden."""
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle instance with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle instance with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)


# The following part should be in main.py for testing
if __name__ == "__main__":
    from polymorphism_demo import Shape, Rectangle, Circle

    def main():
        shapes = [
            Rectangle(10, 5),
            Circle(7)
        ]

        for shape in shapes:
            print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

    main()

