"""Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки."""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def show_specs(self):
        pass


class Fish(Animal):
    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, depth: float):
        super().__init__(name)
        self.depth = depth

    def show_specs(self):
        if self.depth < self.LITTLE:
            return f'Мелководная рыба'
        elif self.depth > self.HIGHT:
            return f'Глубоководная рыба'
        else:
            return f'Среднеглубоководная рыба'

    def __str__(self):
        return f'{self.name} - {self.show_specs()}'


class Bird(Animal):
    def __init__(self, name: str, length: float):
        super().__init__(name)
        self.length = length

    def show_specs(self):
        return self.length * 2


class Cat(Animal):
    LONG = 5
    SHORT = 1

    def __init__(self, name: str, fur_length: float):
        super().__init__(name)
        self.fur_length = fur_length

    def show_specs(self):
        if self.fur_length < self.SHORT:
            return f'Бесшерстная порода'
        elif self.SHORT <= self.fur_length < self.LONG:
            return f'Короткошерстная порода'
        else:
            return f'Длинношерстная порода'


if __name__ == '__main__':
    fish_1 = Fish('karas', 10)
    bird_1 = Bird('vorobey', 0.3)
    cat_1 = Cat('domashnyaya polosataya', 3)

    animal_list = [fish_1, bird_1, cat_1]
    for animal in animal_list:
        print(animal.show_specs())
