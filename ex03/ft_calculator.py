"""Write a calculator class that is able to do calculations (addition, 
multiplication, subtraction, division) of vector with a scalar."""

class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: division by zero")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
