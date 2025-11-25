import math
from abc import ABC, abstractmethod

class Graph(ABC):
    def area(self) -> float:
        raise NotImplementedError
    
    def perimeter(self) -> float:
        raise NotImplementedError

class Rectangle(Graph):
    a = 0.0
    b = 0.0
    def __init__(self, a : float, b : float):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2 * (self.a + self.b)

class Ciecle(Graph):
    r = 0.0
    def __init__(self, r : float):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r
    
    def perimeter(self):
        return 2 * math.pi * self.r

class Triangle(Graph):
    a = 0.0
    b = 0.0
    c = 0.0
    def __init__(self, a : float, b : float, c : float):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
if __name__ == "__main__":
    rect = Rectangle(3, 4)
    print(f"Rectangle area: {rect.area():.2f}")
    print(f"Rectangle perimeter: {rect.perimeter():.2f}")

    circle = Ciecle(5)
    print(f"Circle area: {circle.area():.2f}")
    print(f"Circle perimeter: {circle.perimeter():.2f}")

    triangle = Triangle(3, 4, 5)
    print(f"Triangle area: {triangle.area():.2f}")
    print(f"Triangle perimeter: {triangle.perimeter():.2f}")