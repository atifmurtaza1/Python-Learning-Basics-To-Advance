class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol And Diesel"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

tesla = ElectricCar("Tesla", "Hybrid","850KWh")
print(tesla.fuel_type())
print(tesla.brand)

safari = Car("safari","Phy")
print(safari.brand)
print(safari.fuel_type())