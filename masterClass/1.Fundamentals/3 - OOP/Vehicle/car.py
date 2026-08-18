import Vehicle

class Car(Vehicle):
    def __init__(self, name, speed, model, engine_type, year, color, signal=None, insurance=None):
        super().__init__(name, speed, model, engine_type, year, color, signal, insurance)

    def drive(self):
        super().drive()
        print(f"{self.name} is a car.")

    def honk(self):
        super().honk()
        print(f"{self.name} is honking like a car!")
