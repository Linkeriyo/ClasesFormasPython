import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:
    def __init__(self, color, center, name):
        self.color = color
        self.center = center
        self.name = name

    def print(self):
        print("Forma:\n" +
              "Color: " + self.color + "\n" +
              "Centro: " + str(self.center.x) + ", " + str(self.center.y) + "\n" +
              "Nombre: " + self.name
              )

    def setcolor(self, color):
        self.color = color

    def getcolor(self):
        return self.color

    def movecenter(self, center):
        self.center = center


class Rectangle(Shape):
    def __init__(self, color, center, name, bigSide, smallSide):
        super().__init__(color, center, name)
        self.bigSide = bigSide
        self.smallSide = smallSide

    def print(self):
        print("Rectángulo:\n" +
              "Color: " + self.color + "\n" +
              "Centro: " + str(self.center.x) + ", " + str(self.center.y) + "\n" +
              "Nombre: " + self.name + "\n" +
              "Lado mayor: " + str(self.bigSide) + "\n" +
              "Lado menor: " + str(self.smallSide)
              )

    def getarea(self):
        return self.smallSide * self.bigSide

    def getperimeter(self):
        return self.smallSide * 2 + self.bigSide * 2

    def scale(self, scale):
        self.bigSide = self.bigSide * scale
        self.smallSide = self.smallSide * scale


class Ellipse(Shape):
    def __init__(self, color, center, name, bigRadius, smallRadius):
        super().__init__(color, center, name)
        self.bigRadius = bigRadius
        self.smallRadius = smallRadius

    def print(self):
        print("Elipse:\n" +
              "Color: " + self.color + "\n" +
              "Centro: " + str(self.center.x) + ", " + str(self.center.y) + "\n" +
              "Nombre: " + self.name + "\n"
              "Radio mayor: " + str(self.bigRadius) + "\n" +
              "Radio menor: " + str(self.smallRadius)
              )

    def getarea(self):
        return math.pi * (self.bigRadius * self.smallRadius)


class Square(Rectangle):

    def __init__(self, color, center, name, sides):
        super().__init__(color, center, name, sides, sides)


class Circle(Ellipse):
    def __init__(self, color, center, name, radius):
        super().__init__(color, center, name, radius, radius)


def main():
    shape = Shape("amarillo", Point(4, 2), "marta")
    rectangle = Rectangle("rojo", Point(2, 3), "manolo", 5, 3)
    ellipse = Ellipse("azul", Point(1, 5), "pepe", 3, 2)
    square = Square("cyan", Point(6, 2), "jose", 2)
    circle = Circle("grey", Point(1, 6), "paco", 10)

    shape.print()
    print("------------------------------------------")
    rectangle.print()
    print("Area: " + str(rectangle.getarea()))
    print("------------------------------------------")
    ellipse.print()
    print("Area: " + str(ellipse.getarea()))
    print("------------------------------------------")
    square.print()
    print("Area: " + str(square.getarea()))
    print("------------------------------------------")
    circle.print()
    print("Area: " + str(circle.getarea()))

    print("\nAñadiendo los objetos anteriores a la lista...")
    list = [shape, rectangle, ellipse, square, circle]
    print("Estableciendo azul a todas las formas y moviéndolas al origen de coordenadas...")
    for i in list:
        i.setcolor("azul")
        i.movecenter(Point(0, 0))

    shape.print()
    print("------------------------------------------")
    rectangle.print()
    print("Area: " + str(rectangle.getarea()))
    print("------------------------------------------")
    ellipse.print()
    print("Area: " + str(ellipse.getarea()))
    print("------------------------------------------")
    square.print()
    print("Area: " + str(square.getarea()))
    print("------------------------------------------")
    circle.print()
    print("Area: " + str(circle.getarea()))


if __name__ == "__main__":
    main()
