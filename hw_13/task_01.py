"""Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например,
нельзя создавать прямоугольник со сторонами
отрицательной длины."""

from hw_10.task_06s import Bird, Fish, Cat
from task_exceptions import *


class Rectangle:
    """Класс прямоугольник, принимает ширину и высоту (целые либо числа с плавающей точкой)"""

    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height
        if not isinstance(self.width, int | float) or not isinstance(self.height, int | float):
            raise RectangleSideTypeException(self.width, self.height)
        if self.width <= 0 or self.height <= 0:
            raise RectangleSideValueException(self.width, self.height)

    def calc_perimeter(self):
        """Вычисление периметра прямоугольника"""

        return (self.width + self.height) * 2

    def calc_area(self):
        """Вычисление площади прямоугольника"""

        return self.width * self.height

    def __add__(self, other):
        perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other.width
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


class AnimalFactory:
    def __init__(self, animal_type: str, name: str, spec: float):
        animal_types = ('fish', 'bird', 'cat')
        self.animal_type = animal_type
        self.name = name
        self.spec = spec
        if not isinstance(self.animal_type, str):
            raise AnimalTypeException(animal_type)
        if self.animal_type.lower() not in animal_types:
            raise UnknownAnimalException(animal_type)

    def create_animal(self):
        if self.animal_type.lower() == 'fish':
            return Fish(self.name, self.spec)
        elif self.animal_type.lower() == 'bird':
            return Bird(self.name, self.spec)
        elif self.animal_type.lower() == 'cat':
            return Cat(self.name, self.spec)


if __name__ == '__main__':
    new_rect_1 = Rectangle(0.5, -5)
    new_rect_2 = Rectangle('f')
    new_animal_1 = AnimalFactory('snake', 'cobra', 10).create_animal()
    new_animal_2 = AnimalFactory(1, 'karas', 10).create_animal()
