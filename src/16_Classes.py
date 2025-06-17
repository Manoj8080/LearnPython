class Car:

    location="amalapuram"
    def __init__(self,wheels,engine,color):
        self.wheels=wheels
        self.engine=engine
        self.color=color

    def display_info(self):
        print("car wheels:",self.wheels)
        print("car engine:",self.engine)
        print("car color:",self.color)

bmw=Car(4,"petrol","black")
audi=Car(4,"hybrid","white")

bmw.display_info()
audi.display_info()

bmw.seats=2

audi.gears=6
audi.speed=300

print(f"seats:{bmw.seats}")
print(f"gears:{audi.gears},speed:{audi.speed}")

print("bmw location: ",bmw.location)
print("audi location: ",audi.location)