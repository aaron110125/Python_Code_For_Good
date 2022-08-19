#Making use of getters and setters methods

class degree_Celsius():
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_degree_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    #getter_method
    def get_temperature(self):
        return self._temperature

    #setter method
    def set_temperature(self,value):
        if value < -273.15:
            raise ValueError("Temperature is below -273.15 and is not possible")
        self._temperature = value

human = degree_Celsius(37)
print(human.get_temperature())
print(human.to_degree_fahrenheit())
print(human.set_temperature(-300))
print(human.get_temperature())
print(human.to_degree_fahrenheit())

