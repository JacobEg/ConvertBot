'''
Implementing temperature conversions.
'''
# stdlib imports
from abc import ABC

# my imports
from constants import FAHRENHEIT_AT_0_CELSIUS, CELSIUS_PER_FAHRENHEIT, KELVIN_AT_0_CELSIUS

class Temperature(ABC):
    '''
    Abrstract class for temperature, to be subclassed by all the other units
    '''
    def __init__(self, temp: float):
        super().__init__()
        self._temperature = temp

class Fahrenheit(Temperature):
    def __init__(self, temp: float):
        super().__init__(temp)
    
    def to_celsius(self):
        return (self._temperature - FAHRENHEIT_AT_0_CELSIUS) / CELSIUS_PER_FAHRENHEIT
    
    def to_kelvin(self):
        return self.to_celsius() + KELVIN_AT_0_CELSIUS

class Celsius(Temperature):
    def __init__(self, temp: float):
        super().__init__(temp)
    
    def to_fahrenheit(self):
        return (self._temperature * CELSIUS_PER_FAHRENHEIT) + FAHRENHEIT_AT_0_CELSIUS
    
    def to_kelvin(self):
        return self._temperature + KELVIN_AT_0_CELSIUS

class Kelvin(Temperature):
    def __init__(self, temp: float):
        super().__init__(temp)
    
    def to_fahrenheit(self):
        return  (self.to_celsius() * CELSIUS_PER_FAHRENHEIT) + FAHRENHEIT_AT_0_CELSIUS

    def to_celsius(self):
        return self._temperature - KELVIN_AT_0_CELSIUS