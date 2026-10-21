class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    @staticmethod
    def general_descriptio():
        return f"Car is mean of transport"

tesla = Car('Tesla','Hybrid')
print(tesla.general_descriptio())