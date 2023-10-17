class Shape:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def say_name(self):
        return f"My name is {self.name}"

class Rectangle(Shape):
    def __init__(self, color, name, width, height):
        super().__init__(color, name)

class Circle(Shape):
    def __init__(self, color, name, radius):
        super().__init__(color, name)
