# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:
    """Класс прямоугольник, принимает ширину и высоту (целые либо числа с плавающей точкой)"""

    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimeter(self):
        """Вычисление периметра прямоугольника"""

        return (self.width + self.height) * 2

    def calc_area(self):
        """Вычисление площади прямоугольника"""

        return self.width * self.height

    def __add__(self, other):
        perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other._width
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.calc_perimeter() - other.calc_perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        return f'Perimeter: {self.calc_perimeter()}, width: {self.width}, height: {self.height}'

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __le__(self, other):
        return self.calc_area() <= other.calc_area()


if __name__ == '__main__':
    new_rect = Rectangle(30, 5)
    other_rect = Rectangle(5, 30)
    print(new_rect == other_rect)
    print(new_rect < other_rect)
    print(new_rect <= other_rect)
    print(new_rect >= other_rect)
    print(new_rect)

    print(help(Rectangle))
