#syntax
'''class ParentClass:
    #attributes / methods
    pass
class ChildClass(ParentClass):
    # attributes / methods
    pass'''

class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def display_vehicle_info(self):
        print("brand: ",self.brand)
        print("speed :",self.speed)

class Car(Vehicle):
    def __init__(self,brand,speed,fuel):
        super().__init__(brand,speed)
        self.fuel=fuel

    def display_car_info(self):
        self.display_vehicle_info()
        print("fuel :",self.fuel)

my_car=Car("toyota",250,"petrol")
your_car=Car("mahindra",300,"disel")
my_car.display_car_info()
your_car.display_car_info()