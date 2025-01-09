# Animal Classes
================

This project provides a collection of classes representing different types of animals, including `Animal`, `Dog`, `Cat`, and `Bird`. Each class has its own attributes and methods, allowing for basic interactions and information display.

## Classes

* `Animal`: The base class for all animals, with attributes for species, name, and age.
* `Dog`: A subclass of `Animal`, with additional attributes for breed and house training status.
* `Cat`: A subclass of `Animal`, with additional attributes for declawed status and favorite toy.
* `Bird`: A subclass of `Animal`, with an additional attribute for cage training status.

## Methods

* `make_sound()`: A method that prints a sound made by the animal.
* `display_info()`: A method that prints information about the animal, including its species, name, age, and any additional attributes specific to the class.

## Examples

You can create instances of these classes and interact with them as shown in the example code:
```python
animal = Animal("Animal", "Generic", 0)
dog = Dog("Fido", 5, "Labrador", True)
cat = Cat("Mia", 3, False, "Tennis Ball")
bird = Bird("Buddy", 2, True)

animal.make_sound()
dog.make_sound()
cat.make_sound()
bird.make_sound()

animal.display_info()
dog.display_info()
cat.display_info()
bird.display_info()
```
This will output the sounds made by each animal, followed by their respective information.

## Contributing

If you'd like to contribute to this project or suggest additional features, please feel free to open an issue or submit a pull request.

Note that this is just a basic draft, and you can add or modify sections as needed to fit your project's specific needs.