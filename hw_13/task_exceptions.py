class CustomExceptions(Exception):
    pass


class RectangleSideValueException(CustomExceptions):
    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def __str__(self):
        return f'Стороны прямоугольника {self.width}, {self.height} не могут быть 0 или отрицательной длины!'


class RectangleSideTypeException(CustomExceptions):
    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def __str__(self):
        return f'Стороны прямоугольника {self.width}, {self.height} должны быть целыми или вещественными числами!'


class UnknownAnimalException(CustomExceptions):
    def __init__(self, animal_type: str):
        self.animal_type = animal_type

    def __str__(self):
        return f'Животное "{self.animal_type}" не поддерживается в данной версии фабрики!'


class AnimalTypeException(CustomExceptions):
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def __str__(self):
        return f'Некорректный ввод названия животного "{self.animal_type}"!'
