'''
Implementing temperature conversions.
'''
# stdlib imports
from abc import ABC

# my imports
from constants import FAHRENHEIT_AT_0_CELSIUS, FAHRENHEIT_PER_CELSIUS, KELVIN_AT_0_CELSIUS

class Temperature(ABC):
    '''
    Abrstract class for temperature, to be subclassed by all the other units
    '''
    def __init__(self, temp: float):
        super().__init__()
        self._temperature = temp
    
    def get_temperature(self) -> float:
        return self._temperature

class Fahrenheit(Temperature):
    def __init__(self, temp: float):
        super().__init__(temp)
    
    def to_celsius(self) -> float:
        return (self._temperature - FAHRENHEIT_AT_0_CELSIUS) / FAHRENHEIT_PER_CELSIUS
    
    def to_kelvin(self) -> float:
        return self.to_celsius() + KELVIN_AT_0_CELSIUS
    
    def __str__(self) -> str:
        return '{} ° Fahrenheit'.format(self._temperature)

class Celsius(Temperature):
    def __init__(self, temp: float):
        super().__init__(temp)
    
    def to_fahrenheit(self) -> float:
        return (self._temperature * FAHRENHEIT_PER_CELSIUS) + FAHRENHEIT_AT_0_CELSIUS
    
    def to_kelvin(self) -> float:
        return self._temperature + KELVIN_AT_0_CELSIUS
    
    def __str__(self) -> str:
        return '{} ° Celsius'.format(self._temperature)

class Kelvin(Temperature):
    def __init__(self, temp: float):
        super().__init__(temp)
    
    def to_fahrenheit(self) -> float:
        return  (self.to_celsius() * FAHRENHEIT_PER_CELSIUS) + FAHRENHEIT_AT_0_CELSIUS

    def to_celsius(self) -> float:
        return self._temperature - KELVIN_AT_0_CELSIUS
    
    def __str__(self) -> str:
        return '{} ° Kelvin'.format(self._temperature)