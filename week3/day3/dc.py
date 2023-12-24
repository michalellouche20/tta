import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None and diameter is not None:
            raise ValueError("Only one of radius or diameter should be specified.")
        elif radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter should be specified.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise ValueError("Unsupported operand type. You can only add two Circle instances.")

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise ValueError("Unsupported operand type. You can only compare two Circle instances.")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise ValueError("Unsupported operand type. You can only compare two Circle instances.")

circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)
circle3 = Circle(radius=3)

print(circle1) 
print(circle2.diameter)  
print(circle3.area)  

new_circle = circle1 + circle3
print(new_circle.radius)  

print(circle1 > circle3)  
print(circle1 == circle2)  

circles = [Circle(radius=2), Circle(radius=1), Circle(radius=4)]
sorted_circles = sorted(circles)
print(sorted_circles)