from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A false king born from two houses: multiple inheritage
    The overall objective of this exercise is to understand inheritance and
    roperties.
    - Multiple inheritance (Baratheon, Lannister)
    - Using @property to modify physical characteristics
    Without using external functions"""

    def __init__(self, first_name):
        super().__init__(first_name)
        """ super calls the parent class constructor, but there are two parents
        here, so the MRO (the method Python uses to decide which class to use
        first) comes into play in this case: King-->Baratheon-->Lannister"""

    # ===== EYES =====
    """@property, @setter, get, and set are used to control how data is 
    accessed and modified within an object:
    @property → read as if it were a variable
    .setter → write with control
    get → method for reading
    set → method for writing
    _variable → protected internal attribute"""

    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, value):
        self.eyes = value

    # ===== HAIRS =====
    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        self._hairs = value

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, value):
        self.hairs = value
