class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


car1 = Car('Toyota','Corolla')
car2 = ElectricCar('Tesla','Hyper','850KWh')

print(isinstance(car1,Car))
print(isinstance(car2,Car))
print(isinstance(car1,ElectricCar))
print(isinstance(car2,ElectricCar))