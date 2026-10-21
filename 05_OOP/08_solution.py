class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model
    @property
    def model(self):
       return self.__model

tesla = Car('Tesla',"Hybrid")
# tesla.model = 'Sonic'

print(tesla.model)