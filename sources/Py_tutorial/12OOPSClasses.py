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

# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Beagle", 2)

# Calling methods on the objects
print(dog1.get_details())  # Output: Name: Buddy, Breed: Golden Retriever, Age: 3 years
print(dog1.bark())         # Output: Buddy says Woof!

print(dog2.get_details())  # Output: Name: Max, Breed: Beagle, Age: 2 years
print(dog2.bark())         # Output: Max says Woof!
