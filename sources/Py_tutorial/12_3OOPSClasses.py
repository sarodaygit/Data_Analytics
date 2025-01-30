from abc import ABC, abstractmethod

# Abstract Class: Canine (Abstraction)
class Canine(ABC):
    def __init__(self, name, breed, age):
        """Initialize the Canine object with name, breed, and age."""
        self.name = name
        self.breed = breed
        self.__age = age  # Private attribute

    @abstractmethod
    def bark(self):
        """Abstract method to enforce bark implementation."""
        pass

    def get_age(self):
        """Encapsulated method to get the dog's age."""
        return self.__age

    def set_age(self, new_age):
        """Set a new age with validation."""
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age! Age must be positive.")

    def get_details(self):
        """Common method to return dog details."""
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.__age} years"

    def sleep(self):
        """Common behavior for all dogs."""
        return f"{self.name} is sleeping!"

# Subclass: Dog
class Dog(Canine):
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says Woof!"
    
    def fetch(self, item):
        """A common method for all dogs to fetch an item."""
        return f"{self.name} runs to fetch the {item}!"

# Subclass: GuardDog (Inheritance)
class GuardDog(Dog):
    def __init__(self, name, breed, age, training_level):
        """Initialize a GuardDog with training level."""
        super().__init__(name, breed, age)
        self.training_level = training_level  # New attribute

    def bark(self):
        """Override the bark method to indicate a guard dog."""
        return f"{self.name} says Woof! Stay away, I'm guarding!"

    def get_details(self):
        """Return details of the guard dog."""
        return f"{super().get_details()}, Training Level: {self.training_level}"

# Subclass: PetDog (Polymorphism)
class PetDog(Dog):
    def __init__(self, name, breed, age, favorite_toy):
        """Initialize a PetDog with a favorite toy."""
        super().__init__(name, breed, age)
        self.favorite_toy = favorite_toy  # New attribute

    def bark(self):
        """Override the bark method to indicate a friendly pet dog."""
        return f"{self.name} says Woof! Let's play!"

    def get_details(self):
        """Return details of the pet dog."""
        return f"{super().get_details()}, Favorite Toy: {self.favorite_toy}"

# Function demonstrating polymorphism
def make_dog_bark(dog):
    """Function to make any dog bark."""
    print(dog.bark())

# Main function to create instances and demonstrate behavior
def main():
    # Creating instances
    dog1 = Dog("Buddy", "Golden Retriever", 3)
    guard_dog = GuardDog("Rex", "German Shepherd", 5, "Advanced")
    pet_dog = PetDog("Bella", "Labrador", 2, "Rubber Ball")

    # Displaying details and calling methods
    print(dog1.get_details())
    make_dog_bark(dog1)
    print(dog1.sleep())  # Demonstrating common behavior
    print(dog1.fetch("ball"))  # Using fetch method

    print(guard_dog.get_details())
    make_dog_bark(guard_dog)
    print(guard_dog.sleep())
    print(guard_dog.fetch("stick"))  # GuardDog can also fetch

    print(pet_dog.get_details())
    make_dog_bark(pet_dog)
    print(pet_dog.sleep())
    print(pet_dog.fetch("frisbee"))  # PetDog fetching frisbee

    # Demonstrating encapsulation (Updating Age)
    pet_dog.set_age(3)  # Updating age using setter
    print(f"Updated Age: {pet_dog.get_age()} years")

# Ensuring script runs only when executed directly
if __name__ == "__main__":
    main()
