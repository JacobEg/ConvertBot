'''
Implementing temperature conversions.
'''
# stdlib imports
from abc import ABC

class Temperature(ABC):
    '''
    Abrstract class for temperature, to be subclassed by all the other units
    '''
    def __init__(self, temp: float):
        super().__init__()
        self._temperature = temp

class Fahrenheit(Temperature):
    def __init__(self, temp):
        super().__init__(temp)
    
    def to_celsius(self):
        return (self._temperature - 32) / 1.8
    
    def to_kelvin(self):
        return self.to_celsius() + 273.15

class Celsius(Temperature):
    def __init__(self, temp: float):
        super().__init__(temp)
    
    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32
    
    def to_kelvin(self):
        return self._temperature + 273.15

class Kelvin(Temperature):
    def __init__(self, temp: float):
        super().__init__(temp)
    
    def to_fahrenheit(self):
        return  (self.to_celsius() * 1.8) + 32

    def to_celsius(self):
        return self._temperature - 273.15