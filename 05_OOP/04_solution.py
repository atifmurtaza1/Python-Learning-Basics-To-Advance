class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand

    def set_brand(self,a):
        self.__brand = a
    
    def get_model(self):
        return self.__model


class ElectriCar(Car):
    def __init__(self,__brand,__model,battery_size):
        super().__init__(__brand,__model)
        self.battery_size = battery_size

    


my_car = Car("toota","Kia")
print(my_car.get_brand())
print(my_car.get_model())

my_electric_car = ElectriCar("Tesla","HYper", "860KWH")
print(my_electric_car.get_brand())
print(my_electric_car.get_model())
print(my_electric_car.battery_size)
print(my_electric_car.full_name())
print(my_car.full_name())

my_car.set_brand("Lic")

print(my_car.get_brand())
