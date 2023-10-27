class Vehicle:
    ''' Base class for all vehicles '''
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    ''' This method displays the brand and model of the vehicle'''
    def display_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}")

class Truck(Vehicle):
    ''' This class inherits from the Vehicle class. It has an additional attribute called load_capacity.'''
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity
    ''' This method displays the brand, model and load capacity of the truck.'''
    def display_info(self):
        super().display_info()
        print(f"Capacity: {self.load_capacity} tons")


if __name__ == "__main__":
    truck1 = Truck("Mercedes", "Actros", 40)
    truck1.display_info()
    truck2 = Truck("Volvo", "FH", 50)
    truck2.display_info()