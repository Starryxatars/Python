class Vehicle:
    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print("Car: Press the start button, the engine turns on smoothly.")


class Bike(Vehicle):
    def start(self):
        print("Bike: Kick/self-start, the engine roars to life.")


class Bus(Vehicle):
    def start(self):
        print("Bus: Driver turns the key, air brakes release, the bus moves off.")


for v in (Car(), Bike(), Bus()):
    v.start()
