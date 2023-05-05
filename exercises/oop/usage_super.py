from abc import abstractmethod

class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    @abstractmethod
    def __str__(self):
        pass    
    
class Square(Shape):
    def __init__(self, width, length):
        super().__init__(width, length)
        
    def __str__(self):
        return "This is Square"
    
    def area(self):
        return self.width * self.length

class Cube(Shape):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height
    
    def __str__(self):
        return "This is Cube"
        
    def volume(self):
        return self.width * self.length * self.height
    
s = Square(5,5)
print(f"Area of Square: {s.area()}")

c = Cube(3,4,5)
print(f"Volume of Cube: {c.volume()}")
    
ss = Shape(0,0)

for shapes in [s,c]:
    print(f"{shapes}")