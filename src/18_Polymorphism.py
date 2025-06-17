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

    def show_info(self):
        print("brand: ",self.brand)
        print("speed :",self.speed)

class Car(Vehicle):
    def __init__(self,brand,speed,fuel):
        super().__init__(brand,speed)
        self.fuel=fuel

    def show_info(self):
        super().show_info()
        print("fuel :",self.fuel)

vehicle=Vehicle("generic",90)
car=Car("toyota",300,"petrol")

vehicle.show_info()
car.show_info()