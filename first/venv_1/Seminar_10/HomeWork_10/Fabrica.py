from Animals import Mammal, Bird, Fish, Animal


class AnimalFabric:

    def __init__(self, animal_class: str,  **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'voice':
                self.voice = value
            if key == 'hair':
                self.hair = value

    def get_info_animal(self):
        if self.animal_class == 'bird':
            return Bird(self.name, self.age, self.color, self.voice)
        elif self.animal_class == 'mammal':
            return Mammal(self.name, self.age, self.hair, self.voice, self.color)
        elif self.animal_class == 'fish':
            return Fish(self.name, self.age, self.color)
        else:
            return f'нет такого животного'


if __name__ == '__main__':

    animal1 = AnimalFabric(animal_class='bird', name='Аист', age=1, color='белый', voice='вой').get_info_animal()
    print(animal1.get_info())

    animal2 = AnimalFabric(animal_class='mammal', name='Кошка', age=5, hair='гладкая шерсть', voice='мяу-мяу', color='белая').get_info_animal()
    print(animal2.get_info())