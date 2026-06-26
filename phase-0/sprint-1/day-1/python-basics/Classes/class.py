
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f"Woof!, I'm {self.name}")

    def describe(self):
        print(f"{self.name} is a {self.breed}, {self.age} years old");

dog1 = Dog("Bruno", "Labrador", 3);
dog2 = Dog("Max", "Poodle", 5);

dog1.bark();

dog2.describe();
