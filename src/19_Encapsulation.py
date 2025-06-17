class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.__speed=speed #private variable

    def get_speed(self):
        return self.__speed

    def set_speed(self,new_speed):
        self.__speed=new_speed

    def show_info(self):
        print("brand :",self.brand)
        print("speed :",self.__speed)

class Car(Vehicle):
    def __init__(self,brand,speed,fuel):
        super().__init__(brand,speed)
        self.fuel=fuel

    def show_info(self):
        super().show_info()
        print("fuel :",self.fuel)

car= Car("toyota",250,"petrol")
print("initial speed :",car.get_speed())
car.set_speed(300)
print("updated speed :",car.get_speed())
car.show_info()