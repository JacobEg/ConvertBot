'''
Implementing length conversions.
'''

# stdlib imports
from abc import ABC

# my imports
from utils import to_base_val, to_prefixed_val
from constants import FEET_IN_YARD, FEET_IN_METER, FEET_IN_MILE, YARDS_IN_MILE

class Length(ABC):
    def __init__(self, length: float) -> None:
        super().__init__()
        self._length = length

class Meter(Length):
    def __init__(self, length: float, prefix: str) -> None:
        super().__init__(length)
        self._prefix = prefix
        self._meter = to_base_val(length, prefix)
    
    def to_other_metric(self, prefix : str):
        if not prefix:
            return self._meter
        return to_prefixed_val(self._meter, prefix)
    
    def to_foot(self):
        return self._meter * FEET_IN_METER

    def to_yard(self):
        return self.to_foot() / FEET_IN_YARD

    def to_mile(self):
        return self.to_foot() / FEET_IN_MILE

class Foot(Length):
    def __init__(self, length: float) -> None:
        super().__init__(length)
    
    def to_meter(self, prefix: str):
        pass

    def to_yard(self):
        return self._length / FEET_IN_YARD

    def to_mile(self):
        return self._length / FEET_IN_MILE

class Yard(Length):
    def __init__(self, length: float) -> None:
        super().__init__(length)
    
    def to_meter(self, prefix: str):
        pass

    def to_foot(self):
        return self._length * FEET_IN_YARD

    def to_mile(self):
        return self._length / YARDS_IN_MILE

class Mile(Length):
    def __init__(self, length: float) -> None:
        super().__init__(length)
    
    def to_meter(self, prefix: str):
        pass

    def to_foot(self):
        return self._length * FEET_IN_MILE

    def to_yard(self):
        return self._length * YARDS_IN_MILE