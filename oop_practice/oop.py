# Create a Vehicle class

class Vehicle:
    # Assign attributes max_speed and mileage
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # Set default color as a class variable
    color = "White"

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def __str__(self):
        return f"Color: {self.color} Vehicle Name: {self.name} Speed: {self.max_speed} Mileage {self.mileage}"

# Create a Bus class
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

    # Display info to user when print() is called
    def __str__(self):
        return super().__str__()

class Car(Vehicle):
    pass

bus = (Bus("School Volvo", 180, 12))
print(bus)