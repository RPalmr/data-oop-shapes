# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used

## Shape Challenge
### Define PI
PI = 3.14

### Classes and Methods
class Shape:
    """class shape"""
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def say_name(self):
        return f"My name is {self.name}"

    def say_color(self):
        """ Prints the color fo the shape"""
        return f"My name is {self.color}"

class Rectangle(Shape):
    """class rectangle"""
    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height
        self.name = name

    def say_name(self):
        """Returns a string that says the name of the rectangle and its shape type."""
        return super().say_name() + " and I am a rectangle."

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """class circle"""
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius
        self.name = name

    def say_name(self):
        """Returns a string that says the name of the circle and its shape type."""
        return super().say_name() + " and I am a circle."

    def area(self):
        """Calculates and returns the area of the circle."""
        return round(PI * self.radius ** 2, 2)

    def perimeter(self):
        """Calculates and returns the perimeter of the circle."""
        return round(2 * PI * self.radius, 2)
