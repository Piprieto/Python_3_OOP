from abc import ABC, abstractmethod
"""The objective is to learn how to use abstract classes and inheritance in
Python, understanding: what an abstract class is, why it cannot be instantiated
directly, how a child class inherits and completes the behavior of the
abstract class and how attributes, methods, and docstrings work"""


class Character(ABC):
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name    # nombre del personaje
        self.is_alive = is_alive        # argumento opcional,por defecto True

    @abstractmethod
    def die(self):
        """Declare the abstract method die. Define that any character 
        must know how to "die" (or at least have a function for that)
        pass simply indicates "does nothing" in the base class."""
        pass


class Stark(Character):
    """
    Define the Stark class that inherits from Character; that is, Stark takes
    the structure defined in Character (attributes and methods) and
    completes/uses it. In other words: Character is a base recipe, and Stark is
    a concrete version of that recipe.
    """

    def __init__(self, first_name, is_alive=True):
        """We call the parent class constructor (Character.__init__)
        to perform the attribute assignment"""

        super().__init__(first_name, is_alive)
        

    def die(self):
        """Method: We changed the is_alive attribute of the object to False"""
        self.is_alive = False
