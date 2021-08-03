from abc import abstractmethod


class Animal:
    def __init__(self, name, breed):
        # print('This is the constructor of Dog class.')
        # self.name = name  # public attribute
        # self._name = name  # protected attribute
        # self.__name = name  # private attribute => _Dog__name
        self._name = name
        self._breed = breed
        self.legs_no = None

    @property
    def name(self):
        # verify if access is allowed
        return self._name

    # def get_name(self):
    #     # verify if access is allowed
    #     return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # def set_name(self, name):
    #     # verify if access is allowed
    #     self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def breed(self):
        # verify if access is allowed
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed

    # def set_name(self, name):
    #     # verify if access is allowed
    #     self._name = name

    @breed.deleter
    def breed(self):
        del self._breed

    @property
    def name_and_breed(self):
        return f'{self._name} - {self._breed}'

    @staticmethod
    @abstractmethod
    def speak():
        pass

    def __str__(self):
        return f'Object of type {type(self)} with name = "{self._name}"'

    def __repr__(self):
        return f'<{type(self).__name__}, {self._name}>'
