'''
Implementing volume conversions.
'''

from abc import ABC

class Volume(ABC):
    def __init__(self, vol: float):
        super().__init__()
        self._vol = vol
    
    def get_volume(self) -> float:
        return self._vol
    
class Liter(Volume):
    pass

class Gallon(Volume):
    pass

class Quart(Volume):
    pass

class Pint(Volume):
    pass

class Cup(Volume):
    pass

class Tablespoon(Volume):
    pass

class Teaspoon(Volume):
    pass