from S1E9 import Character
"""
Create two families that inherit from the Character class, that we can
instantiate without going through the Character class.
Find a solution so that "__str__" and "__repr__" return strings and not
objects. Write a Class method to create characters in a chain."""


class Baratheon(Character):
    """
    Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """The str method allows you to represent the object in a
        user-friendly way for the user"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """The repr method provides a developer-oriented representation
        of the object."""
        return self.__str__()
    """This returns what we specified in `str` because nothing else is needed
    here.If we needed to debug the code or the object had many important
    attributes, it would be better to do the following:
        def __repr__(self):
            return f"Persona(nombre={self.nombre!r}, edad={self.edad!r})"
    """

    def die(self):
        self.is_alive = False


class Lannister(Character):
    """
    Representing the Lannister family.
    """

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def die(self):
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
