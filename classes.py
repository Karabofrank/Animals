"""
Five examples of classes from Gemini, Animals,Shape calculator, Bank Account,
Employee management and Inventory system.
"""

class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age  

    def make_sound(self):
        print("The animal makes a sound")

    def display_info(self):
        print("Species:", self.species)
        print("Name:", self.name)
        print("Age:", self.age)

# Animal Shelter
class Dog(Animal):
    def __init__(self, name, age, breed, is_house_trained):
        super().__init__("Dog", name, age)
        self.breed = breed
        self.is_house_trained = is_house_trained

    def make_sound(self):
        print("The dog barks")

    def display_info(self):
        super().display_info()
        print("Breed:", self.breed)
        print("House Trained:", self.is_house_trained)

class Cat(Animal):
    def __init__(self, name, age, is_declawed, favorite_toy):
        super().__init__("Cat", name, age)
        self.is_declawed = is_declawed
        self.favorite_toy = favorite_toy

    def make_sound(self):
        print("The cat meows")

    def display_info(self):
        super().display_info()
        print("Declawed:", self.is_declawed)
        print("Favorite Toy:", self.favorite_toy)

class Bird(Animal):
    def __init__(self, name, age, is_cage_trained):
        super().__init__("Bird", name, age)
        self.is_cage_trained = is_cage_trained

    def make_sound(self):
        print("The bird chirps")

    def display_info(self):
        super().display_info()
        print("Cage Trained:", self.is_cage_trained)
        
# Create instances of the Animal, Dog, Cat, and Bird classes
animal = Animal("Animal", "Generic", 0)
dog = Dog("Fido", 5, "Labrador", True)
cat = Cat("Mia", 3, False, "Tennis Ball")
bird = Bird("Buddy", 2, True)

# Demonstrate method calls
animal.make_sound()
dog.make_sound()
cat.make_sound()
bird.make_sound()

# Display information about the instances
animal.display_info()
dog.display_info()
cat.display_info()
bird.display_info()
