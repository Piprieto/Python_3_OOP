from abc import ABC, abstractmethod


class Character(ABC):
   
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name    # nombre del personaje
        self.is_alive = is_alive        # argumento opcional,por defecto True

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
       
    def die(self):
        self.is_alive = False
