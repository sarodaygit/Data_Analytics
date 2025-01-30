# dog.py

class Dog:
    def __init__(self, name, breed, age):
        """Initialize the Dog object with name, breed, and age."""
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says Woof!"

    def get_details(self):
        """Return the details of the dog."""
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age} years"

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
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age} years, Training Level: {self.training_level}"

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
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age} years, Favorite Toy: {self.favorite_toy}"

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

    print(guard_dog.get_details())
    make_dog_bark(guard_dog)

    print(pet_dog.get_details())
    make_dog_bark(pet_dog)

# Ensuring script runs only when executed directly
if __name__ == "__main__":
    main()
