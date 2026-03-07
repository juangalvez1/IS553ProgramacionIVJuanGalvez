from io import *
import math

class Triangulo:
    def __init__(self, side1 = 0, side2 = 0, side3 = 0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        semiPerimeter = (self.side1 + self.side2 + self.side3) / 2

        area = math.sqrt(semiPerimeter * (semiPerimeter - self.side1) * (semiPerimeter - self.side2) * (semiPerimeter - self.side3))

        return area
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def triangleType(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Isósceles"
        else:
            return "Escaleno"
        
def main():
    a = float(input("Ingrese la longitud del lado 1: "))
    b = float(input("Ingrese la longitud del lado 2: "))
    c = float(input("Ingrese la longitud del lado 3: "))

    triangle = Triangulo(a, b, c)

    print(f"Esta es el área del triángulo: {triangle.area()}")
    print(f"Este es el perímetro del triángulo: {triangle.perimeter()}")
    print(f"La clasificación del triángulo es: {triangle.triangleType()}")

main()