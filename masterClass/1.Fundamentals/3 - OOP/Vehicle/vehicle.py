class Vehicle:
    def __init__(self, name, speed, model, engine_type, year, color, signal=None, insurance=None):
        self.name = name
        self.speed = speed
        self.model = model
        self.engine_type = engine_type
        self.year = year
        self.color = color
        self.signal = signal
        self.insurance = insurance

    def drive(self):
        start_speed = 5
        print(f"{self.name} is driving at {self.speed} + {start_speed}  km/h")
    def stop(self):
        print(f"{self.name} has stopped.")
    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.name} has accelerated to {self.speed} km/h")
    def honk(self):
        print(f"{self.name} is honking!")
    def __str__(self):
        return f"{self.year} {self.color} {self.name} {self.model} with {self.engine_type} engine"
    def crash(self):
        print(f"{self.name} has crashed!")
    def repair(self):
        print(f"{self.name} is being repaired.")
        print(f"{self.name} is now repaired.")
        print(f"{self.name} is ready to drive again. Call {self.insurance} for insurance details.")
    
 