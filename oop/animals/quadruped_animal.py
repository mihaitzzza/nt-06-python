from abc import abstractmethod
from animals.base import Animal


class QuadrupedAnimal(Animal):
    @staticmethod
    @abstractmethod
    def speak():
        pass

    legs_no = 4


# Dog
# - name
# - breed
# - color
# - legs_no

class Dog(QuadrupedAnimal):
    @staticmethod
    def speak():
        print('Ham, ham!')


class Cat(QuadrupedAnimal):
    @staticmethod
    def speak():
        print('Miau, miau!')


class Cow(QuadrupedAnimal):
    @staticmethod
    def speak():
        print('Muu, muu!')


class Horse(QuadrupedAnimal):
    @staticmethod
    def speak():
        print('Ni, ho, ho!')
