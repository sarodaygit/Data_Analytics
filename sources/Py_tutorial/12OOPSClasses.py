# Unified Example with Vehicle

# Class and Object
class Vehicle:
    def __init__(self, brand, model):
        # Constructor to initialize the brand and model of a vehicle
        self.brand = brand
        self.model = model

    def display_info(self):
        # Method to display vehicle information
        print(f"Brand: {self.brand}, Model: {self.model}")

# Encapsulation
class VehicleService:
    def __init__(self, service_date):
        # Constructor to initialize the service date (private attribute)
        self.__service_date = service_date  # Private attribute

    def update_service_date(self, new_date):
        # Method to update the service date
        self.__service_date = new_date

    def get_service_date(self):
        # Method to retrieve the current service date
        return self.__service_date

# Inheritance
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        # Constructor to initialize car-specific attributes
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_info(self):
        # Method to display car-specific information
        print(f"Brand: {self.brand}, Model: {self.model}, Fuel Type: {self.fuel_type}")

# Polymorphism
class Bike(Vehicle):
    def display_info(self):
        # Overridden method to display bike-specific information
        print(f"Brand: {self.brand}, Model: {self.model} - This is a Bike")

class VehicleManager:
    @staticmethod
    def show_vehicle_info(vehicle):
        # Static method to display information for any vehicle
        vehicle.display_info()

# Abstraction
from abc import ABC, abstractmethod

class VehiclePart(ABC):
    @abstractmethod
    def part_info(self):
        # Abstract method to provide part-specific information
        pass

class Engine(VehiclePart):
    def part_info(self):
        # Implementation of the abstract method for engine-specific information
        print("This is the engine of the vehicle.")

# Main code
if __name__ == "__main__":
    # Class and Object Example
    vehicle1 = Vehicle("Toyota", "Corolla")
    vehicle2 = Vehicle("Honda", "Civic")
    vehicle1.display_info()
    vehicle2.display_info()

    # Encapsulation Example
    service = VehicleService("2025-01-17")
    print("Service Date:", service.get_service_date())
    service.update_service_date("2025-06-20")
    print("Updated Service Date:", service.get_service_date())

    # Inheritance Example
    car = Car("Tesla", "Model S", "Electric")
    car.display_info()

    # Polymorphism Example
    bike = Bike("Yamaha", "YZF-R15")
    VehicleManager.show_vehicle_info(car)
    VehicleManager.show_vehicle_info(bike)

    # Abstraction Example
    engine = Engine()
    engine.part_info()
