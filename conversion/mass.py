'''
Implementing mass conversions.
'''

# stdlib imports
from abc import ABC

# my imports
from utils import to_base_val, to_prefixed_val
from constants import OUNCES_PER_POUND, GRAMS_PER_OUNCE, GRAMS_PER_POUND

class Mass(ABC):
    def __init__(self, mass: float) -> None:
        super().__init__()
        self._mass = mass

class Gram(Mass):
    def __init__(self, mass: float, prefix: str) -> None:
        super().__init__(mass)
        self._prefix = prefix
        self._gram = to_base_val(mass, prefix)
    
    def to_pound(self):
        return self._gram / GRAMS_PER_POUND

    def to_ounce(self):
        return self._gram / GRAMS_PER_OUNCE

    def to_other_metric(self, prefix: str):
        if not prefix:
            return self._gram
        return to_prefixed_val(self._gram, prefix)

class Pound(Mass):
    def __init__(self, mass: float) -> None:
        super().__init__(mass)
    
    def to_gram(self):
        return self._mass * GRAMS_PER_POUND

    def to_ounce(self):
        return self._mass * OUNCES_PER_POUND

class Ounce(Mass):
    def __init__(self, mass: float) -> None:
        super().__init__(mass)
    
    def to_gram(self):
        return self._mass * GRAMS_PER_OUNCE

    def to_pound(self):
        return self._mass / OUNCES_PER_POUND