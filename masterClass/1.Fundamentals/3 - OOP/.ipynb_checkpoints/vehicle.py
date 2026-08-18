class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color  # Optional attribute for color

    def start(self):
        return f"{self.year} {self.make} {self.model} is starting."

    def stop(self):
        return f"{self.year} {self.make} {self.model} is stopping."

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
# Example usage:
if __name__ == "vehicle.py":
    my_vehicle = Vehicle("Toyota", "Corolla", 2020, "blue")
    print(my_vehicle.start())
    print(my_vehicle.stop())
    print(my_vehicle)
# This code defines a Vehicle class with attributes for make, model, and year.
# It includes methods to start and stop the vehicle, and a string representation method.
# The example usage creates an instance of the Vehicle class and demonstrates its methods.
# The Vehicle class can be extended to include more features like fuel type, color, etc.
# This code defines a Vehicle class with attributes for make, model, and year.
# It includes methods to start and stop the vehicle, and a string representation method.
# The example usage creates an instance of the Vehicle class and demonstrates its methods.
# The Vehicle class can be extended to include more features like fuel type, color, etc.
# This code defines a Vehicle class with attributes for make, model, and year.      



class Car(Vehicle):
    def __init__(self, make, model, year, color, num_doors):
        super().__init__(make, model, year, color)
        self.num_doors = num_doors  # Additional attribute for number of doors

    def open_trunk(self):
        return f"{self.year} {self.make} {self.model}'s trunk is now open."

    def __str__(self):
        return f"{super().__str__()} with {self.num_doors} doors"
# Example usage: