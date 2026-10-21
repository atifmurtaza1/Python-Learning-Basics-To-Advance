class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car +=1


safar = Car("Safari","Hyper")
print(Car.total_car)
print(Car.total_car)
tesla = Car("Tesla","Sonic")
# print(tesla.total_car)


