class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
class Battery:
    def battery_info(self):
        return f"This is battery INfo"
    
class Engine:
    def engine_info(self):
        return f"This is Engine INfo"

class ElectricCarTwo(Battery,Engine,Car):
    pass


tesla = ElectricCarTwo("Tesla","Sonic")
print(tesla.engine_info())
print(tesla.battery_info())
