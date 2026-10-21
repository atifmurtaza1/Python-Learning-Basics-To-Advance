class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"

class ElectriCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_electri_car = ElectriCar("Tesla","Hybrid","850KWh")

print(my_electri_car.brand)
print(my_electri_car.model)
print(my_electri_car.battery_size)
print(my_electri_car.fullName())