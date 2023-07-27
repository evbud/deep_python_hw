"""Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики."""

from task_06s import Fish, Bird, Cat


class AnimalFactory:
    def __init__(self, animal_type: str, name: str, spec: float):
        self.animal_type = animal_type
        self.name = name
        self.spec = spec

    def create_animal(self):
        if self.animal_type.lower() == 'fish':
            return Fish(self.name, self.spec)
        elif self.animal_type.lower() == 'bird':
            return Bird(self.name, self.spec)
        elif self.animal_type.lower() == 'cat':
            return Cat(self.name, self.spec)


if __name__ == '__main__':
    new_fish = AnimalFactory('Fish', 'karas', 10).create_animal()
    print(f'{new_fish.name}, {new_fish.show_specs()}')
    print(new_fish)
    new_bird = AnimalFactory('bird', 'chaika', 1).create_animal()
    print(f'{new_bird.name}, {new_bird.show_specs()}')
    new_cat = AnimalFactory('cat', 'shinshila', 5).create_animal()
    print(f'{new_cat.cat_name}, {new_cat.show_specs()}')
