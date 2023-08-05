'''
Implementing length conversions.
'''

# stdlib imports
from abc import ABC

# my imports
from utils import to_base_val, to_prefixed_val
from constants import FEET_PER_YARD, FEET_PER_METER, FEET_PER_MILE, YARDS_PER_MILE, INCHES_PER_FOOT

class Length(ABC):
    def __init__(self, length: float):
        super().__init__()
        self._length = length
    
    def get_length(self) -> float:
        return self._length

class Meter(Length):
    def __init__(self, length: float, prefix: str=''):
        super().__init__(length)
        self._prefix = prefix
        self._meter = to_base_val(length, prefix)
    
    def to_other_metric(self, prefix: str) -> float:
        return to_prefixed_val(self._meter, prefix)
    
    def to_foot(self) -> float:
        return self._meter * FEET_PER_METER

    def to_yard(self) -> float:
        return self.to_foot() / FEET_PER_YARD

    def to_mile(self) -> float:
        return self.to_foot() / FEET_PER_MILE
    
    def to_inch(self) -> float:
        return self.to_foot() * INCHES_PER_FOOT
    
    def __str__(self) -> str:
        suffix = 's' if self._length != 1.0 else ''
        return '{} {}meter{}'.format(self._length, self._prefix, suffix)

class Foot(Length):
    def __init__(self, length: float):
        super().__init__(length)
    
    def to_meter(self, prefix: str='') -> float:
        return to_prefixed_val(self._length / FEET_PER_METER, prefix)

    def to_yard(self) -> float:
        return self._length / FEET_PER_YARD

    def to_mile(self) -> float:
        return self._length / FEET_PER_MILE
    
    def to_inch(self) -> float:
        return self._length * INCHES_PER_FOOT
    
    def __str__(self) -> str:
        unit = 'feet' if self._length != 1.0 else 'foot'
        return '{} {}'.format(self._length, unit)

class Yard(Length):
    def __init__(self, length: float) -> float:
        super().__init__(length)
    
    def to_meter(self, prefix: str='') -> float:
        return to_prefixed_val(self.to_foot() / FEET_PER_METER, prefix)

    def to_foot(self) -> float:
        return self._length * FEET_PER_YARD

    def to_mile(self) -> float:
        return self._length / YARDS_PER_MILE
    
    def to_inch(self) -> float:
        return self.to_foot() * INCHES_PER_FOOT
    
    def __str__(self) -> str:
        suffix = 's' if self._length != 1.0 else ''
        return '{} yard{}'.format(self._length, suffix)

class Mile(Length):
    def __init__(self, length: float):
        super().__init__(length)
    
    def to_meter(self, prefix: str='') -> float:
        return to_prefixed_val(self.to_foot() / FEET_PER_METER, prefix)

    def to_foot(self) -> float:
        return self._length * FEET_PER_MILE

    def to_yard(self) -> float:
        return self._length * YARDS_PER_MILE
    
    def to_inch(self) -> float:
        return self.to_foot() * INCHES_PER_FOOT
    
    def __str__(self) -> str:
        suffix = 's' if self._length != 1.0 else ''
        return '{} mile{}'.format(self._length, suffix)

class Inch(Length):
    def __init__(self, length: float):
        super().__init__(length)
    
    def to_foot(self) -> float:
        return self._length / INCHES_PER_FOOT
    
    def to_mile(self) -> float:
        return self.to_foot() / FEET_PER_MILE
    
    def to_meter(self, prefix: str='') -> float:
        return to_prefixed_val(self.to_foot() / FEET_PER_METER, prefix)
    
    def to_yard(self) -> float:
        return self.to_foot() / FEET_PER_YARD
    
    def __str__(self) -> str:
        suffix = 'es' if self._length != 1.0 else ''
        return '{} inch{}'.format(self._length, suffix)